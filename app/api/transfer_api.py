from fastapi import APIRouter

from app.types import TransferMaticInput
from app.vtb_api import vtb_matic_transfer


transfer_router = APIRouter(prefix='/transfer')


@transfer_router.post('/transfer_matic')
def transfer_matic(transfer_input: TransferMaticInput) -> bool:
    vtb_matic_transfer(transfer_input.from_private_key, transfer_input.to_public_key, transfer_input.amount)
    return True
