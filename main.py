from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI

from app.api.transfer_api import transfer_router
from app.api.wallet_api import wallet_router
from settings import Settings


settings = Settings()
app = FastAPI()
app.include_router(wallet_router)
app.include_router(transfer_router)

if __name__ == '__main__':
    config = Config()
    config.bind = f'{settings.host}:{settings.port}'
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
