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

Description: This program handles a Student Information Management System which
utilizes "user.txt" file and "unit.txt" file located in the "data"folder. The
application feature multiple user roles including Admin, Teacher and Student,
each with varying levels of access to different operations.
"""

from user_admin import *
from user_student import *
from user_teacher import *

def main_menu():
    """

    Menu function of the Student Information Managment system.

    This function display all available operations for users to choose
    from and performs the operation based on the selection from the menu.

    Parameters
    ----------
    None

    Returns
    -------
    Userinput

    """
    os.system('clear' if os.name == 'posix' else 'cls')
    print('-' * 50)
    print("Welcome to the student management system!")
    print("1. Admin Login")
    print("2. Teacher Login")
    print("3. Student Login")
    print("4. Exit")

def generate_test_data():
    """

    This function generate test data for the program, including one
    admin user (with the username "admin" and password "password"),
    three units, three teachers (each allocated to one unit), and ten
    students (all of whom are enrolled in these three units, and
    students can enrol in more than one unit).

    This function will be called when the program starts and all the
    files will be overwritten by the newly generated test data.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    # Generating test data for users and units
    user = User()
    users_data = [
        f"12345, admin, {user.encrypt('password')}, AD, enabled",  # Admin user

        # 3 teachers
        f"11, teacherA, {user.encrypt('pw1')}, TA, enabled, ['FIT9131', 'FIT9134']",
        f"22, teacherB, {user.encrypt('pw2')}, TA, enabled, ['FIT9132', 'FIT9135']",
        f"33, teacherC, {user.encrypt('pw3')}, TA, enabled, ['FIT9133']",

        # 10 students
        f"111, studentA, {user.encrypt('pw5')}, ST, enabled, []",
        f"222, studentB, {user.encrypt('pw6')}, ST, enabled, [('FIT9134', 80)]",
        f"333, studentC, {user.encrypt('pw7')}, ST, enabled, [('FIT9131', 80)]",
        f"444, studentD, {user.encrypt('pw8')}, ST, enabled, [('FIT9131', 80), ('FIT9132', 80)]",
        f"555, studentE, {user.encrypt('pw9')}, ST, enabled, [('FIT9133', 66)]",
        f"666, studentF, {user.encrypt('pw10')}, ST, enabled, [('FIT9135', -1)]",
        f"777, studentG, {user.encrypt('pw11')}, ST, enabled, []",
        f"888, studentH, {user.encrypt('pw12')}, ST, enabled, []",
        f"999, studentI, {user.encrypt('pw13')}, ST, enabled, []",
        f"000, studentJ, {user.encrypt('pw14')}, ST, enabled, []"
    ]

    units_data = [
        # 3 units
        "1111111, FIT9131, Unit One, 30",  # Unit 1
        "2222222, FIT9132, Unit Two, 30",  # Unit 2
        "3333333, FIT9133, Unit Three, 2",  # Unit 3
        "4444444, FIT9134, Unit Four, 1",  # Unit 4
        "5555555, FIT9135, Unit Five, 5",  # Unit 5
    ]

    # Save test data to files
    with open("data/user.txt", "w") as user_file:
        for user in users_data:
            user_file.write(user + "\n")

    with open("data/unit.txt", "w") as unit_file:
        for unit in units_data:
            unit_file.write(unit + "\n")

def main():
    """
    This function is responsible for managing all aspects of the sytem.
    When the function is invoked, it will display a menu that allows the
    user to select menu options and input their login credentials. Once
    the user selects an option, the program will execute the relevant
    functions or display additional prompts as needed. The user is able to
    return to the menu at any time or exit the program if desired.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Examples
    --------

    >>>
    1. Login
    2. Exit

    Enter your choice (1-2): 1
    Enter your username: admin
    Enter your password:
    Login failed. Please check your credentials or user status.
    Press Enter to continue...

    >>>
    1. Login
    2. Exit

    Enter your choice (1-2):  Invalid choice. Please try again.
    Press Enter to continue...

    >>>
    --------------------------------------------------
    Welcome to the student management system!
    1. Admin Login
    2. Teacher Login
    3. Student Login
    4. Exit
    Enter your choice (1-4): 2
    --------Teacher Login--------
    Enter your username: teacherA
    Enter your password: pw1
    Login successful!
    --------------------------------------------------
    1. List teaching units
    2. Add teaching unit
    3. Delete teaching unit
    4. List enrolled students
    5. Show unit average, max, min score
    6. Log out
    Please enter your selection: 1
    1111111, FIT9131, Unit One, 30
    4444444, FIT9134, Unit Four, 1
    --------------------------------------------------
    1. List teaching units
    2. Add teaching unit
    3. Delete teaching unit
    4. List enrolled students
    5. Show unit average, max, min score
    6. Log out
    Please enter your selection: 2
    Please insert the new unit!
    Unit code: FIT9136
    Unit name: Algorithms and programming foundations in Python
    Unit capacity: 30
    --------------------------------------------------
    1. List teaching units
    2. Add teaching unit
    3. Delete teaching unit
    4. List enrolled students
    5. Show unit average, max, min score
    6. Log out
    Please enter your selection: 1
    1111111, FIT9131, Unit One, 30
    4444444, FIT9134, Unit Four, 1
    4659360, FIT9136, Algorithms and programming foundations in Python, 30
    --------------------------------------------------
    1. List teaching units
    2. Add teaching unit
    3. Delete teaching unit
    4. List enrolled students
    5. Show unit average, max, min score
    6. Log out
    Please enter your selection: 6
    Logging out...
    Press Enter to continue...
    >>>
    """
    generate_test_data()

    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")
        # Admin login
        user = User()
        if choice == '1':
            print("--------Admin Login--------")
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")

            user_info = user.login(user_name, user_password)

            if user_info and user_info.split(', ')[3] == 'AD':
                words = user_info.split(', ')
                user = UserAdmin(int(words[0]), words[1], words[2], words[3], words[4])
                while True:
                    user.admin_menu()
                    admin_input = input("Please enter your selection: ")
                    if admin_input == "1":
                        search_name = input("Please insert the name: ")
                        user.search_user(search_name)
                    elif admin_input == "2":
                        user.list_all_users()
                    elif admin_input == "3":
                        user.list_all_units()
                    elif admin_input == "4":
                        change_name = input("Please insert the user's name: ")
                        user.enable_disable_user(change_name)
                    elif admin_input == "5":
                        print("Please insert the information for the new user")
                        user_name = input("User name: ")
                        while user.check_username_exist(user_name):
                            print('Username already exists!')
                            user_name = input("User name: ")
                        user_password = input("Password: ")
                        user_role = input("Role: ")
                        if user_role == 'TA':
                            new_user = UserTeacher(None, user_name, user.encrypt(user_password), user_role, None, None)
                        elif user_role == 'ST':
                            new_user = UserStudent(None, user_name, user.encrypt(user_password), user_role, None, None)
                        else:
                            new_user = UserAdmin(None, user_name, user.encrypt(user_password), user_role, None)
                        user.add_user(new_user)
                    elif admin_input == "6":
                        user.delete_user(input("Please enter the username: "))
                    elif admin_input == "7":
                        print("Logging out...")
                        break
            else:
                print("Login failed. Please check your credentials or user status.")

        # Teacher login
        if choice == '2':
            print("--------Teacher Login--------")
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")

            user_info = user.login(user_name, user_password)

            if user_info and user_info.split(', ')[3] == 'TA':
                words = user_info.split(', ')
                user = UserTeacher(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:])))
                print("Login successful!")
                while True:
                    user.teacher_menu()
                    teacher_input = input("Please enter your selection: ")
                    if teacher_input == "1":
                        user.list_teach_units()
                    elif teacher_input == "2":
                        print("Please insert the new unit!")
                        unit_code = input("Unit code: ")
                        unit_name = input("Unit name: ")
                        unit_capacity = input("Unit capacity: ")
                        new_unit = Unit(None, unit_code, unit_name, unit_capacity)
                        user.add_teach_unit(new_unit)
                    elif teacher_input == "3":
                        user.delete_teach_unit(input("Insert the unit code to delete: "))
                    elif teacher_input == "4":
                        unit_code = input("Insert the unit code: ")
                        user.list_enrol_students(unit_code)
                    elif teacher_input == "5":
                        user.show_unit_avg_max_min_score(input("Insert the unit code: "))
                    elif teacher_input == "6":
                        print("Logging out...")
                        break
            else:
                print("Login failed. Please check your credentials or user status.")

        # Student login
        if choice == '3':
            print("--------Student Login--------")
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")

            user_info = user.login(user_name, user_password)

            if user_info and user_info.split(', ')[3] == 'ST':
                words = user_info.split(', ')
                user = UserStudent(int(words[0]), words[1], words[2], words[3], words[4], eval(', '.join(words[5:])))
                print("Login successful!")
                while True:
                    user.student_menu()
                    student_input = input("Please enter your selection: ")
                    if student_input == "1":
                        user.list_available_units()
                    elif student_input == "2":
                        user.list_enrolled_units()
                    elif student_input == "3":
                        user.enrol_unit(input("Insert the unit code to enrol: "))
                    elif student_input == "4":
                        unitCode_drop = input("Insert the unit code to drop: ")
                        user.drop_unit(unitCode_drop)
                    elif student_input == "5":
                        user.check_score(input("Please insert the Unit code to check score: "))
                    elif student_input == "6":
                        user.generate_score(input("Please insert the unit code to generate scroe: "))
                    elif student_input == "7":
                        print("Logging out...")
                        break
            else:
                print("Login failed. Please check your credentials or user status.")

        # Exit the program
        if choice == '4':
            print("Exiting the application...")
            exit(0)

        if choice not in '1234':
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
