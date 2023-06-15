"""
Name: Huixin Wang
Date: 3rd Apr 2023
Description:
"""
class Contact:
    def __init__(self, name, organisation, phones = []):
        #write your answer here
        self.name = name
        self.organisation = organisation
        self.phones = phones

    def __str__(self):
        #write your answer here
        formatted_str = "Name: " + self.name+ " Organisation: " + self.organisation + '\nPhone Number/s: '
        for phone in self.phones: # sorted according to keys, e.g., 'phone1','phone2',....
            formatted_str += phone + '\n                ' 
        return formatted_str

class ExtendedContact(Contact):
    def __init__(self, name, organisation, phones =[], email="", address=""):
        super().__init__(name, organisation, phones)
        self.email = email
        self.address = address

    def __str__(self):
        formatted_str = super().__str__() + "\nemial: " + str(self.email)
        formatted_str += "\nAddress: " + str(self.address) + '\n'
        return formatted_str

#test
contact = ExtendedContact("Huixin", "Monash", ["000000000000"],"hwan0158@student.monash.edu", "3000")
print(contact)

