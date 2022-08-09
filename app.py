from fastapi import FastAPI
from view import *
from middleware import *
from fastapi.middleware.cors import CORSMiddleware


my_app = FastAPI()

# Добавление пользовательского middleware
my_app.add_middleware(SimpleMiddleware, some_attribute="some attribute")

my_app.include_router(data_router)
my_app.include_router(file_router)
my_app.include_router(task_router)
my_app.include_router(template_router)
my_app.include_router(api_router)

# CORS (Cross-Origin Resource Sharing)
# совместное использование ресурсов разных источников

allow_origins = [
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
my_app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # Список источников, которым должно быть разрешено отправлять запросы из разных источников.
    allow_credentials=True,
    allow_methods=["*"],  # Список методов HTTP, которые должны быть разрешены для запросов из разных источников
    allow_headers=["*"],  # Список заголовков HTTP-запросов, которые должны поддерживаться для запросов из разных источников
)
# allow_origin_regex - Строка регулярного выражения для сопоставления с источниками
# например 'https://.*\.example\.org'.
# allow_credentials - файлы cookie должны поддерживаться для запросов из разных источников
# expose_headers - Укажите любые заголовки ответов, которые должны быть доступны для браузера. По умолчанию []
# max_age - Устанавливает максимальное время в секундах для браузеров для кэширования ответов CORS. По умолчанию 600
