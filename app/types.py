"""
Вот на этом моменте я сдался и смирился с правилами FastAPI.
Наполовину...
"""

from pydantic import BaseModel, validator


class WalletInput(BaseModel):
    user_id: int
    private_key: str
    public_key: str

    @validator('private_key', 'public_key', 'user_id')
    def key_exists(cls, v):
        if not v:
            raise ValueError('Fields must be not empty')
        return v


class TransferMaticInput(BaseModel):
    from_private_key: str
    to_public_key: str
    amount: float

    @validator('from_private_key', 'to_public_key')
    def key_exists(cls, v):
        if not v:
            raise ValueError('Keys must be not empty')
        return v

    @validator('amount')
    def amount_greater_zero(cls, v):
        if v <= 0:
            raise ValueError('Amount must be greater than zero')
        return v
