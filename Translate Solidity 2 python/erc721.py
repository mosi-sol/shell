# SPDX-License-Identifier: MIT
from typing import Dict
from web3 import Web3

class MyNFT:

    _owners: Dict[int, str] = dict()
    _balances: Dict[str, int] = dict()
    _token_approvals: Dict[int, str] = dict()
    _operator_approvals: Dict[str, Dict[str, bool]] = dict()
    _name: str = ""
    _symbol: str = ""
    _base_uri: str = ""

    def __init__(self, name: str, symbol: str, web3: Web3):
        self._name = name
        self._symbol = symbol
        self.web3 = web3

    def supports_interface(self, interface_id: bytes) -> bool:
        return interface_id == self.web3.sha3(text="IERC721").hex() or interface_id == self.web3.sha3(text="IERC721Metadata").hex()

    def balance_of(self, owner: str) -> int:
        if owner == "0x0000000000000000000000000000000000000000":
            raise ValueError("ERC721: balance query for the zero address")
        return self._balances.get(owner, 0)

    def owner_of(self, token_id: int) -> str:
        owner = self._owners.get(token_id)
        if owner is None:
            raise ValueError("ERC721: owner query for nonexistent token")
        return owner

    def approve(self, to: str, token_id: int) -> None:
        owner = self.owner_of(token_id)
        if to == owner:
            raise ValueError("ERC721: approval to current owner")

        sender = self.web3.eth.default_account
        if sender != owner and not self.is_approved_for_all(owner, sender):
            raise ValueError("ERC721: approve caller is not owner nor approved for all")

        self._approve(to, token_id)

    def get_approved(self, token_id: int) -> str:
        if not self._exists(token_id):
            raise ValueError("ERC721: approved query for nonexistent token")

        return self._token_approvals.get(token_id, "")

    def set_approval_for_all(self, operator: str, approved: bool) -> None:
        sender = self.web3.eth.default_account
        if operator == sender:
            raise ValueError("ERC721: approve to caller")

        self._operator_approvals.setdefault(sender, dict())[operator] = approved

    def is_approved_for_all(self, owner: str, operator: str) -> bool:
        return self._operator_approvals.get(owner, dict()).get(operator, False)

    def transfer_from(self, frm: str, to: str, token_id: int) -> None:
        if not self._is_approved_or_owner(self.web3.eth.default_account, token_id):
            raise ValueError("ERC721: transfer caller is not owner nor approved")

        self._transfer(frm, to, token_id)

    def safe_transfer_from(self, frm: str, to: str, token_id: int) -> None:
        self.safe_transfer_from(frm, to, token_id, "")

    def safe_transfer_from(self, frm: str, to: str, token_id: int, data: bytes) -> None:
        if not self._is_approved_or_owner(self.web3.eth.default_account, token_id):
            raise ValueError("ERC721: transfer caller is not owner nor approved")
        self._safe_transfer(frm, to, token_id, data)

    def _safe_transfer(self, frm: str, to: str, token_id: int, data: bytes) -> None:
        self._transfer(frm, to, token_id)
        if self.web3.isAddress(to) and self.web3.eth.getCode(to) != "0x":
            to_contract = self.web3.eth.contract(address=to, abi=IERC721Receiver.abi)
            receiver_selector = self.web3.sha3(text="onERC721Received(address,address,uint256,bytes)").hex()
            result = to_contract.functions.onERC721Received(self.web3.eth.default_account, frm, token_id, data).call()
            if result != receiver_selector:
                raise ValueError("ERC721: transfer to non ERC721Receiver implementer")

    def _approve(self, to: str, token_id: int) -> None:
        self._token_approvals[token_id] = to

    def _exists(self, token_id: int) -> bool:
        return token_id in self._owners

    def _is_approved_or_owner(self, spender: str, token_id: int) -> bool:
        if not self._exists(token_id):
            raise ValueError("ERC721: operator query for nonexistent token")
        owner = self.owner_of(token_id)
        return spender == owner or self.get_approved(token_id) == spender or self.is_approved_for_all(owner, spender)

    def _transfer(self, frm: str, to: str, token_id: int) -> None:
        if self.owner_of(token_id) != frm:
            raise ValueError("ERC721: transfer of token that is not own")
        if to == "0x0000000000000000000000000000000000000000":
            raise ValueError("ERC721: transfer to the zero address")

        self._before_token_transfer(frm, to, token_id)

        self._approve("", token_id)

        self._balances[frm] -= 1
        self._balances[to] += 1
        self._owners[token_id] = to

    def _before_token_transfer(self, frm: str, to: str, token_id: int) -> None:
        pass

    def set_base_uri(self, base_uri: str) -> None:
        self._base_uri = base_uri

    def token_uri(self, token_id: int) -> str:
        if not self._exists(token_id):
            raise ValueError("ERC721Metadata: URI query for nonexistent token")

        if self._base_uri == "":
            raise ValueError("ERC721Metadata: base URI not set")

        return f"{self._base_uri}/{token_id}"
