"""
Name: Huixin Wang
Date: 24th March 2023
Description:This function shows the details of the contact in the contact dictionary
"""

def view_contacts(contact_dict):
    for i, j in contact_dict.items():
        print("ID:", i)
        print(f"Name: {j[0]}\nOrganisation: {j[2]}")
        print(f"Address: {j[1]}\nPhone Numbers: {j[3]}")
    return None

#Test valid input
contact_dict = {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]],
    2222222: ["Jerry", "Carnegie", "Youtube", ["0412345879"]]}
view_contacts(contact_dict)
