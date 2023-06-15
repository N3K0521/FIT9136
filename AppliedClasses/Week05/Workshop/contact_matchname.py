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

    def match_name(self, substr):
        if self.name.lower().startswith(substr.lower()):
            return True
        else:
            return False

#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Huixin Wang','Monash',['0451953737'])

print("\ntesting match_name method\n")
# testing match_name method
print(c1.match_name('huixin'))



