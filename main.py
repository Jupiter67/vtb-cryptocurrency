from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI

from app.service import router
from settings import Settings


settings = Settings()
app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    config = Config()
    config.bind = f'{settings.host}:{settings.port}'
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
