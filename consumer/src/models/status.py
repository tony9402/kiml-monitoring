from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StatusDao(Base):  # type: ignore
    __tablename__ = "status"
    uuid = Column("uuid", String, primary_key=True)
    status = Column("status", String, nullable=False)
    run_name = Column("run_name", String, nullable=False)
    experiment_name = Column("experiment_name", String, nullable=False)
    experiment_id = Column("experiment_id", String, nullable=False)
    image = Column("image", String, nullable=False)
    instance_type = Column("instance_type", String, nullable=False)
    create_time = Column("create_time", TIMESTAMP, nullable=True)
    start_time = Column("start_time", TIMESTAMP, nullable=True)
    end_time = Column("end_time", TIMESTAMP, nullable=True)
