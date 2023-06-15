"""
Name: Huixin Wang
Date: 21 Mar 2023
Description:
"""

class Contact:
    def __init__(self, name, organisation, phones=[]):
        self.name = name
        self.organisation = organisation
        self.phones = phones

    def update_name(self, name):
        self.name = name
    
    def update_org(self, organisation):
        self.organisation = organisation
    
    def add_phone(self, phone):
        if phone in self.phones:
            print("Phone number already exists")
        else:
            self.phones.append(phone)

    def match_name(self, substr):
        if self.name.lower().startswith(substr.lower()):
            return True
        else:
            return False

    def remove_phone(self, index):
        if index in range(0, len(self.phones)):
            del self.phones[index]
            return True
        else:
            print("Invalid index")
            return False

    def update_phone(self, index, new_phone):
        if index in range(0, len(self.phones)):
            self.phones[index] = new_phone
            return True
        else:
            print("Invalid index")
            return False

    def __str__(self):
        formatted_str = "Name: " + self.name + "\nOrganisation: " + self.organisation + '\nPhone number/s: '
        for phone in self.phones:
            formatted_str += phone + '\n'
        return formatted_str

    def __eq__(self, other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        organisation_self = self.organisation.lower()
        organisation_other = other.organisation.lower()
        if name_self == name_other and organisation_self == organisation_other:
            return True
        else:
            return False

    def __lt__(self, other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        organisation_self = self.organisation.lower()
        organisation_other = other.organisation.lower()
        if name_self < name_other:
            return True
        elif name_self == name_other:
            if organisation_self < organisation_other:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        organisation_self = self.organisation.lower()
        organisation_other = other.organisation.lower()
        if name_self > name_other:
            return True
        elif name_self == name_other:
            if organisation_self > organisation_other:
                return True
            else:
                return False
        else:
            return False

print("Creating 2 instances")
c1 = Contact('Huixin', 'Monash', ['0451953737', '1234567'])
c2 = Contact('Lee', 'Monash', ['123958723'])

print("\nupdate_name method:")
c1.update_name('Rebecca')
print(c1)

print("\nmatch_name method:")
print(c1.match_name("Hui"))

print("\nadd_phone method:")
c1.add_phone("12349873290345807")
print(c1)

    
