from core.db import Base

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from sqlmodel import SQLModel, Field

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())
    user = Column(String)


class DataTest(Base):
    __tablename__ = "data_test"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)

# class DataBase1(SQLModel):
#     name: str
#
# class Value(DataBase1, table=True):
#     sum: int = Field(default=None, primary_key=True)


# DataBase1 это базовая модель, от которой наследуются другие.
# У неё есть два свойства name и artist, оба из которых являются строками.
# Это модель только для данных, так как в ней нет table=True, она используется только в качестве модели pydantic.
#
# Value Тем временем добавляет sum в базовую модель.
# Это табличная модель, так что это модель pydantic и SQLAlchemy.
# Она представляет собой таблицу базы данных.