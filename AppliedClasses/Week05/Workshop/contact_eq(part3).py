"""
Name: Huixin Wang
Date: 31st Mar 2023
Description:
"""

class Contact:
    def __init__(self, name, organisation, phone_num = []):
        self.name = name
        self.organisation = organisation
        self.phone_num = phone_num
    
    def __eq__(self,other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        if name_self == name_other and org_self == org_other:
            return True
        else:
            return False

#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Huixin','Monash',['0451953737'])
c2 = Contact('Lee','Monash',['1234567'])

print("\ntesting __eq__method\n")
print('c1 == c2?',c1 == c2)


