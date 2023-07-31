from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import (
    Boolean, 
    Column, 
    String, 
    Text, 
    BigInteger,
    TIMESTAMP,
)


Base = declarative_base() 


class StatusDao(Base):
    __tablename__ = "status"
    id = Column("id", BigInteger, primary_key=True)
    uuid = Column("uuid", String, nullable=True)
    status = Column("status", String, nullable=False)
    run_name = Column("run_name", String, nullable=False)
    experiment_name = Column("experiment_name", String, nullable=False)
    image = Column("image", String, nullable=False)
    instance_type = Column("instance_type", String, nullable=False)
    create_time = Column("create_time", TIMESTAMP, nullable=True)
    start_time = Column("start_time", TIMESTAMP, nullable=True)
    end_time = Column("end_time", TIMESTAMP, nullable=True)