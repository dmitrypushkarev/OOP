"""Класс для консольного приложения “I-Bank” для хранения денежных вкладов и манипуляций с ними."""

class Account:
    def __init__(self, name: str, passport: str, phone: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone = phone
        self.balance = start_balance

    def full_info(self) -> str:
        return f'имя: {self.name}, \nпаспорт: {self.passport}, \nтелефон: {self.phone}'

    def __repr__(self):
        return 0


client1 = Account('Уууася', "1234 173723", "+7-985-727-36-47")

print(client1.full_info())