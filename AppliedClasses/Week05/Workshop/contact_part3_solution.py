"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script create a __eq__() of Contact class.
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
    other: object
        a object of the class contact
    

    Methods
    -------
    __init__()
        Constructor method

    __eq__()
        use to specific whether two contacts are equal.
    """
    # Constructor Method
    def __init__(self, name, organisation, phones = []):
        self.name = name
        self.organisation = organisation
        self.phones = phones

    def __eq__(self, other):
        # lower-casing name and organisation for both object
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        # comparing the variables
        if name_self == name_other and org_self == org_other:
            return True
        else:
            return False

#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Shirin','Monash',['0425685212','0464545464'])
c2 = Contact('Lily','Monash',['0425685212'])

print("\ntesting __eq__method\n")
print('c1 == c2?',c1 == c2)
