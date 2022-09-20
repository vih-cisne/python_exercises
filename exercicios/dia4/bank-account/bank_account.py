class BankAccount:
    def __init__(self):
        self.opened = False
        self.__balance = 0

    def get_balance(self):
        self.is_opened()

        return self.__balance

    def open(self):
        self.is_already_opened()

        self.opened = True

    def is_amount_negative(self, amount):
        if amount < 0:
            raise ValueError("amount must be greater than 0")

    def deposit(self, amount):
        self.is_opened()
        self.is_amount_negative(amount)

        self.__balance += amount

    def withdraw(self, amount):
        self.is_opened()
        self.is_amount_negative(amount)

        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("amount must be less than balance")

    def is_already_opened(self):
        if self.opened:
            raise ValueError("account already open")

    def is_opened(self):
        if not self.opened:
            raise ValueError("account not open")

    def close(self):
        self.is_opened()

        #reopened account doesn´'t retain balance?

        self.__balance = 0
        self.opened = False

