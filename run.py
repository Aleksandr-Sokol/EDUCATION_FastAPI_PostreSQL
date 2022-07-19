import uvicorn
from app import my_api

uvicorn.run(my_api, host="127.0.0.1", port=5005)
