"""
Name: FIT9136 - Teaching Team
Date: 7 April 2022
Description: This python script create Extended Contact class.
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
    def __init__(self, name, organisation, phones = [], email="", address = ""):
        super().__init__(name, organisation, phones)
        self.email = email
        self.address = address

    def __str__(self):
        formatted_str = super().__str__() + "\nEmail: "+ str(self.email)
        formatted_str += "\nAddress: " + str(self.address) + "\n"
        return formatted_str 

#test
econtact = ExtendedContact("Shirin", "Monash", ["0000000000"],"sh@monash.edu", "Clayton")
print(econtact)

