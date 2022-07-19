from sqlalchemy.orm import Session
from abc import ABC
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from core import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(ABC):
    model = NotImplemented

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        # В ассинхронном режиме sqlalchemy orm не доступен.
        # data = await db.execute(self.model).filter(self.model.id == id).first()  # 3
        # Нужно импользовать sqlalchemy core
        data = await db.get(self.model, id)
        return data

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()  # 4

    async def create(self, db: AsyncSession, **kwargs) -> ModelType:
        db_obj = self.model(**kwargs)
        db.add(db_obj)
        # db.commit()   # Для синхронного запуска
        # db.refresh(db_obj)
        return await db.commit()  # Для ассинхронного запуска
