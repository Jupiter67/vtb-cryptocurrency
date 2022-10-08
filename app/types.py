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
    def field_exists(cls, v):
        if not v:
            raise ValueError('Fields must be not empty')
        return v


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


class GenerateNftInput(BaseModel):
    to_public_key: str
    uri: str
    nft_count: int

    @validator('to_public_key', 'uri', 'nft_count')
    def field_exists(cls, v):
        if not v:
            raise ValueError('Fields must be not empty')
        return v

    @validator('nft_count')
    def nft_count_greater_zero(cls, v):
        if v > 0:
            return v
        raise ValueError('NFT count must be greater than zero')

