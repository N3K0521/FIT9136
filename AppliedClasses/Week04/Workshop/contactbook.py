"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script does the contact operations like add,
delete, and view.
"""

# Import library
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
    unique_num = random.randint(10000, 100000)
    # Checking the randomly generated ID is in contact_dict
    while unique_num in contact_dict.keys():
        # if exists, then create new ID
        unique_num = random.randint(10000, 100000)
        
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
    

def delete_contact(contact_dict):
    """
    Deletes contact deatils 
    
    This function asks user for ID and then deletes details
    of the contact associated with it and returns the updated dictionary

    Parameters
    ----------
    contact_dict : dict
        Dictionary containing contact details
    
    Returns
    -------
    dict
        Dictionary updated after deleting contact details
        
    Examples
    --------
    >>> delete_contact(contact_dict = {})
    Empty Contact book
    
    >>> contact_dict = {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]],
    2222222: ["Jerry", "Carnegie", "Youtube", ["0412345879"]]}
    >>> delete_contact(contact_dict)
    Enter the ID: 111111
    {2222222: ["Jerry", "Carnegie", "Youtube", ["0412345879"]]}
    """
    # Checks for the empty dictionary
    if len(contact_dict) == 0:
        print("Empty Contact book")
    else:
        # Show the contact details to the users
        view_contacts(contact_dict)
        # Asks user to enter ID
        user_input = input("Enter the ID:")
        # checking Id for digits only
        while not user_input.isdigit():
            # Until a digit is entered, asking the user to enter again.
            print("ID contains alphabets. Try again")
            user_input = input("Enter the ID:")
        
        # Checking ID in the contact_dict
        if int(user_input) in contact_dict.keys():
            # using del to delete
            del contact_dict[int(user_input)]
        else:
            print("ID is invaild.\n")
    return contact_dict
        

def view_contacts(contact_dict):
    """
    Views Contact details
    
    This function shows the details of the contact 
    in the contact dictionary.

    Parameters
    ----------
    contact_dict : dict
        Dictionary containing contact details
    
    Returns
    -------
    None
    
        
    Examples
    --------
    >>> view_contacts(contact_dict = {})
    Empty Contact book
    
    >>> contact_dict = {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]],
    2222222: ["Jerry", "Carnegie", "Youtube", ["0412345879"]]}
    >>> view_contacts(contact_dict)
    ID: 111111
    Name: Tom    Organization: Monash
    Address: Melbourne    Phone Numbers: ['0412345678', '0498765432']

    ID: 2222222
    Name: Jerry  Organization: Youtube
    Address: Carnegie    Phone Numbers: ['0412345879']
    """
    # Checks for the empty dictionary
    if len(contact_dict) == 0:
        print("Empty Contact book.\n")
    else:
        # Iterating through dictionary items
        for k, v in contact_dict.items():
            # printing the details
            print("ID:", k)
            print(f"Name: {v[0]}\tOrganization: {v[2]}")
            print(f"Address: {v[1]}\tPhone Numbers: {v[3]}\n")
    
    return None
        


## Main Program Starts

def main():
    """
    Main function of the contact book.
    
    This function shows the menu and performs the operation 
    based on the selection from the menu 
    on the contact book dictionary.

    Parameters
    ----------
    None
    
    Returns
    -------
    None

    """
    print("----------------Welcome to the Contact Book----------------")
    contact_dict = {11111: ["Deep", "Melbourne", "Monash", ["0412345678", "0498754321"]]}
    # using while loop to print out the interface continously till user chooses to quit.
    while True:
        print("Enter the number on left side for the operation")
        print("1....Add Contact")
        print("2....Delete Contact")
        print("3....View Contacts")
        print("4....Exit")

        # Asking user to enter a choice
        choice = input("Enter your choice:")

        # Performing user validation by using string methods
        while not choice.isdigit():
            # Until a digit is entered, asking the user to enter again.
            print("You have enter invalid choice. Try again")
            choice = input("Enter your choice:")

        # Converting the Choice into integer
        choice = int(choice)

        # checking the choice and calling the function based on the options
        if choice == 1:
            contact_dict = add_contact(contact_dict)
        elif choice == 2:
            contact_dict = delete_contact(contact_dict)
        elif choice == 3:
            view_contacts(contact_dict)
        elif choice == 4:
            print("Exiting the program")
            break
        else:
            print("You have enter invalid choice.")
            
if __name__ == "__main__":
    main()
