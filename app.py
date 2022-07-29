from fastapi import FastAPI
from view import *


my_api = FastAPI()

my_api.include_router(data_router)
my_api.include_router(file_router)
my_api.include_router(task_router)
my_api.include_router(template_router)
my_api.include_router(api_router)
