import asyncio
import aiohttp
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from typing import List, Optional, Any, Dict


router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Sorry Not found"}},
)


async def request_get_html(url, session, auth, headers):
    """
    Для ассинхронных запросов
    ответ от сервера в формате HTML
    """
    async with session.get(url, auth=auth, headers=headers, allow_redirects=True) as response:
        return await response.read()


async def request_get_json(url, session, auth, headers):
    """
    Для ассинхронных запросов
    ответ от сервера в формате JSON
    """
    async with session.get(url, auth=auth, headers=headers, allow_redirects=True) as response:
        return await response.json()


@router.get("/{view_profile_id}", response_class=ORJSONResponse)
async def device(view_profile_id: str):
    """
    Запрос для ассинхронной отправки нескольких запросов
    """
    headers = {
        'view-profile-id': view_profile_id,
    }
    login = 'Ivan'
    password = '123'
    auth = aiohttp.BasicAuth(login, password)

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(request_get_html(f'https://ya.ru', session, auth, headers), name='ya_1'),
                 asyncio.create_task(request_get_html(f'https://ya.ru', session, auth, headers), name='ya_2'),
                 ]
        await asyncio.gather(*tasks)
        results: List[Dict[Any, Any]] = await asyncio.gather(*tasks)  # wait for all async operations
    return results
