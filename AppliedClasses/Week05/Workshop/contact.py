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
    
#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Huixin Wang','Monash',['0451953737'])

print(c1.name)
print(c1.organisation)
print(c1.phone_num)
