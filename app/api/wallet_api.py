"""
API start here
"""

from typing import Dict, Union

from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import SessionLocal
from app.models import Wallet
from app.value_objects import Wallet as WalletObject
from app.vtb_api import vtb_create_wallet


wallet_router = APIRouter(prefix='/wallet')


@wallet_router.get("/get_wallet/{user_id}")
async def get_wallet_by_id(user_id: int) -> Dict[str, Union[str, int]]:
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
        if result:
            return WalletObject.from_orm(result["Wallet"]).__dict__
        raise HTTPException(status_code=404, detail="Item not found")


@wallet_router.post("/create_wallet")
async def create_wallet(req: Request) -> Dict[str, int]:
    async with SessionLocal() as s:
        s: AsyncSession
        async with s.begin():
            r = await req.json()
            new_wallet = vtb_create_wallet()
            w = Wallet(
                user_id=int(r["user_id"]),
                private_key=new_wallet["private_key"],
                public_key=new_wallet["public_key"],
            )
            s.add(w)
        await s.refresh(w)
    return WalletObject.from_orm(w).__dict__


@wallet_router.delete("/delete_wallet/{wallet_id}")
async def delete_wallet(wallet_id: int) -> bool:
    async with SessionLocal() as s:
        s: AsyncSession
        async with s.begin():
            query = delete(Wallet).where(Wallet.id == wallet_id)
            await s.execute(query)
    return True