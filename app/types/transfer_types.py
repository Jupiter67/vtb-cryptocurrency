"""
Types for post requests on transfer
"""

from pydantic import BaseModel, validator


class TransferCoinInput(BaseModel):
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


class TransferMaticInput(TransferCoinInput):
    pass


class TransferRubleInput(TransferCoinInput):
    pass


class TransferNftInput(BaseModel):
    from_private_key: str
    to_public_key: str
    token_id: int

    @validator('from_private_key', 'to_public_key', 'token_id')
    def field_exists(cls, v):
        if not v:
            raise ValueError('Fields must be not empty')
        return v
