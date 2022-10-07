from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.service import foo
from settings import Settings


settings = Settings()
app = FastAPI(routes=[
    APIRoute('/foo', foo, methods=['GET'])
])

if __name__ == '__main__':
    config = Config()
    config.bind = f'{settings.host}:{settings.port}'
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
