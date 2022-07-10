from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import Depends
from shcemas.schema_data import DataBaseSchema, DataSchema

from crud.data_crud import DataCRUD
from core.db import get_db

my_api = FastAPI()

@my_api.get("/")
async def root():
    return {"message": "Hello World"}


@my_api.get("/data/{data_id}", response_model=DataSchema)
async def data(data_id, db: Session = Depends(get_db)) -> DataSchema:
    data_crud = DataCRUD()
    data_i = data_crud.get(db, data_id)
    return data_i

@my_api.post("/data", response_model=DataSchema)
async def create(data: DataBaseSchema, db: Session = Depends(get_db)):
    data_crud = DataCRUD()
    data_i = data_crud.create(db, **data.dict(exclude_unset=True))
    return data_i
