from sqlalchemy import Column, Integer, String

from app.db import Base


class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True)
    private_key = Column(String, nullable=False)
    public_key = Column(String, nullable=False)
