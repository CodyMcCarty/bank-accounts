# account.py
import csv
# from owner import Owner

class Account():
    
    def __init__(self, account_id, initial_balance, open_date):
        if initial_balance < 0:
            raise Exception ("Must enter a positive balance")
        self.account_id = account_id
        self.current_balance = initial_balance
        self.open_date = open_date

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

    def all_accounts(self):
        print(f"Number of accouts: {len(accounts)}")
        for account in accounts:
            print(account.account_id, account.current_balance, account.open_date)

    def find(self, id):
        for account in accounts:
            if int(account.account_id) == id:
                print(account.account_id, account.current_balance, account.open_date)


accounts = []
with open('support/accounts.csv') as csv_file_accounts:
    csv_reader_accounts = csv.reader(csv_file_accounts)

    next(csv_reader_accounts)

    for line in csv_reader_accounts:
        accounts.append(Account(line[0], int(line[1]), line[2]))


accounts[0].find(1216)














# ca = Account(7080, 500)
# ca.show_balance()
# ca.withdraw(200)
# ca.deposit(3500)
