from sqlalchemy.orm import Session
from abc import ABC
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from core import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(ABC):  # 1
    # def __init__(self, model: Type[ModelType]):  # 2
    #     """
    #     CRUD object with default methods to Create, Read, Update, Delete (CRUD).
    #     **Parameters**
    #     * `model`: A SQLAlchemy model class
    #     * `schema`: A Pydantic model (schema) class
    #     """
    #     self.model = model
    model = NotImplemented

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()  # 3

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()  # 4

    def create(self, db: Session, **kwargs) -> ModelType:
        # obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**kwargs)  # type: ignore
        db.add(db_obj)
        db.commit()  # 5
        db.refresh(db_obj)
        return db_obj
