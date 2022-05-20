# owner.py

import csv

class Owner():

    def __init__(self, owner_id, last_name, first_name, street_address, city, state, owner = None):
        self.owner_id = owner_id
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state 
        self.owner = owner

owners = []                
with open('support/owners.csv', 'r') as csv_file_owners:
    csv_reader_owners = csv.reader(csv_file_owners)

    next(csv_reader_owners)

    for line in csv_reader_owners:
        owners.append(Owner(line[0], line[1], line[2], line[3], line[4], line[5]))

for owner in owners:
    print(owner.last_name)




    










