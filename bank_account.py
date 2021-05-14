class BankAccount:
    balance = 0

    def deposit(self, money):
        self.balance += money
        return f'Вы пополнили баланс на {money} сом\nВаш баланс: {self.balance}'

    def withdraw(self, money):
        if self.balance > money:
            self.balance -= money
            return f'Вы сняли со счета {money} сом\nВаш баланс: {self.balance}'
        else:
            return f'У вас недостаточно средств на счету'


class MinimumBalanceAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.min_balance = 100

    def withdraw(self, money):
        if self.balance - money > self.min_balance:
            return super().withdraw(money)
        else:
            return f'У вас недостаточно средств на счету'


# b = BankAccount()
# print(b.deposit(15000))
# print(b.withdraw(10000))
# print(b.withdraw(10000))
m = MinimumBalanceAccount()
print(m.deposit(1000))
print(m.withdraw(50))
print(m.withdraw(1100))
