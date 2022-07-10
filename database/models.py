from core.db import Base

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())
    user = Column(String)
