# account.py

class Account():
    
    def __init__(self, account_id, initial_balance):
        if initial_balance < 0:
            raise Exception ("Must enter a positive balance")
        self.account_id = account_id
        self.current_balance = initial_balance

    def show_balance(self):
        print(self.current_balance)

    def deposit(self, ammount):
        self.current_balance += ammount
        self.show_balance()

    def withdraw(self, ammount):
        future_ammount = self.current_balance - ammount
        if future_ammount < 0:
            raise Exception (f"Insufenciant funds.\n Your current balance is $ {self.current_balance}, and you can't withdraw $ {ammount}  " )
        self.current_balance = future_ammount
        self.show_balance()



ca = Account(7080, 500)
ca.show_balance()
ca.withdraw(200)
ca.deposit(3500)
