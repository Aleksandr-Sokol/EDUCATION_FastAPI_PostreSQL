from fastapi import FastAPI
from view import *
from middleware import *


my_app = FastAPI()

# Добавление пользовательского middleware
my_app.add_middleware(SimpleMiddleware, some_attribute="some attribute")

my_app.include_router(data_router)
my_app.include_router(file_router)
my_app.include_router(task_router)
my_app.include_router(template_router)
my_app.include_router(api_router)
