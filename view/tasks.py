from fastapi import BackgroundTasks, APIRouter
from time import sleep
from shcemas.schema_data import MessageSchema

router = APIRouter(
    prefix="/task",
    responses={404: {"description": "Sorry Not found"}},
)


def sleep_task(message: str):
    sleep(10)
    print(f'sleep_task: {message}')


@router.get("/start")
async def send_message(background_tasks: BackgroundTasks):
    background_tasks.add_task(sleep_task, 'Complite')
    return 'send complitly'


@router.post("/")
async def send_message(background_tasks: BackgroundTasks, data: MessageSchema):
    background_tasks.add_task(sleep_task, data.text)
    return 'send complitly'
