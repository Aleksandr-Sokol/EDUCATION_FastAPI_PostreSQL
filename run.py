import uvicorn
from app import my_api

uvicorn.run(my_api, host="0.0.0.0", port=5005)
