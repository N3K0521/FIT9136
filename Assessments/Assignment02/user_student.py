"""
Creation Date: 19th April 2023
Last Modified Date: 09th May 2023

Group number: App03-Group41

Group number 1:
    Name: Huixin Wang
    Student ID: 31552544

Group number 2:
    Name:Enze Dong
    Student ID:33038937

Group number 3:
    Name:Nikita Bhararia
    Student ID:32708246
"""

import random
from user import User
from unit import Unit

class UserStudent(User):
    """
    A class used to store the Student details

    Attributes
    ----------
    user_id : int
        an integer to store the user id
    user_name : str
        a string to store the user's name
    user_password : str
        a string to store the user's password
    user_role : str
        a string to store the user's role
    user_status : str
        a string to store the user's status

    Methods
    -------
    student_menu():
        Display a list of all operations that can only be performed by a student
    list_available_units():
        Display all the units that can be enrolled by the current student.
    list_enrolled_units()
        Display all the units that the student enrolled.
    enrol_unit(unit_code):
        Enrol the current student into a unit. One student can enrol a
        maximum of 3 units and each unit has its own capacity. After
        enrollment, initialise the score as -1.
    drop_unit(unit_code):
        Remove the unit from the list of units in which the student is
        currently enrolled
    check_score(unit_code):
        Display the unit score
    generate_score(unit_code):
        Generate a random score for a unit
    """
    # constructor
    def __init__(self, user_id, user_name, user_password, user_role='ST', user_status='enabled', enrolled_units=None):
        """
        :param user_id: int
            The id of the student (default is None)
            Must be unique integer
        :param user_name: str
            The name of the student (default is None)
            Must be unique and can only consist of numbers,
                letters, underscores
        :param user_password: str
            The password of the user (default is None)
            Must be encrypted
        :param user_role: str
            The role of the user (default is 'ST')
        :param user_status: str
            The stored user status of the user (default is "enabled")
        :param enrolled_units: list of tuples (unit_code, score)
            The stored enrolled_units (default score is -1)
        """
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        if enrolled_units == None:
            self.enrolled_units = []
        else:
            self.enrolled_units = enrolled_units

    # string function
    def __str__(self):
        """
        :return: A formatted string containing account details
        """
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}, {self.enrolled_units}"

    # function to display the student menu
    def student_menu(self):
        """
        Display the student menu
        """
        print('-' * 50)
        print("Please select from the menu:")
        print("1. List available units information")
        print("2. List enrolled units")
        print("3. Enrol in a unit")
        print("4. Drop a unit")
        print("5. Check the score of a unit")
        print("6. Generate score")
        print("7. Logout")

    # function to display the list of available units
    def list_available_units(self):
        """
        List all the available units to enrol
        :param: None
        :return: None
        """
        # Nikita's attempt
        # print("Unit Code - Unit Name:")
        # with open('data/unit.txt') as units:
        #     for unit in units:
        #         unit_data = unit.strip().split(',')
        #         if (int(unit_data[3]) > 0):
        #             print(unit_data[1] + " - " + unit_data[2])

        # Huixin - 07/05/2023 - In order to integrate with the application runs in main.py
        units = []
        with open('data/unit.txt') as f:
            for line in f.readlines():
                words = line.strip().split(', ')
                units.append(Unit(int(words[0]), words[1], words[2], int(words[3])))
        unit_codes = [unit.unit_code for unit in units]
        selected_nums = [0] * len(unit_codes)
        with open('data/user.txt') as f:
            for line in f.readlines():
                if line.split(', ')[3] == 'ST':
                    words = line.strip().split(', ')
                    student = UserStudent(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:])))
                    for enrolled_unit in student.enrolled_units:
                        selected_nums[unit_codes.index(enrolled_unit[0])] += 1
        for i in range(len(units)):
            if selected_nums[i] < units[i].unit_capacity:
                print(units[i])

    # function to display the list of enrolled units
    def list_enrolled_units(self):
        """
        list all the units that student enrolled
        :return: None
        """
        if not self.enrolled_units:
            print("You are not enrolled in any units")
        else:
            print("Enrolled units below:")
            for enrolled_unit in self.enrolled_units:
                print(enrolled_unit)

    # function to enrol the user with a unit
    def enrol_unit(self, unit_code):
        """
        Enrol the student to a unit. The maximum units can be enrolled
        by each student is 3, each unit has its own capacity
        :param unit_code: str
            The unit code of the unit (e.g. FIT9136)
        :return: None
        """
        # Nikita's attempt
        # # validating the user is already enrolled with 3 units
        # if len(self.enrolled_units) >= 3:
        #     print("You have already enrolled in the maximum number of units (3)")
        # # reading the unit is available to enrol
        # is_code_found = False
        # with open('data/unit.txt') as units_file:
        #     for unit in units_file:
        #         unit_data = unit.strip().split(',')
        #         if unit_data[1].lower() == unit_code.lower():
        #             current_unit = Unit(
        #                 unit_data[0], unit_data[1], unit_data[2], unit_data[3])
        #             is_code_found = True
        #
        # # output error message when the unit code is not found
        # if not is_code_found:
        #     print("Unit code is invalid")
        #     return
        # else:
        #     # enrolling the student
        #     unit_data = current_unit.unit_code
        #     if int(current_unit.unit_capacity) <= 0:
        #         print("Can't Enrol. This unit is already full")
        #     else:
        #         self.enrolled_units.append((unit_code, -1))
        #         print(f"Successfully enrolled in the {unit_code}!")
        #         units_list = []
        #         with open('data/unit.txt') as units_file:
        #             for unit in units_file:
        #                 unit_data = unit.strip().split(',')
        #                 if unit_data[1].lower() == unit_code.lower():
        #                     current_unit = unit_data[0] + "," + unit_data[1] + \
        #                                    "," + unit_data[2] + "," + \
        #                                    str(int(unit_data[3]) - 1)
        #                     units_list.append(current_unit)
        #
        #                 else:
        #                     units_list.append(unit.strip())
        #     # updating the unit.txt file after enroll by reducing the capacity by 1
        #     file = open("data/unit.txt", "w")
        #     for user in units_list:
        #         file.write(user + "\n")
        #     file.close()
        #
        #     # updating the user.txt file regarding the newly enrolled unit
        #     all_user_data = []
        #     with open('data/user.txt') as user_file:
        #         for user_data in user_file:
        #             current_user_data = user_data.strip()
        #             values = current_user_data.split(',')
        #             if (values[5] != None) and values[1] == self.user_name:
        #                 line = values[0] + "," + values[1] + "," + \
        #                        values[2] + "," + values[3] + \
        #                        "," + values[4] + ","
        #                 enrol_string = ""
        #                 for x, y in self.enrolled_units:
        #                     if enrol_string != "":
        #                         enrol_string += "_"
        #                     enrol_string += str(x) + "-" + str(y)
        #                 line += enrol_string
        #                 all_user_data.append(line)
        #         else:
        #             all_user_data.append(user_data.strip())
        #
        #
        # file = open("data/user.txt", "w")
        # for user in all_user_data:
        #     file.write(user + "\n")
        # file.close()

        # Huixin - 07/05/2023 - In order to integrate with the application runs in main.py
        if len(self.enrolled_units) >= 3:
            print("You have already enrolled in the maximum number of units (3)")
            return
        units = []
        with open('data/unit.txt') as f:
            for line in f.readlines():
                words = line.strip().split(', ')
                units.append(Unit(int(words[0]), words[1], words[2], int(words[3])))
        unit_codes = [unit.unit_code for unit in units]
        if unit_code not in unit_codes:
            print("Unit code is invalid")
            return
        if unit_code in [x[0] for x in self.enrolled_units]:
            print("You have enrolled!")
            return
        nums = 0
        with open('data/user.txt', 'r') as f:
            for line in f.readlines():
                if line.split(', ')[3] == 'ST' and unit_code in line:
                    nums += 1
        if nums < units[unit_codes.index(unit_code)].unit_capacity:
            self.enrolled_units.append((unit_code, -1))
            with open('data/user.txt', 'r') as f:
                lines = f.readlines()
            with open('data/user.txt', 'w') as f:
                for line in lines:
                    if self.user_name in line:
                        f.write(str(self) + '\n')
                    else:
                        f.write(line)
            print(f"Successfully enrolled in the {unit_code}!")
        else:
            print(f"Failed: The number of people has reached the capacity")

    def drop_unit(self, unit_code):
        """
        Remove the unit from the enrolled unit list
        :param unit_code: str
                The unit code of the unit (e.g. FIT9136)
        :return: None
        """

        # Nikita's attempt
        # # validating and dropping an enrolled unit
        # if not self.enrolled_units:
        #     print("You are not enrolled in any units")
        #     return
        # for i, unit in enumerate(self.enrolled_units):
        #     if unit[0] == unit_code:
        #         del self.enrolled_units[i]
        #         print(f"You have successfully dropped {unit_code}")
        #
        #         units_list = []
        #         with open('data/unit.txt') as units_file:
        #             for unit in units_file:
        #                 unit_data = unit.strip().split(',')
        #                 if unit_data[1].lower() == unit_code.lower():
        #                     current_unit = unit_data[0] + "," + unit_data[1] + \
        #                                    "," + unit_data[2] + "," + \
        #                                    str(int(unit_data[3]) + 1)
        #                     units_list.append(current_unit)
        #                 else:
        #                     units_list.append(unit.strip())
        # # updating the unit.txt after dropping the unit
        # file = open("data/unit.txt", "w")
        # for user in units_list:
        #     file.write(user + "\n")
        # file.close()
        #
        # all_user_data = []
        # with open('data/user.txt') as user_file:
        #     for user_data in user_file:
        #         current_user_data = user_data.strip()
        #         values = current_user_data.split(',')
        #         if (values[5] != None) and values[1] == self.user_name:
        #             line = values[0] + "," + values[1] + "," + \
        #                    values[2] + "," + values[3] + \
        #                    "," + values[4] + ","
        #             enrol_string = ""
        #             for x, y in self.enrolled_units:
        #                 if enrol_string != "":
        #                     enrol_string += "_"
        #                 enrol_string += str(x) + "-" + str(y)
        #             line += enrol_string
        #             all_user_data.append(line)
        #         else:
        #             all_user_data.append(user_data.strip())
        # # updating the user.txt after dropping the unit
        # file = open("data/user.txt", "w")
        # for user in all_user_data:
        #     file.write(user + "\n")
        # file.close()
        # return

        # Huixin - 07/05/2023 - In order to integrate with the application runs in main.py
        if not self.enrolled_units:
            print("You are not enrolled in any units")
            return
        for i in range(len(self.enrolled_units)):
            if self.enrolled_units[i][0] == unit_code:
                self.enrolled_units.pop(i)
                with open('data/user.txt', 'r') as f:
                    lines = f.readlines()
                with open('data/user.txt', 'w') as f:
                    for line in lines:
                        if self.user_name in line:
                            f.write(str(self) + '\n')
                        else:
                            f.write(line)
                print(f"You have successfully dropped {unit_code}")
                return
        print(f"You don't enroll the {unit_code} unit.")

    # function to check the scores of the enrolled units
    def check_score(self, unit_code=None):
        """
        Display the unit score
        :param unit_code: str
                The unit code of the unit (e.g. FIT9136)
        :return: None
        """
        if not self.enrolled_units:
            print("Not yet enrolled")
            return
        if unit_code is None:
            print("Scores:")
            for unit_code, score in self.enrolled_units:
                print(f"{unit_code}: {score}")
        else:
            for enrolled_unit_code, enrolled_unit_score in self.enrolled_units:
                if enrolled_unit_code == unit_code:
                    print(f"Score for {unit_code}: {enrolled_unit_score}")
                    return
            print("Not yet enrolled")

    # function to generate the scores of the given input unit code
    def generate_score(self, unit_code):
        """
        Generate a random score between 0 and 100 (inclusive) for
        a unit. This resulting score will be added to the student's
        list of enrolled units in the 'user.txt' file.

        :param unit_code: str
                The unit code of the unit (e.g. FIT9136)
        :return: None
        """

        # Nikita's attempt
        # enrolled_units = []
        # all_user_data = []
        # # updating the generated score in the user.txt file
        # with open('data/user.txt') as user_file:
        #     for user_data in user_file:
        #         current_user_data = user_data.strip()
        #         values = current_user_data.split(',')
        #         if (values[5] != None) and values[1] == self.user_name:
        #             enrol = values[5].split("_")
        #             for i in enrol:
        #                 unit = i.split("-")
        #                 if unit_code == unit[0]:
        #                     unit_score = random.randint(0, 100)
        #                 else:
        #                     unit_score = unit[1]
        #                 enrolled_units.append((unit[0], unit_score))
        #             self.enrolled_units = enrolled_units
        #
        #             line = values[0] + "," + values[1] + "," + \
        #                    values[2] + "," + values[3] + "," + values[4] + ","
        #
        #             enrol_string = ""
        #             for x, y in enrolled_units:
        #                 if enrol_string != "":
        #                     enrol_string += "_"
        #                 enrol_string += str(x) + "-" + str(y)
        #             line += enrol_string
        #             all_user_data.append(line)
        #     else:
        #         all_user_data.append(user_data.strip())

        # Huixin - 07/05/2023 - In order to integrate with the application runs in main.py
        for i in range(len(self.enrolled_units)):
            if self.enrolled_units[i][0] == unit_code:
                self.enrolled_units[i] = (unit_code, random.randint(0, 100))
                with open('data/user.txt', 'r') as f:
                    lines = f.readlines()
                with open('data/user.txt', 'w') as f:
                    for line in lines:
                        if self.user_name in line:
                            f.write(str(self) + '\n')
                        else:
                            f.write(line)
                print("Generated Successfully!")
                return
        print("Not yet enrolled")