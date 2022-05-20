import csv

account_owners = []    
with open("support/account_owners.csv") as csv_file_account_owners:
    csv_reader_account_owners = csv.reader(csv_file_account_owners)

    for line in csv_file_account_owners:
        account_owners.append(line)


for line in account_owners:
    print(line)