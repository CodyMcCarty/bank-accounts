# account.py

class Account():
    
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.current_balance = initial_balance

    def show_balance(self):
        print(self.current_balance)

    def deposit(self, ammount):
        self.current_balance += ammount
        self.show_balance()

    def withdraw(self, ammount):
        self.current_balance -= ammount
        self.show_balance()



ca = Account(7080, 500)
ca.show_balance()
