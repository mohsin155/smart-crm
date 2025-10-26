from sqlmodel import SQLModel, Session
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

DatabaseUrl = "postgresql+asyncpg://kumaran:123456@localhost:5432/crm"

# dbEngine = create_async_engine(DatabaseUrl, echo=True)

# async_session = sessionmaker(
#     dbEngine, class_=AsyncSession, expire_on_commit=False
# )

# async def init_db():
#     async with dbEngine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)

# async def get_session():
#     async with async_session() as session:
#         yield session


class Database:
    def __init__(self):
        self.engine = create_async_engine(DatabaseUrl, echo=True)
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def init_db(self):
        from src.infrastructure.models.users import Users
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session(self):
        async with self.async_session() as session:
            yield session


db = Database()