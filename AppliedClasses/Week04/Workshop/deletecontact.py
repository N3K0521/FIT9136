"""
Name: Huixin Wang
Date: 24th March 2023
Description:This fucntion asks user for ID and then delete details of the contact
associated with it and returns the updated dictionary
"""

def delete_contact(contact_dict = {}):
    id = input("Enter the ID: ")
    while not id.isdigit():
        print("Invalid input.")
        id = input("Enter the ID: ")
    
    #check if the id is in the dictionary
    if int(id) in contact_dict.keys():
        del contact_dict[int(id)]
    else:
        print("ID not found.")
    return contact_dict
    
#Test valid input
contact_dict = {11111: ["Deep", "Melbourne", "Monash", ["0412345678", "0498754321"]]}
contact_dict = delete_contact(contact_dict) 
print(contact_dict)
