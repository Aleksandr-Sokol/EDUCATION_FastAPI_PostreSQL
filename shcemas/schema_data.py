import datetime

from pydantic import BaseModel


class DataBaseSchema(BaseModel):
    title: str
    text: str
    date: datetime.datetime
    user: str

    class Config:
        orm_mode = True


class DataSchema(DataBaseSchema):
    id: int
