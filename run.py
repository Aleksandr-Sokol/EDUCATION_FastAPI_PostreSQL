import uvicorn
from app import my_app

uvicorn.run(my_app, host="0.0.0.0", port=5005)
