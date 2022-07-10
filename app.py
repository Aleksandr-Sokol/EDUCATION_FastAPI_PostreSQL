from fastapi import FastAPI
from view import router

my_api = FastAPI()

@my_api.get("/")
async def root():
    return {"message": "Hello World"}


my_api.include_router(router)
