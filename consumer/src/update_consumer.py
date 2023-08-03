import os
import time
from typing import List

from dotenv import load_dotenv
from kiml.login import login_kiml
from kiml.run import get_run_by_id
from kiml.utils import convert_run_dict
from kiml.workspace import kiml_set_workspace
from models.status import StatusDao
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

UPDATE_STATUS = [
    "Creating",
    "Deleting",
    "Pending",
    "Rebooting",
    "Running",
    "Starting",
    "Stopping",
    "Initalizing",
]


def update():
    sess = Session()
    datas: List[StatusDao] = (
        sess.query(StatusDao).filter(StatusDao.status.in_(UPDATE_STATUS)).all()
    )
    if len(datas) == 0:
        return
    update_datas: List[dict] = []
    for data in datas:
        latest_data: dict = get_run_by_id(data.uuid).to_dict()
        latest_data: dict = convert_run_dict(latest_data)
        update_datas.append(latest_data)

    print("Updated")
    sess.bulk_update_mappings(StatusDao, update_datas)
    sess.commit()
    sess.flush()
    sess.close()


def consumer():
    while True:
        update()
        time.sleep(5)  # 5 seconds


def main():
    consumer()


if __name__ == "__main__":
    load_dotenv()

    login_kiml(os.environ["KIML_ID"], os.environ["KIML_PW"])
    kiml_set_workspace(os.environ["KIML_WORKSPACE"])

    for count_of_try in range(10000):
        try:
            engine = create_engine(
                os.environ["POSTGRES_SYNC_URL"],
                pool_size=20,
                echo=True,
                pool_pre_ping=True,
            )
            print("Connected !")
            break
        except Exception:
            continue
    Session = sessionmaker(engine, autocommit=False, autoflush=False)
    main()
