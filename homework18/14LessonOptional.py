class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return (
            f'Account number: {self._account_number},'
            f'balance: {self._balance}'
        )


class SavingsAccount(Account):
    def __init__(self, balance, account_number, intererst_rate):
        super().__init__(balance, account_number)
        self.intererst_rate = intererst_rate

    def add_interest(self):
        interest = self._balance * (self.intererst_rate / 100)
        self._balance += interest


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def send_letter(self):
        if self._balance < 0 and abs(self._balance) > self.overdraft_limit:
            return 'Where is my money, Lebovsky?'
        return ''


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        self.accounts = [acc for acc in self.accounts
                         if acc.get_account_number() != account_number]

    def pay_dividend(self, dividend):
        for account in self.accounts:
            account.deposit(dividend)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_letter()


Saving = SavingsAccount(0, 'N001', intererst_rate=12)
Curr = CurrentAccount(0, 'N002', overdraft_limit=2000)

bank = Bank()

bank.open_account(Saving)
bank.open_account(Curr)
Saving.deposit(10000)
Curr.withdraw(3000)

print('Виводимо стан рахунків')
print(Saving)
print(Curr)
print('Проводимо апдейт по рахункам')
bank.update()
print('Виводимо стан рахунків')
print(Saving)
print(Curr)
