import requests
from typing import Dict, List, Union

from settings import Settings

s = Settings()


# TODO: camel-to-snake utilities


def vtb_create_wallet() -> Dict[str, str]:
    response = requests.post(f"{s.base_url}/v1/wallets/new").json()
    return {"private_key": response["privateKey"], "public_key": response["publicKey"]}


def vtb_matic_transfer(from_private: str, to_public: str, amount: float) -> str:
    body = {"fromPrivateKey": from_private, "toPublicKey": to_public, "amount": amount}
    response = requests.post(f"{s.base_url}/v1/transfers/matic", data=body).json()
    return response["transactionHash"]


def vtb_ruble_transfer(from_private: str, to_public: str, amount: float) -> str:
    body = {"fromPrivateKey": from_private, "toPublicKey": to_public, "amount": amount}
    response = requests.post(f"{s.base_url}/v1/transfers/ruble", data=body).json()
    return response["transactionHash"]


def vtb_transfer_nft(from_private: str, to_public: str, token_id: int) -> str:
    body = {"fromPrivateKey": from_private, "toPublicKey": to_public, "tokenId": token_id}
    response = requests.post(f"{s.base_url}/v1/transfers/nft", data=body).json()
    return response["transactionHash"]


def vtb_check_transaction_status(transaction_hash: str) -> str:
    response = requests.post(f"{s.base_url}/v1/transfers/status/{transaction_hash}").json()
    return response["status"]


def vtb_get_balance(public_key: str) -> Dict[str, float]:
    response = requests.get(f"{s.base_url}/v1/wallets/{public_key}/balance").json()
    return {"matic_amount": response["maticAmount"], "coins_amount": response["coinsAmount"]}


def vtb_get_balance_nft(public_key: int) -> List[Dict[str, Union[str, List[int]]]]:
    response = requests.get(f"{s.base_url}/v1/wallets/{public_key}/nft/balance").json()
    return response["balance"]


def vtb_generate_nft(public_key: str, uri: str, nft_count: int) -> str:
    body = {"publicKey": public_key, "uri": uri, "nftCount": nft_count}
    response = requests.post(f"{s.base_url}/v1/nft/generate", data=body).json()
    return response["transactionHash"]


def vtb_get_nft_info(token_id: int) -> Dict[str, Union[int, str]]:
    response = requests.get(f"{s.base_url}/v1/nft/{token_id}").json()
    return {"token_id": response["tokenId"], "uri": response["uri"], "public_key": response["publicKey"]}


def vtb_get_nft_list(transaction_hash: str) -> List[Dict[str, Union[str, List[int]]]]:
    response = requests.get(f"{s.base_url}/v1/nft/generate/{transaction_hash}").json()
    return response


def vtb_get_transaction_history(
    public_key: str, page: int = 1, offset: int = 20, sort: str = "asc"
) -> List[Dict[str, Union[str, int]]]:
    body = {'page': page, 'offset': offset, 'sort': sort}
    response = requests.post(f'{s.base_url}/v1/wallets/{public_key}/history', data=body).json()
    return response['history']
