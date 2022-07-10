from fastapi import APIRouter
from crud.data_crud import DataCRUD
from sqlalchemy.orm import Session
from fastapi import Depends
from shcemas.schema_data import DataBaseSchema, DataSchema
from core.db import get_db


router = APIRouter(
    prefix="/data",
    responses={404: {"description": "Sorry Not found"}},
)


@router.get("/{data_id}", response_model=DataSchema)
async def data(data_id, db: Session = Depends(get_db)) -> DataSchema:
    data_crud = DataCRUD()
    data_i = data_crud.get(db, data_id)
    return data_i

@router.post("/", response_model=DataSchema)
async def create(data: DataBaseSchema, db: Session = Depends(get_db)):
    data_crud = DataCRUD()
    data_i = data_crud.create(db, **data.dict(exclude_unset=True))
    return data_i