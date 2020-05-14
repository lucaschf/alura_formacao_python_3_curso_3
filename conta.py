class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print("Balance of {} of holder {}".format(self.__balance, self.__holder))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance -= value
        else:
            print("No sufficient founds")

    def __can_withdraw(self, value):
        available_value = self.limit + self.balance
        return available_value >= value

    def transfer(self, value, target):
        self.withdraw(value)
        target.deposit(value)

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def banks():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
