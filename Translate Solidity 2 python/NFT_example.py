# SPDX-License-Identifier: MIT
from typing import Dict
from web3 import Web3

class MyNFT:

    _owners: Dict[int, str] = dict()
    _token_metadata: Dict[int, str] = dict()
    _name: str = ""
    _symbol: str = ""

    def __init__(self, name: str, symbol: str, web3: Web3):
        self._name = name
        self._symbol = symbol
        self.web3 = web3

    def supports_interface(self, interface_id: bytes) -> bool:
        return interface_id == self.web3.sha3(text="IERC721").hex() or interface_id == self.web3.sha3(text="IERC721Metadata").hex()

    def balance_of(self, account: str) -> int:
        return sum(1 for owner in self._owners.values() if owner == account)

    def owner_of(self, token_id: int) -> str:
        return self._owners.get(token_id, "")

    def safe_transfer_from(self, frm: str, to: str, token_id: int, data: bytes) -> None:
        self._transfer(frm, to, token_id)
        if self.web3.isAddress(to) and self.web3.eth.getCode(to) != "0x":
            to_contract = self.web3.eth.contract(address=to, abi=IERC721Receiver.abi)
            receiver_selector = self.web3.sha3(text="onERC721Received(address,address,uint256,bytes)").hex()
            result = to_contract.functions.onERC721Received(self.web3.eth.default_account, frm, token_id, data).call()
            if result != receiver_selector:
                raise ValueError("ERC721: transfer to non ERC721Receiver implementer")

    def _transfer(self, frm: str, to: str, token_id: int) -> None:
        if self.owner_of(token_id) != frm:
            raise ValueError("ERC721: transfer of token that is not own")
        self._owners[token_id] = to

    def set_token_uri(self, token_id: int, uri: str) -> None:
        self._token_metadata[token_id] = uri

    def token_uri(self, token_id: int) -> str:
        return self._token_metadata.get(token_id, "")
