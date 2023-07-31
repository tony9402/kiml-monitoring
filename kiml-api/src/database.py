from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_async_engine('postgresql+asyncpg://user:pass@server_addr/database', echo=True, pool_pre_ping=True)


async def get_db_session() -> AsyncSession:
    sess = AsyncSession(bind=engine)
    try:
        yield sess
    finally:
        await sess.close()