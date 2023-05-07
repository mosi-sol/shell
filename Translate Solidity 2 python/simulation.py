class Contract:
    def __init__(self, balance):
        self.balance = balance
        self.total_supply = 0
        self.accounts = {}

    def mint(self, amount):
        self.total_supply += amount
        self.balance += amount

    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            return False
        if self.accounts[sender] < amount:
            return False
        self.accounts[sender] -= amount
        self.accounts[receiver] += amount
        return True

    def balanceOf(self, account):
        if account not in self.accounts:
            return 0
        return self.accounts[account]

    def addAccount(self, account, balance):
        self.accounts[account] = balance
        self.balance += balance

    def removeAccount(self, account):
        if account not in self.accounts:
            return False
        self.balance -= self.accounts[account]
        del self.accounts[account]
        return True
