

class House:

    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, sale):
        return self._price - sale


class SmallHouse(House):

    def __init__(self, _price):
        self._area = 42
        self._price = _price


class Client:

    default_name = 'Nik'
    default_age = 21
    def __init__(self, bank, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._account = bank.add_account(self)
        self._house = None

    def info(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}\nДом: {self._house}\n')

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nДом: {self._house}\n'

    @staticmethod
    def default_info():
        default_name = 'Nik'
        default_age = 21
        print(f'Имя: {default_name}\nВозраст: {default_age}\n')

    def _make_deal(self, house: House, price):
        self._account -= price
        self._house = house

    def earn_money(self, money: int):
        self._account += money

    def buy_house(self, house: House, sale):
        try:
            self._make_deal(house, house.final_price(sale))
        except:
            print('Недостатончо денег для покупки')


class Account:
    default_amount = 0

    def __init__(self, client: Client, amount: int=default_amount) -> None:
        self.client = client
        self.amount = amount


    def __str__(self) -> str:
        return f'Пользователь: {self.client}\nСчет: {self.amount}\n'

    def __iadd__(self, other: int):
        self.amount += other
        return self

    def __isub__(self, other: int):
        if self.amount - other <= 0:
            self.amount = 0
            return self

        self.amount -= other
        return self

class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, client: Client) -> Account:
        if client not in self.accounts:
            self.accounts.append(client)
            return Account(client)
        else:
            raise

    def __str__(self):
        return f'{self.accounts}\n'







