"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script does the add contact operation
"""

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
        print(contact_dict)
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

#Test valid input
contact_dict = {11111: ["Deep", "Melbourne", "Monash", ["0412345678", "0498754321"]]}
contact_dict = delete_contact(contact_dict) 
print(contact_dict)
