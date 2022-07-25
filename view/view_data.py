import asyncio
import time
from fastapi import APIRouter
from crud.data_crud import DataCRUD
from sqlalchemy.orm import Session
from fastapi import Depends
from shcemas.schema_data import DataBaseSchema, DataSchema
from core.db import get_db, get_async_db


router = APIRouter(
    prefix="/data",
    responses={404: {"description": "Sorry Not found"}},
)


@router.get("/{data_id}", response_model=DataSchema)
async def data(data_id: int, db: Session = Depends(get_async_db)) -> DataSchema:
    data_crud = DataCRUD()
    # Для синхронного запуска
    # data_i = data_crud.get(db, data_id)
    # return data_i
    return await data_crud.get(db, data_id)  # Для ассинхронного запуска

@router.post("/", response_model=DataSchema)
async def create(data: DataBaseSchema, db: Session = Depends(get_async_db)):
    data_crud = DataCRUD()
    # Для синхронного запуска
    # data_i = data_crud.create(db, **data.dict(exclude_unset=True))
    # return data_i
    return await data_crud.create(db, **data.dict(exclude_unset=True))  # Для ассинхронного запуска
