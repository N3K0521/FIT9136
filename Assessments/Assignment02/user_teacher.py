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

import os
import random
from user import User
from user_student import UserStudent
from unit import Unit

class UserTeacher(User):
    """
    UserTeacher Class: Inherits from the User class and represents a teacher user.

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
    techer_menu():
        Display teacher operations menu
    list_teach_units():
        Display the information of all units that are taught by the
        current teacher.
    add_teach_unit():
        Add a new unit information to the data/unit.txt and add the
        unit_code in the current teacher's 'teach_units' list
    delete_teach_unit(unit_obj):
        Delete a unit from the current teacher's 'teach_units' list.
        If this unit has been enrolled by students, remove all associated
        enrollment records as well.
    list_enrol_students(unit_code):
        Display the information of all students currently enrolled in the unit.
    show_unit_avg_max_min_score(unit_code):
        Display the unit's average, maximum and minimum score
    """
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role="TA", user_status="enabled", teach_units=None):
        """
        Initializes a teacher object.

        Uses the super() function to call the __init__ of the User class.
        If teach_units is not provided, it defaults to an empty list.

        :param user_id: int
            The id of the teacher (default is None)
            Must be unique integer
        :param user_name: str
            The name of the teacher (default is None)
            Must be unique and can only consist of numbers,
                letters, underscores
        :param user_password: str
            The password of the user (default is None)
            Must be encrypted
        :param user_role: str
            The role of the user (default is 'TA')
        :param user_status: str
            The stored user status of the user (default is "enabled")
        :param teach_units: list
            A list of units code taught by the teacher
        """
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.teach_units = teach_units if teach_units else []

    def __str__(self):
        """
        Returns the teacher's information as a formatted string.
        """
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}, {self.teach_units}"

    def teacher_menu(self):
        """
        Displays a list of all operations that can only be performed by a teacher.
        """
        print('-' * 50)
        print("1. List teaching units")
        print("2. Add teaching unit")
        print("3. Delete teaching unit")
        print("4. List enrolled students")
        print("5. Show unit average, max, min score")
        print("6. Log out")

    def list_teach_units(self):
        """
        Displays the information of all units that are taught by the current teacher.
        :param: None
        :return: None
        """
        if not self.teach_units:
            print("No units taught by the teacher are found in the system.")
            return
        with open("data/unit.txt", "r") as file:
            for line in file:
                unit_data = line.strip().split(", ")
                if unit_data[1] in self.teach_units:
                    print(line.strip())

    def add_teach_unit(self, unit_obj):
        """
        Adds a new unit information to the data/unit.txt and adds the unit_code in the current teacher's 'teach_units' list
        :param: unit_obj
            An instance of the Unit class
        :return: None
        """
        self.teach_units.append(unit_obj.unit_code)
        with open("data/unit.txt", "a") as file:
            file.write(str(unit_obj) + "\n")
        with open("data/user.txt", "r") as file:
            lines = file.readlines()
        with open("data/user.txt", "w") as file:
            for line in lines:
                if self.user_name in line:
                    line = str(self) + "\n"
                file.write(line)

    def delete_teach_unit(self, unit_code):
        """
        Deletes a unit from the current teacher's 'teach_units' list.
        :param unit_code: str
            The unit code of the unit (e.g. FIT9136)
        :return: None
        """
        if unit_code in self.teach_units:
            self.teach_units.remove(unit_code)
        with open("data/unit.txt", "r") as file:
            lines = file.readlines()
        with open("data/unit.txt", "w") as file:
            for line in lines:
                if unit_code not in line:
                    file.write(line)
        with open("data/user.txt", "r") as file:
            lines = file.readlines()
        with open("data/user.txt", "w") as file:
            for line in lines:
                if self.user_name in line:
                    line = str(self) + "\n"
                elif unit_code in line and line.split(', ')[3] == 'ST':
                    words = line.strip().split(', ')
                    student = UserStudent(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:])))
                    for enrolled_unit in student.enrolled_units:
                        if enrolled_unit[0] == unit_code:
                            student.enrolled_units.remove(enrolled_unit)
                    line = str(student) + "\n"
                file.write(line)

    def list_enrol_students(self, unit_code):
        """
        Displays the information of all students currently enrolled in the unit.
        :param unit_code: str
            The unit code of the unit (e.g. FIT9136)
        :return: None
        """

        #Enze's attempt
        # with open("data/unit.txt", "r") as file:
        #     for line in file:
        #         unit_data = line.strip().split(", ")
        #         if unit_data[1] == unit_code:
        #             students = unit_data[4].split(";")
        #             if not students:
        #                 print("No students are enrolled in this unit.")
        #             for student in students:
        #                 print(student)

        # Huixin - 09/05/2023 - In order to integrate with the application runs in main.py
        with open("data/user.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            if unit_code in line and line.split(', ')[3] == 'ST':
                words = line.strip().split(', ')
                student = UserStudent(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:])))
                print(student)

    def show_unit_avg_max_min_score(self, unit_code):
        """
        Displays the average, maximum, and minimum scores of a specific unit.

        It reads the unit data from 'data/unit.txt' file and calculates the average, max, and min scores
        only if the scores are available.
        :param unit_code: str
            The unit code of the unit (e.g. FIT9136)
        :return: None
        """
        # Enze's attempt
        # with open("data/unit.txt", "r") as file:
        #     for line in file:
        #         unit_data = line.strip().split(", ")
        #         if unit_data[1] == unit_code:
        #             scores = [int(score) for score in unit_data[4].split(";") if score.isdigit()]
        #             if not scores:
        #                 print("No scores available for this unit.")
        #             else:
        #                 avg_score = sum(scores) / len(scores)
        #                 max_score = max(scores)
        #                 min_score = min(scores)
        #                 print(f"Average score: {avg_score}")
        #                 print(f"Max score: {max_score}")
        #                 print(f"Min score: {min_score}")

        # Huixin - 09/05/2023 - In order to integrate with the application runs in main.py
        with open("data/user.txt", "r") as file:
            lines = file.readlines()
        scores = []
        for line in lines:
            if unit_code in line and line.split(', ')[3] == 'ST':
                words = line.strip().split(', ')
                student = UserStudent(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:])))
                for enrolled_unit in student.enrolled_units:
                    if enrolled_unit[0] == unit_code:
                        scores.append(enrolled_unit[1])
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"Max score: {max(scores)}")
        print(f"Min score: {min(scores)}")
