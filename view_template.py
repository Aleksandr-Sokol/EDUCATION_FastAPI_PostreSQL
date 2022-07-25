from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="",
    responses={404: {"description": "Sorry Not found"}},
)

# Должна существовать директория templates/ в которой лежат html файлы
# (PUG не настроен)
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",  {"request": request})
    # Если нужно передать {{id}} в html шаблон
    # return templates.TemplateResponse("item.html", {"request": request, "id": id})
