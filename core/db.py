
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"  # Для синхронного запуска
SQLALCHEMY_ASYNC_DATABASE_URI = "sqlite+aiosqlite:///example.db"  # Для асинхронного запуска
# postgresql+asyncpg


engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URI, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionAsync = sessionmaker(autocommit=False, autoflush=False, bind=async_engine)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
Base: DeclarativeMeta = declarative_base()

# Для синхронного запуска
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Для асинхронного запуска
async def get_async_db() -> AsyncGenerator:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        finally:
            await session.close()
