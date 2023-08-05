from user import user
from instructor import instructor
from student import student
import sqlite3
db = sqlite3.connect('leopardweb.db')
cursor = db.cursor()

class Admin(user):
    def __init__(self, ID, firstname, lastname, title, office, email):
        super().__init__(ID, firstname, lastname)
        self.title = title
        self.office = office
        self.email = email

    # Add or remove user. If ar == true, then it will add user, else remove user
    def addRemoveUser(self, ar, badID, yes):
        if ar == True:
            print("What type of user would you like to add?")
            choice = input("Enter your choice (Admin, Instructor, Student): ")
            if choice == "Admin":
                print("Please enter the following information")
                idn = input("ID number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                title = input("Title: ")
                office = input("Office: ")
                email = input("Email: ")
                new_admin(idn, fn, ln, title, office, email)
            elif choice == "Instructor":
                print("Please enter the following information")
                idn = input("ID number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                title = input("Title: ")
                yoh = input("Year of Hire: ")
                dept = input("Department: ")
                email = input("Email: ")
                new_instructor(idn, fn, ln, title, yoh, dept, email)
            elif choice == "Student":
                print("Please enter the following information")
                idn = input("ID number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                egy = input("Expected graduation year: ")
                major = input("Major: ")
                email = input("Email: ")
                new_student(idn, fn, ln, egy, major, email)
            else:
                print("Invalid Input!")
        else:
            # remove user based on ID.
            print("Please enter the ID of the user")
            removeid = badID
            cursor.execute("""SELECT ID FROM admin WHERE ID=?""", (removeid,))
            admin_check = cursor.fetchone()
            cursor.execute("""SELECT ID FROM instructor WHERE ID=?""", (removeid,))
            instructor_check = cursor.fetchone()
            cursor.execute("""SELECT ID FROM student WHERE ID=?""", (removeid,))
            student_check = cursor.fetchone()
            if admin_check or instructor_check or student_check:
                confirm = yes
                if confirm == "yes":
                    if admin_check:
                        cursor.execute("""DELETE FROM admin WHERE ID=?""", (removeid,))
                        db.commit()
                        print("User removed from the admin table.")
                    if instructor_check:
                        cursor.execute("""DELETE FROM instructor WHERE ID=?""", (removeid,))
                        db.commit()
                        print("User removed from the instructor table.")
                    if student_check:
                        cursor.execute("""DELETE FROM student WHERE ID=?""", (removeid,))
                        db.commit()
                        print("User removed from the student table.")
                else:
                    print("Canceling user removal...")
            else:
                print("User not found in the database")

    # Add/remove course. If ar == true, add course, else remove course
    def addRemoveCourse(self, ar, CRN, Title, dept,Time, Days, Semester,Year, credit_num, remCRN):
        if ar:

            crn = int(CRN)
            title = str(Title)
            department = str(dept)
            time = str(Time)
            days = str(Days)
            semester = str(Semester)
            year = int(Year)
            creditnum = int(credit_num)
            cursor.execute("""SELECT CRN FROM courses WHERE CRN=?""", (crn,))
            existing_crn = cursor.fetchone()

            if existing_crn:
                print("Error: Course with CRN ", crn, "already exists.")
            else:
                cursor.execute(
                    """INSERT INTO courses (CRN, TITLE, DEPT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (?,?,?,?,?,?,?,?)""",
                    (crn, title, department, time, days, semester, year, creditnum))
                db.commit()
        else:
            print("Course Removal - Please enter the following information")
            removecrn = int(remCRN)
            cursor.execute("""SELECT CRN FROM courses WHERE CRN=?""", (removecrn,))
            courses_check = cursor.fetchone()
            if courses_check:
                cursor.execute("""DELETE FROM courses WHERE CRN=?""", (removecrn,))
                db.commit()
                print("Course removed from the courses table.")
            else:
                print("Invalid input!")

    # prints all courses
    def printRoster(self):
        cursor.execute("""SELECT * FROM courses""")
        course_info = cursor.fetchall()
        print("----- Courses -----")
        for row in course_info:
            print(row)

    # modify user based on selected ID

    def modUserAdmin(self, ID, choice, newVal):
        print("Enter the ID of the user that you would like to edit")
        editID = ID
        cursor.execute("""SELECT ID FROM admin WHERE ID=?""", (editID,))
        admin_check = cursor.fetchone()
        choice = choice
        match choice:
            case "1":
                newID = newVal
                cursor.execute("""UPDATE admin SET ID = ? WHERE ID = ?""", (newID, editID,))
                db.commit()
            case "2":
                newFN = newVal
                cursor.execute("""UPDATE admin SET NAME = ? WHERE ID = ?""", (newFN, editID,))
                db.commit()
            case "3":
                newLN = newVal
                cursor.execute("""UPDATE admin SET SURNAME = ? WHERE ID = ?""", (newLN, editID,))
                db.commit()
            case "4":
                newTitle = newVal
                cursor.execute("""UPDATE admin SET TITLE = ? WHERE ID = ?""", (newTitle, editID,))
                db.commit()
            case "5":
                newOffice = newVal
                cursor.execute("""UPDATE admin SET OFFICE = ? WHERE ID = ?""", (newOffice, editID,))
                db.commit()
            case "6":
                newEmail = newVal
                cursor.execute("""UPDATE admin SET EMAIL = ? WHERE ID = ?""", (newEmail, editID,))
                db.commit()
            case "7":
                print("Exiting...")
            case _:
                print("Invalid input!")


    def modifyInstructor(self,ID, choice, newVal):
        editID = ID
        cursor.execute("""SELECT ID FROM instructor WHERE ID=?""", (editID,))
        instructor_check = cursor.fetchone()

        if instructor_check:
            print("1. ID Number")
            print("2. First Name")
            print("3. Last Name")
            print("4. Title")
            print("5. Year of Hire")
            print("6. Department")
            print("7. Email")
            print("8. Exit")
            choice = choice
            match choice:
                case "1":
                    newID = newVal
                    cursor.execute("""UPDATE instructor SET ID = ? WHERE ID = ?""", (newID, editID,))
                    db.commit()
                case "2":
                    newFN = newVal
                    cursor.execute("""UPDATE instructor SET NAME = ? WHERE ID = ?""", (newFN, editID,))
                    db.commit()
                case "3":
                    newLN = newVal
                    cursor.execute("""UPDATE instructor SET SURNAME = ? WHERE ID = ?""", (newLN, editID,))
                    db.commit()
                case "4":
                    newTitle = newVal
                    cursor.execute("""UPDATE instructor SET TITLE = ? WHERE ID = ?""", (newTitle, editID,))
                    db.commit()
                case "5":
                    newHRYR = newVal
                    cursor.execute("""UPDATE instructor SET HIREYEAR = ? WHERE ID = ?""", (newHRYR, editID,))
                    db.commit()
                case "6":
                    newDEPT = newVal
                    cursor.execute("""UPDATE instructor SET DEPT = ? WHERE ID = ?""", (newDEPT, editID,))
                    db.commit()
                case "7":
                    newEmail = newVal
                    cursor.execute("""UPDATE instructor SET EMAIL = ? WHERE ID = ?""", (newEmail, editID,))
                    db.commit()
                case "8":
                    print("Exiting...")
                case _:
                    print("Invalid input!")

    def modUserStudent(self, ID, choice, newVal):
        editID = ID
        cursor.execute("""SELECT ID FROM student WHERE ID=?""", (editID,))
        student_check = cursor.fetchone()
        if student_check:
            print("1. ID Number")
            print("2. First Name")
            print("3. Last Name")
            print("4. Expected Graduation Year")
            print("5. Major")
            print("6. Email")
            print("7. Exit")
            choice = choice
            match choice:
                case "1":
                    newID = newVal
                    cursor.execute("""UPDATE student SET ID = ? WHERE ID = ?""", (newID, editID,))
                    db.commit()
                case "2":
                    newFN = newVal
                    cursor.execute("""UPDATE student SET NAME = ? WHERE ID = ?""", (newFN, editID,))
                    db.commit()
                case "3":
                    newLN = newVal
                    cursor.execute("""UPDATE student SET SURNAME = ? WHERE ID = ?""", (newLN, editID,))
                    db.commit()
                case "4":
                    newGRADYR = newVal
                    cursor.execute("""UPDATE student SET GRADYEAR = ? WHERE ID = ?""", (newGRADYR, editID,))
                    db.commit()
                case "5":
                    newMajor = newVal
                    cursor.execute("""UPDATE student SET MAJOR = ? WHERE ID = ?""", (newMajor, editID,))
                    db.commit()
                case "6":
                    newEmail = newVal
                    cursor.execute("""UPDATE student SET EMAIL = ? WHERE ID = ?""", (newEmail, editID,))
                    db.commit()
                case "7":
                    print("Exiting...")
                case _:
                    print("Invalid input!")

    def modifyUser(self):
        print("Enter the ID of the user that you would like to edit")
        editID = input("ID Number: ")
        cursor.execute("""SELECT ID FROM admin WHERE ID=?""", (editID,))
        admin_check = cursor.fetchone()
        cursor.execute("""SELECT ID FROM instructor WHERE ID=?""", (editID,))
        instructor_check = cursor.fetchone()
        cursor.execute("""SELECT ID FROM student WHERE ID=?""", (editID,))
        student_check = cursor.fetchone()
        if admin_check or instructor_check or student_check:
            print("Enter the attribute you would like to edit")
            if admin_check:
                print("1. ID Number")
                print("2. First Name")
                print("3. Last Name")
                print("4. Title")
                print("5. Office")
                print("6. Email")
                print("7. Exit")
                choice = input("Please enter your choice (1-7): ")
                match choice:
                    case "1":
                        newID = input("Please enter a new ID number: ")
                        cursor.execute("""UPDATE admin SET ID = ? WHERE ID = ?""", (newID, editID,))
                        db.commit()
                    case "2":
                        newFN = input("Please enter a new First name: ")
                        cursor.execute("""UPDATE admin SET NAME = ? WHERE ID = ?""", (newFN, editID,))
                        db.commit()
                    case "3":
                        newLN = input("Please enter a new Last name: ")
                        cursor.execute("""UPDATE admin SET SURNAME = ? WHERE ID = ?""", (newLN, editID,))
                        db.commit()
                    case "4":
                        newTitle = input("Please enter a new Title: ")
                        cursor.execute("""UPDATE admin SET TITLE = ? WHERE ID = ?""", (newTitle, editID,))
                        db.commit()
                    case "5":
                        newOffice = input("Please enter a new Office: ")
                        cursor.execute("""UPDATE admin SET OFFICE = ? WHERE ID = ?""", (newOffice, editID,))
                        db.commit()
                    case "6":
                        newEmail = input("Please enter a new Email: ")
                        cursor.execute("""UPDATE admin SET EMAIL = ? WHERE ID = ?""", (newEmail, editID,))
                        db.commit()
                    case "7":
                        print("Exiting...")
                    case _:
                        print("Invalid input!")
            elif instructor_check:
                print("1. ID Number")
                print("2. First Name")
                print("3. Last Name")
                print("4. Title")
                print("5. Year of Hire")
                print("6. Department")
                print("7. Email")
                print("8. Exit")
                choice = input("Please enter your choice (1-8): ")
                match choice:
                    case "1":
                        newID = input("Please enter a new ID number: ")
                        cursor.execute("""UPDATE instructor SET ID = ? WHERE ID = ?""", (newID, editID,))
                        db.commit()
                    case "2":
                        newFN = input("Please enter a new First name: ")
                        cursor.execute("""UPDATE instructor SET NAME = ? WHERE ID = ?""", (newFN, editID,))
                        db.commit()
                    case "3":
                        newLN = input("Please enter a new Last name: ")
                        cursor.execute("""UPDATE instructor SET SURNAME = ? WHERE ID = ?""", (newLN, editID,))
                        db.commit()
                    case "4":
                        newTitle = input("Please enter a new Title: ")
                        cursor.execute("""UPDATE instructor SET TITLE = ? WHERE ID = ?""", (newTitle, editID,))
                        db.commit()
                    case "5":
                        newHRYR = input("Please enter a new hire year: ")
                        cursor.execute("""UPDATE instructor SET HIREYR = ? WHERE ID = ?""", (newHRYR, editID,))
                        db.commit()
                    case "6":
                        newDEPT = input("Please enter a new Department: ")
                        cursor.execute("""UPDATE instructor SET DEPT = ? WHERE ID = ?""", (newDEPT, editID,))
                        db.commit()
                    case "7":
                        newEmail = input("Please enter a new Email: ")
                        cursor.execute("""UPDATE instructor SET EMAIL = ? WHERE ID = ?""", (newEmail, editID,))
                        db.commit()
                    case "8":
                        print("Exiting...")
                    case _:
                        print("Invalid input!")

            elif student_check:
                print("1. ID Number")
                print("2. First Name")
                print("3. Last Name")
                print("4. Expected Graduation Year")
                print("5. Major")
                print("6. Email")
                print("7. Exit")
                choice = input("Please enter your choice (1-7): ")
                match choice:
                    case "1":
                        newID = input("Please enter a new ID number: ")
                        cursor.execute("""UPDATE student SET ID = ? WHERE ID = ?""", (newID, editID,))
                        db.commit()
                    case "2":
                        newFN = input("Please enter a new First name: ")
                        cursor.execute("""UPDATE student SET NAME = ? WHERE ID = ?""", (newFN, editID,))
                        db.commit()
                    case "3":
                        newLN = input("Please enter a new Last name: ")
                        cursor.execute("""UPDATE student SET SURNAME = ? WHERE ID = ?""", (newLN, editID,))
                        db.commit()
                    case "4":
                        newGRADYR = input("Please enter a new Graduation year: ")
                        cursor.execute("""UPDATE student SET GRADYEAR = ? WHERE ID = ?""", (newGRADYR, editID,))
                        db.commit()
                    case "5":
                        newMajor = input("Please enter a new Major: ")
                        cursor.execute("""UPDATE student SET MAJOR = ? WHERE ID = ?""", (newMajor, editID,))
                        db.commit()
                    case "6":
                        newEmail = input("Please enter a new Email: ")
                        cursor.execute("""UPDATE student SET EMAIL = ? WHERE ID = ?""", (newEmail, editID,))
                        db.commit()
                    case "7":
                        print("Exiting...")
                    case _:
                        print("Invalid input!")


# function to add admin's to a list of objets
def add_admin():
    admin_list = []
    cursor.execute("""SELECT * FROM admin""")
    all_admin_info = cursor.fetchall()

    for admin_info in all_admin_info:
        ID, first_name, last_name, title, office, email = admin_info
        existing_admin = next((Admin for Admin in admin_list if Admin.ID == ID), None)
        if existing_admin:
            continue

        newadmin = Admin(ID, first_name, last_name, title, office, email)
        admin_list.append(newadmin)

    return admin_list


# function to add students's to a list of objets
def add_student():
    student_list = []
    cursor.execute("""SELECT * FROM student""")
    all_student_info = cursor.fetchall()

    for student_info in all_student_info:
        ID, first_name, last_name, expectedgradyear, major, email = student_info
        existing_student = next((student for student in student_list if student.ID == ID), None)
        if existing_student:
            continue

        newstudent = student(ID, first_name, last_name, expectedgradyear, major, email)
        student_list.append(newstudent)

    return student_list


# function to add instructors's to a list of objets
def add_instructor():
    instructor_list = []
    cursor.execute("""SELECT * FROM instructor""")
    all_instructor_info = cursor.fetchall()

    for instructor_info in all_instructor_info:
        ID, first_name, last_name, title, yearofhire, department, email = instructor_info
        existing_instructor = next((instructor for instructor in instructor_list if instructor.ID == ID), None)
        if existing_instructor:
            continue

        newinstructor = instructor(ID, first_name, last_name, title, yearofhire, department, email)
        instructor_list.append(newinstructor)

    return instructor_list


# Adds a new admin to the database
def new_admin(ID, firstname, lastname, title, office, email):
    cursor.execute("""SELECT ID FROM admin WHERE ID=?""", (ID,))
    existing_id = cursor.fetchone()

    if existing_id:
        print("Error: User with ID", ID, "already exists.")
    else:
        cursor.execute("""INSERT INTO admin (ID, NAME, SURNAME, TITLE, OFFICE, EMAIL) VALUES (?,?,?,?,?,?)""",
                       (ID, firstname, lastname, title, office, email))
        db.all


# Adds a new instructor to the database
def new_instructor(ID, first_name, last_name, title, yearofhire, department, email):
    cursor.execute("""SELECT ID FROM instructor WHERE ID=?""", (ID,))
    existing_id = cursor.fetchone()

    if existing_id:
        print("Error: User with ID", ID, "already exists.")
    else:
        cursor.execute(
            """INSERT INTO instructor (ID, NAME, SURNAME, TITLE, HIREYR, DEPT, EMAIL) VALUES (?,?,?,?,?,?,?)""",
            (ID, first_name, last_name, title, yearofhire, department, email))
        db.commit()


# Adds a new student to the database
def new_student(ID, first_name, last_name, expectedgradyear, major, email):
    ID = int(ID)
    first_name = str(first_name)
    last_name = str(last_name)
    expectedgradyear = int(expectedgradyear)
    major = str(major)
    email = str(email)

    cursor.execute("""SELECT ID FROM student WHERE ID=?""", (ID,))
    existing_id = cursor.fetchone()



    if existing_id:
        print("Error: User with ID", ID, "already exists.")
    else:
        cursor.execute("""INSERT INTO student (ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL) VALUES (?,?,?,?,?,?)""",
                       (ID, first_name, last_name, expectedgradyear, major, email))
        db.commit()


# Print's the database at start of program
def print_database():

    admin_objects = add_admin()
    student_objects = add_student()
    instructor_object = add_instructor()

    print("----- Students -----")
    for student in student_objects:
        print(student.ID, student.firstname, student.lastname, student.expdgradyr, student.major, student.email)

    print("----- Instructors -----")
    for instructor in instructor_object:
        print(instructor.ID, instructor.firstname, instructor.lastname, instructor.title, instructor.yearofhire,
              instructor.department, instructor.email)

    print("----- Admins -----")
    for Admin in admin_objects:
        print(Admin.ID, Admin.firstname, Admin.lastname, Admin.title, Admin.office, Admin.email)


# Init functions when program is run
admin_objects = add_admin()
student_objects = add_student()
instructor_object = add_instructor()
# print_database()


# Converts the 24 hour format to 12 hour format for schedule printing
def convert_time_format(time):
    hours, minutes = time.split(':')
    period = 'AM' if int(hours) < 12 else 'PM'

    if int(hours) > 12:
        hours = str(int(hours) - 12)

    return f"{hours}:{minutes} {period}"

