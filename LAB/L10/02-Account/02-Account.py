import json


class Account:
    def __init__(self, *args):
        self.name, self.account_number, self.money, self.history = args

    def show_data(self):
        print(f"""Name : {self.name}
Account number : {self.account_number}
Money : {self.money}
History : {self.history}""")

    def deposit(self):
        _amt =int(input("Amount : "))
        self.money+=_amt 
        
        print(f"Current money : {self.money}")
        
        if self.history == "": 
            self.history = f"Deposit : {_amt }"
        else: 
            self.history+=f"\nDeposit : {_amt }"

    def withdraw(self):
        _amt=int(input("amount : "))
        self.money-=_amt
        
        print(f"Current money : {self.money}")
        
        if self.history == "": 
            self.history = f"Withdraw : {_amt}"
        else: 
            self.history+=f"\nWithdraw : {_amt}"

    def show_history(self):
        print(self.history)
        
with open(input("Filename : ")) as f:
    classes = [Account(*item.values()) for item in json.load(f)]

def main():
    acc_no=input("Account number : ")
    while True:
        for acc in classes:
            if acc.account_number == acc_no:
                while True:
                    menu=int(input("Menu : "))
                    if menu == 0:
                        return
                    elif menu == 1: 
                        acc.show_data()
                    elif menu == 2: 
                        acc.deposit()
                    elif menu == 3: 
                        acc.withdraw()
                    elif menu == 4: 
                        acc.show_history()
                    elif menu == 5:
                        acc_no=input("Account number : ")
                        break

main()
