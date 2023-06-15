"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script does the Add contact operation.
"""

import random

def add_contact(contact_dict = {}):
    """
    Asks user to enter the contact details and 
    return the updated dictionary
    
    This function addes new user to the contact dictionary
    by asking user name, organization, address, phone numbers,
    and assign randomly generated unique ID.

    Parameters
    ----------
    contact_dict : dict
        Dictionary containing contact details
    
    Returns
    -------
    dict
        Dictionary containing added contact details
        
    Examples
    --------
    >>> add_contact(contact_dict = {})
    {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]]}
    >>> add_contact(contact_dict = {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]]})
    {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]],
    2222222: ["Jerry", "Carnegie", "Youtube", ["0412345879"]]}
    """
    # Randomly generating the ID
    unique_num = random.randint(10000, 99999)
    # Checking the randomly generated ID is in contact_dict
    while unique_num in contact_dict.keys():
        # if exists, then create new ID
        unique_num = random.randint(10000, 99999)
        
    # Asking user Name, organization, and address
    name = input("Name: ")
    organization = input("Organization: ")
    address = input("Address: ")

    phone_nums = []
    # Asking user to enter the as many as phone numbers 
    while True:
        phone_num = input("Phone Number:")
        check = input("Do you want to add more numbers? (Y or N)")
        # checking user input
        if check in "Nn":
            phone_nums.append(phone_num)
            # using break the infinite loop
            break
        elif check in "Yy":
            phone_nums.append(phone_num)
        else:
            print("Wrong Choice. Phone Number Not added")
        
    # updating the contact_dict
    contact_dict.update({unique_num: [name, address, organization, phone_nums]})
    return contact_dict

#Test valid input
contact_dict = {11111: ["Deep", "Melbourne", "Monash", ["0412345678", "0498754321"]]}
contact_dict = add_contact(contact_dict) 
print(contact_dict)

