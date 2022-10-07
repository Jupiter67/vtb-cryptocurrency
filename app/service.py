"""
API start here
"""

from fastapi import APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import SessionLocal
from app.models import Wallet
from app.value_objects import Wallet as WalletObject


router = APIRouter()


@router.get("/get_wallet/{user_id}")
async def get_wallet_by_id(user_id: int):
    """
    Creates new wallet

    :param: user_id: id of user
    :return: wallet object
    """
    async with SessionLocal() as s:
        s: AsyncSession
        async with s.begin():
            query = select(Wallet).where(Wallet.user_id == user_id)
            result = await s.execute(query)
            result = result.fetchone()
        return WalletObject.from_orm(result['Wallet']).__dict__
