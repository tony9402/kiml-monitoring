import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_async_engine(
    os.environ["POSTGRES_ASYNC_URL"],
    pool_size=20,
    echo=True,
    pool_pre_ping=True,
)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)  # noqa: E501


async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session
