import json


class Account(dict):

    def __init__(self, __dict: dict):
        self.__dict__ = __dict

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def tuple_values(self):
        return tuple(self.__dict__.values())

    def show_data(self):
        print("""Name : {}
Account number : {}
Money : {}
History : {}""".format(*self.tuple_values()))

    def show_money(self):
        print(f"Current money : {self.__dict__['money']}")

    def update_history(self, text: str):
        self.__dict__['history'] = (self.__dict__['history']
                                    +
                                    f'\n{text.strip()}\n').strip()

    def deposit(self):
        _amount = int(input('Amount : '))
        self.__dict__['money'] += _amount
        self.show_money()

        self.update_history(f"Deposit : {_amount}")

    def withdraw(self):
        _amount = int(input('amount : '))
        self.__dict__['money'] -= _amount
        self.show_money()

        self.update_history(f"Withdraw : {_amount}")

    def show_history(self):
        print(self.__dict__['history'])


def main():

    with open(input('Filename : ')) as file:
        classes = [Account(_dict) for _dict in json.load(file)]

    accn=input("Account number : ")
    while True:
        for acc in classes:
            if acc['account number'] == accn:
                while True:
                    m=int(input("Menu : "))
                    if m == 0:return
                    elif m == 1:acc.show_data()
                    elif m == 2:acc.deposit()
                    elif m == 3:acc.withdraw()
                    elif m == 4:acc.show_history()
                    elif m == 5:
                        accn=input("Account number : ")
                        break


main()
