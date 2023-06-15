"""
Name: Huixin Wang
Date: 24th Mar 2023
Description:This function adds a new user to the
contact dictionary by asking user name, organisation,
address, phone numbers, and assign a randomly
generated unique ID.
"""

import random

def add_contact(contact_dict = {}):
#assign a randomly generated unique ID
    unique_id = random.randint(10000, 99999)
    #check if the id is in the dictionary
    while unique_id in contact_dict.keys():
        #generate a new ID if exists
        unique_id = random.randint(10000, 99999)

    #asking user name, organisation, address
    name = input("Name: ")
    organisation = input("Organisation: ")
    address = input("Address: ")

    #asking phone numbers (one contact may have multiple numbers)
    phone_nums = []

    while True:
        phone_num = input("Phone number: ")
        check = input("Another number to add? (Y/N)")
        if check in "Nn":
            phone_nums.append(phone_num)
            break
        elif check in "Yy":
            phone_nums.append(phone_num)
        else:
            print("Invalid input.")

    # update the contact_dict
    contact_dict.update({unique_id:[name, address, organisation, phone_nums]})
    return contact_dict

#Test valid input
contact_dict = {11111: ["Deep", "Melbourne", "Monash", ["0412345678", "0498754321"]]}
contact_dict = add_contact(contact_dict) 
print(contact_dict)
