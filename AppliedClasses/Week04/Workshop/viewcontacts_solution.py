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

#Test valid input
contact_dict = {111111: ["Tom", "Melbourne", "Monash", ["0412345678", "0498765432"]],
    2222222: ["Jerry", "Carnegie", "Youtube", ["0412345879"]]}
view_contacts(contact_dict)
