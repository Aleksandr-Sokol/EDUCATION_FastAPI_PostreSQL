from fastapi import FastAPI
from view import router as data_router
from view_file import router as file_router
from tasks import router as task_router

my_api = FastAPI()

@my_api.get("/")
async def root():
    return {"message": "Hello World"}


my_api.include_router(data_router)
my_api.include_router(file_router)
my_api.include_router(task_router)
