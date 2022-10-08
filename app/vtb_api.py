import requests

from settings import Settings


def vtb_create_wallet():
    s = Settings()
    response = requests.post(f'{s.base_url}/v1/wallets/new')
    return response.json()


