# SPDX-License-Identifier: MIT
from typing import Dict
from web3 import Web3

class MyToken:

    _balances: Dict[str, int] = dict()
    _allowances: Dict[str, Dict[str, int]] = dict()
    _name: str = ""
    _symbol: str = ""
    _total_supply: int = 0

    def __init__(self, name: str, symbol: str, initial_supply: int, web3: Web3):
        self._name = name
        self._symbol = symbol
        self._total_supply = initial_supply
        self._balances[self.web3.eth.default_account] = self._total_supply
        self.web3 = web3

    def supports_interface(self, interface_id: bytes) -> bool:
        return interface_id == self.web3.sha3(text="IERC20").hex()

    def balance_of(self, account: str) -> int:
        return self._balances.get(account, 0)

    def transfer(self, recipient: str, amount: int) -> bool:
        sender = self.web3.eth.default_account
        if self.balance_of(sender) < amount:
            return False
        self._balances[sender] -= amount
        self._balances[recipient] += amount
        return True

    def allowance(self, owner: str, spender: str) -> int:
        return self._allowances.get(owner, dict()).get(spender, 0)

    def approve(self, spender: str, amount: int) -> bool:
        owner = self.web3.eth.default_account
        self._allowances[owner][spender] = amount
        return True

    def transfer_from(self, sender: str, recipient: str, amount: int) -> bool:
        owner = self.web3.eth.default_account
        if self.allowance(sender, owner) < amount or self.balance_of(sender) < amount:
            return False
        self._balances[sender] -= amount
        self._balances[recipient] += amount
        self._allowances[sender][owner] -= amount
        return True

    def total_supply(self) -> int:
        return self._total_supply
