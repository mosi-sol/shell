# SPDX-License-Identifier: MIT
from typing import Dict
from web3 import Web3

class MyToken:

    _balances: Dict[str, Dict[int, int]] = dict()
    _operators: Dict[str, Dict[str, bool]] = dict()
    _token_metadata: Dict[int, str] = dict()
    _name: str = ""
    _symbol: str = ""

    def __init__(self, name: str, symbol: str, web3: Web3):
        self._name = name
        self._symbol = symbol
        self.web3 = web3

    def supports_interface(self, interface_id: bytes) -> bool:
        return interface_id == self.web3.sha3(text="IERC1155").hex() or interface_id == self.web3.sha3(text="IERC1155MetadataURI").hex()

    def balance_of(self, account: str, token_id: int) -> int:
        return self._balances.get(account, dict()).get(token_id, 0)

    def balance_of_batch(self, accounts: List[str], token_ids: List[int]) -> List[int]:
        return [self.balance_of(accounts[i], token_ids[i]) for i in range(len(accounts))]

    def set_approval_for_all(self, operator: str, approved: bool) -> None:
        sender = self.web3.eth.default_account
        if operator == sender:
            raise ValueError("ERC1155: approve to caller")
        self._operators.setdefault(sender, dict())[operator] = approved

    def is_approved_for_all(self, account: str, operator: str) -> bool:
        return self._operators.get(account, dict()).get(operator, False)

    def safe_transfer_from(self, frm: str, to: str, token_id: int, amount: int, data: bytes) -> None:
        self._transfer(frm, to, token_id, amount)
        if self.web3.isAddress(to) and self.web3.eth.getCode(to) != "0x":
            to_contract = self.web3.eth.contract(address=to, abi=IERC1155Receiver.abi)
            receiver_selector = self.web3.sha3(text="onERC1155Received(address,address,uint256,uint256,bytes)").hex()
            result = to_contract.functions.onERC1155Received(self.web3.eth.default_account, frm, token_id, amount, data).call()
            if result != receiver_selector:
                raise ValueError("ERC1155: transfer to non ERC1155Receiver implementer")

    def safe_batch_transfer_from(self, frm: str, to: str, token_ids: List[int], amounts: List[int], data: bytes) -> None:
        if len(token_ids) != len(amounts):
            raise ValueError("ERC1155: ids and amounts length mismatch")
        for i in range(len(token_ids)):
            self._transfer(frm, to, token_ids[i], amounts[i])
        if self.web3.isAddress(to) and self.web3.eth.getCode(to) != "0x":
            to_contract = self.web3.eth.contract(address=to, abi=IERC1155Receiver.abi)
            receiver_selector = self.web3.sha3(text="onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)").hex()
            result = to_contract.functions.onERC1155BatchReceived(self.web3.eth.default_account, frm, token_ids, amounts, data).call()
            if result != receiver_selector:
                raise ValueError("ERC1155: transfer to non ERC1155Receiver implementer")

    def _transfer(self, frm: str, to: str, token_id: int, amount: int) -> None:
        sender = self.web3.eth.default_account
        if frm != sender and not self.is_approved_for_all(frm, sender):
            raise ValueError("ERC1155: caller is not owner nor approved")
        self._balances.setdefault(to, dict())[token_id] += amount
        self._balances.setdefault(frm, dict())[token_id] -= amount
        if self._balances[frm][token_id] == 0:
            del self._balances[frm][token_id]

    def set_token_uri(self, token_id: int, uri: str) -> None:
        self._token_metadata[token_id] = uri

    def token_uri(self, token_id: int) -> str:
        return self._token_metadata.get(token_id, "")
