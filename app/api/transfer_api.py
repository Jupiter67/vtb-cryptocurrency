from fastapi import APIRouter

from app.types.transfer_types import TransferMaticInput, TransferRubleInput, TransferNftInput
from app.vtb_api import vtb_matic_transfer, vtb_ruble_transfer, vtb_transfer_nft


transfer_router = APIRouter(prefix='/transfer')


@transfer_router.post('/transfer_matic')
async def transfer_matic(transfer_input: TransferMaticInput) -> bool:
    await vtb_matic_transfer(
        transfer_input.from_private_key, transfer_input.to_public_key, transfer_input.amount
    )
    return True


@transfer_router.post('/transfer_ruble')
async def transfer_ruble(transfer_input: TransferRubleInput) -> bool:
    await vtb_ruble_transfer(
        transfer_input.from_private_key, transfer_input.to_public_key, transfer_input.amount
    )
    return True


@transfer_router.post('/transfer_nft')
async def transfer_nft(transfer_input: TransferNftInput) -> bool:
    await vtb_transfer_nft(
        transfer_input.from_private_key, transfer_input.to_public_key, transfer_input.token_id
    )
    return True
