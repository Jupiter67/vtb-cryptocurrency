"""
Вот на этом моменте я сдался и смирился с правилами FastAPI.
Наполовину...
"""

from pydantic import BaseModel


class WalletInput(BaseModel):
    user_id: int
    private_key: str
    public_key: str
