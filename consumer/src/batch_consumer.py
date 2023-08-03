import os
import time

from dotenv import load_dotenv
from kiml.login import login_kiml
from kiml.run import get_run_list
from kiml.utils import convert_run_dict
from kiml.workspace import kiml_set_workspace
from models.status import StatusDao
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def batch():
    sess = Session()
    run_list: list = get_run_list()
    insert_datas = []
    update_datas = []
    exist_uuid = sess.query(StatusDao.uuid).all()
    exist_uuid = set([x.uuid for x in exist_uuid])
    run_uuids = []
    for run in run_list:
        data = run.to_dict()
        data = convert_run_dict(data)

        if data["uuid"] in exist_uuid:
            update_datas.append(data)
        else:
            insert_datas.append(data)

        run_uuids.append(data["uuid"])

    sess.query(StatusDao).filter(StatusDao.uuid.not_in(run_uuids)).delete()
    sess.bulk_insert_mappings(StatusDao, insert_datas)
    sess.bulk_update_mappings(StatusDao, update_datas)

    sess.commit()
    sess.flush()
    sess.close()


def cron_batch():
    while True:
        batch()
        time.sleep(30)  # * 60) # 10 minutes


def main():
    cron_batch()


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
            break
        except Exception:
            continue
    Session = sessionmaker(engine, autocommit=False, autoflush=False)
    main()
