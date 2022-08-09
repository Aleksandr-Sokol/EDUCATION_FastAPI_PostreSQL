from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
import time


class SimpleMiddleware(BaseHTTPMiddleware):
    """
    Пример пользовательского middleware
    """
    def __init__(self, app, some_attribute: str):
        """
        :param some_attribute:  Некий атрибут переданный в middleware
        """
        super().__init__(app)
        self.some_attribute = some_attribute

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        start_time = time.time()
        content_type = request.headers.get('Content-Type')
        response = await call_next(request)
        response.headers["X-Process-Time"] = str(time.time() - start_time)
        return response
