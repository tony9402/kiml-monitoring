import os

import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from kiml.run import get_run_by_id, get_run_list
from models.status import StatusDao


def prestart():
    # sess = async_session()
    run_list: list = get_run_list()
    print(run_list[0].to_dict())


async def main():
    pass


if __name__ == "__main__":
    # load_dotenv()
    # engine = create_async_engine(os.environ['POSTGRES_URL'])
    # async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession())
    prestart()
    # asyncio.run(main())