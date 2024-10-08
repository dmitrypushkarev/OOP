"""Класс для консольного приложения “I-Bank” для хранения денежных вкладов и манипуляций с ними."""

class Account:
    def __init__(self, name: str, passport: str, phone: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone = phone
        self.__balance = start_balance # закрываем прямой доступ к балансу

    def full_info(self) -> str:
        return f'имя: {self.name}, паспорт: {self.passport}, телефон: {self.phone}'

    def __repr__(self):
        return f"{self.name}, баланс: {self.balance}"

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int):
        """Пополнение баланса"""
        self.__balance += amount

    def withdraw(self, amount: int):
        """Снятие средств"""
        if self.__balance >= amount:
            self.__balance -= amount + int(amount * bank1.commission / 100)
        else:
            raise ValueError("Недостаточно средств!")

    def transfer(self, target_account: 'Account', amount: int):
        """Перевод средств"""
        if self.__balance >= amount:
            self.__balance -= amount + int(amount * bank1.commission / 100)
            target_account.__balance += amount
        else:
            raise ValueError('Недостаточно средств!')

class Bank:
    def __init__(self, commission: int = 0):
        self.__commission = commission

    def add_commission(self, other: int):
        """Установка комиссии банка, только целые числа"""
        self.__commission += other

    @property
    def commission(self) -> int:
        return self.__commission


bank1 = Bank()
bank1.add_commission(4)
print(bank1.commission)
client1 = Account('Александр', "1234 173723", "+7-985-727-36-47", 500)
client2 = Account("Евгений", "2312 312323", "+7-916-212-42-09", 800)
print(client1, client2)
client1.transfer(client2, 200) 
print(client1, client2)

