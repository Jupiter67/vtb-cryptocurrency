"""
API start here
"""

from fastapi import APIRouter
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import SessionLocal
from app.models import Wallet
from app.value_objects import Wallet as WalletObject
from app.types import WalletInput


router = APIRouter()


@router.get("/get_wallet/{user_id}")
async def get_wallet_by_id(user_id: int) -> dict:
    """
    Gets wallet by user id

    :param: user_id: id of user
    :return: wallet object
    """
    async with SessionLocal() as s:
        s: AsyncSession
        async with s.begin():
            query = select(Wallet).where(Wallet.user_id == user_id)
            result = await s.execute(query)
            result = result.fetchone()
        return WalletObject.from_orm(result["Wallet"]).__dict__


@router.post("/create_wallet")
async def create_wallet(w_input: WalletInput) -> dict:
    async with SessionLocal() as s:
        s: AsyncSession
        async with s.begin():
            w = Wallet(**w_input.__dict__)
            s.add(w)
        await s.refresh(w)
    return WalletObject.from_orm(w).__dict__


@router.delete('/delete_wallet/{wallet_id}')
async def delete_wallet(wallet_id: int) -> bool:
    async with SessionLocal() as s:
        s: AsyncSession
        async with s.begin():
            query = delete(Wallet).where(Wallet.id == wallet_id)
            await s.execute(query)
    return True
