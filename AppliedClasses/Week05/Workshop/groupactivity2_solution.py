"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script create a __init__() and match_name() of Contact class.
"""

class Contact:
    """
    A class to store the Contact details of the person 
    
    Attributes
    ----------
    name: str
        a string to store name of the contact person
    organisation: str
        a string to store organisation of the contact person
    phones: list
        a list to store mobile number of the user
    substr: str
        a string to store sub string that is to be found from the contact

    Methods
    -------
    __init__()
        Constructor method
        
    match_name()
        a method accepts a string as an argument, and return True if the string was a prefix of the name of the person, or False if it is not.
    """
    # Constructor Method
    def __init__(self, name, organisation, phones = []):
        self.name = name
        self.organisation = organisation
        self.phones = phones
        
    # match name method
    def match_name(self, substr):
        # Checking name if it startswith
        if self.name.lower().startswith(substr.lower()):
            return True
        else:
            return False

#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Shirin','Monash',['0425685212','0464545464'])
c2 = Contact('Lily','Monash',['0425685212'])

print("\ntesting match_name method\n")
# testing match_name method
print(c1.match_name('shi'))
print(c1.match_name('li'))
