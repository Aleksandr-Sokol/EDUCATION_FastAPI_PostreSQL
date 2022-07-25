from fastapi import APIRouter, UploadFile, File
from typing import List
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/file",
    responses={404: {"description": "Sorry Not found"}},
)


@router.get("/")
async def get_file():
    """
    """
    return FileResponse(
        'view_file.py',
        media_type='text',
        filename='file_name.py'
    )


@router.post("/upload")
async def upload(file: UploadFile = File(None)):
    """
    multipart у файла должно быть имя file
    """
    contents = await file.read()
    return contents


@router.post("/uploads")
async def uploads(files: List[UploadFile] = File(None)):
    """
    multipart у всех файлов должно быть имя files
    """
    list_names = []
    for file in files:
        list_names.append(file.filename)
    return ' '.join(list_names)
