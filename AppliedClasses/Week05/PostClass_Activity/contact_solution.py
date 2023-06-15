"""
Name: FIT9136 - Teaching Team
Date: 21th Feb 2022
Description: This python script create a Contact class.
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
    index: int
        a integer to store the index value to enter new phone number
    new_phone: str
        a string to store mobile number of the user
    substr: str
        a string to store sub string that is to be found from the contact
    other: object
        a object of the class contact
    

    Methods
    -------
    update_name()
        a method to update the name of the person
    match_name()
        a method accepts a string as an argument, and return True if the string was a prefix of the name of the person, or False if it is not.
    update_organisation()
        a method to update the organisation of the person
    add_phone()
        a method to add a phone number
    remove_phone()
        a method to remove the phone number on the position of index.
    update_phone()
        a method to update the phone number on index to new_phone.
    """
    # Constructor Method
    def __init__(self, name, organisation, phones = []):
        self.name = name
        self.organisation = organisation
        self.phones = phones
        
    # update name method
    def update_name(self, name):
        self.name = name
        
    # update name method
    def update_organisation(self,organisation):
        self.organisation =  organisation
        
    # match name method
    def match_name(self, substr):
        # Checking name if it startswith
        if self.name.lower().startswith(substr.lower()):
            return True
        else:
            return False
    
    # add phone method
    def add_phone(self,phone):
        # checking phone number in existing list
        if phone in self.phones:
            print("Phone number already exists!")
        else:
            # if not then added it
            self.phones.append(phone)
    
    # remove method
    def remove_phone(self, index):
        # finding the index in the phone list
        if index in range(0,len(self.phones)):
            # if exists then delete
            del self.phones[index]
            return True
        else:
            print("Index out of range")
            return False
        
    # update phone method
    def update_phone(self, index, new_phone):
        # checking index in the phone list
        if index in range(0,len(self.phones)):
            # if it exists then replace with new phone number
            self.phones[index] = new_phone
            return True
        else:
            print("Index out of range")
            return False
     
    #__str__(self): This is  the overloaded method that is useful for formatting the output of the contact represented in this Contact class.
    def __str__(self):
        formatted_str = "Name: " + self.name+ " Organisation: " + self.organisation + '\nPhone Number/s: '
        for phone in self.phones: # sorted according to keys, e.g., 'phone1','phone2',....
            formatted_str += phone + '\n                ' 
        return formatted_str
      
      
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
      
    def __lt__(self, other):
        # lower-casing name and organisation for both object
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        # comparing the variables
        if name_self < name_other:
            return True
        elif name_self == name_other:
            if org_self < org_other:
                return True
            else:
                return False
        else:
            return False
        
    def __gt__(self, other):
        # lower-casing name and organisation for both object
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        # comparing the variables
        if name_self > name_other:
            return True
        elif name_self == name_other:
            if org_self > org_other:
                return True
            else:
                return False
        else:
            return False
#Test
print("Creating two instances")
# creating two instances
c1 = Contact('Shirin','Monash',['0425685212','0464545464'])
c2 = Contact('Lily','Monash',['0425685212'])


print("\ntesting update_name method\n")
# testing update_name method
c1.update_name('shirin')
# print method utilise __str__ method
print(c1)


print("\ntesting update_organisation method\n")
# testing update_organisation method
c1.update_organisation('Melbourne')
print(c1)

print("\ntesting match_name method\n")
# testing match_name method
print(c1.match_name('shi'))
print(c1.match_name('li'))

print("\ntesting add_phone method\n")
# testing add_phone method
c1.add_phone('0433586891')
print(c1)

print("\ntesting update_phone method\n")
# testing update_phone method
c1.update_phone(1,'0464545465')
print(c1)

print("\ntesting __eq__, __lt__, __gt__ method\n")
# testing __eq__, __lt__, __gt__ method
print(c1)
print(c2)
print('c1 == c2?',c1 == c2)
print('c1 > c2?',c1 > c2)
print('c1 < c2?',c1 < c2)


print("\nTesting __str__ method\n")
# create a list of contact 
contact_list = [c1,c2]
# printing out the contacts one by one, based on the current order
for c in contact_list:
    print(c)
    
    
print("\nTesting index method\n")
# we can also use the index method, because we overloaded __eq__
contact_list.index(Contact('shirin','Melbourne'))
