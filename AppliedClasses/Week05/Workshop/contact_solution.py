"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script create a __init__() of Contact class.
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
    
    Methods
    -------
    __init__()
        Constructor method
    """
    # Constructor Method
    def __init__(self, name, organisation, phones = []):
        self.name = name
        self.organisation = organisation
        self.phones = phones

#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Shirin','Monash',['0425685212','0464545464'])
c2 = Contact('Lily','Monash',['0425685212'])

print(c1.name)
print(c1.organisation)
print(c1.phones)

print(c2.name)
print(c2.organisation)
print(c2.phones)
