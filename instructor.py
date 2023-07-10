from user import user
import sqlite3
db = sqlite3.connect('assignment3.db')
cursor = db.cursor()

class instructor(user):
    def __init__(self, ID, firstname, lastname, title, yearofhire, department, email):
        super().__init__(ID, firstname, lastname)
        self.title = title
        self.yearofhire = yearofhire
        self.department = department
        self.email = email
        self.schedule = []

    # Prints the schedule of the user based on the CRN's in their schedule
    def printSchedule(self):
         print("------ Schedule ------")

         cursor.execute("""SELECT * FROM courses WHERE CRN IN ({}) ORDER BY TIME""".format(','.join(self.schedule)))
         scheduled_courses = cursor.fetchall()

         day_mapping = {'M': 'Monday', 'T': 'Tuesday', 'W': 'Wednesday', 'R': 'Thursday', 'F': 'Friday'}

         sorted_courses = sorted(scheduled_courses, key=lambda x: x[3])

         current_day = None

         for course in sorted_courses:
             crn, title, dept, time, days, semester, year, credits = course

             day_codes = list(days)
             start_time, end_time = time.split('-')

             if current_day != day_codes:
                 current_day = day_codes
                 print("\n" + ', '.join(day_mapping[day] for day in current_day) + ":")

             start_time = convert_time_format(start_time)
             end_time = convert_time_format(end_time)


             print(f"CRN: {crn} | Course: {title} | Time: {start_time}-{end_time}")

         print("----------------------")

    # Not implemented/added
    def printClassList(self):
        print("Printed out your class list! Kinda...")

    # searches for courses in database (same as student)
    def searchCourse(self):
        cursor.execute("PRAGMA table_info(courses)")
        columns = cursor.fetchall()
        column_names = [column[1] for column in columns]

        print("Available columns for search:")
        for i, column in enumerate(column_names, start=1):
            print(f"{i}. {column}")

        choice = input("Enter the column number to search: ")
        if choice.isdigit() and int(choice) in range(1, len(column_names) + 1):
            column = column_names[int(choice) - 1]
            value = input(f"Enter the value to search for in {column}: ")

            cursor.execute(f"SELECT * FROM courses WHERE {column}=?", (value,))
            results = cursor.fetchall()

            if results:
                print("Search Results:")
                for row in results:
                    print(row)
            else:
                print("No results found.")
        else:
            print("Invalid column choice.")

    # Adds/Drops course (same as student)
    def addDropCourse(self, ad):
        crn = input("Enter the CRN of the course: ")
        cursor.execute("""SELECT * FROM courses WHERE CRN=?""", (crn,))
        course_data = cursor.fetchone()

        if course_data:
            if ad and crn in self.schedule:
                print("Course with CRN", crn, "is already in your schedule.")
            elif not ad and crn not in self.schedule:
                print("Course with CRN", crn, "is not in your schedule.")
            else:
                if ad:
                    conflicting_courses = []
                    for scheduled_crn in self.schedule:
                        cursor.execute("""SELECT * FROM courses WHERE CRN=?""", (scheduled_crn,))
                        scheduled_course_data = cursor.fetchone()

                        if scheduled_course_data[4] == course_data[4] and scheduled_course_data[5] == course_data[5]:
                            conflicting_courses.append(scheduled_course_data)

                    if conflicting_courses:
                        print("The course conflicts with the following courses in your schedule:")
                        for course in conflicting_courses:
                            print(course)
                    else:
                        self.schedule.append(crn)
                        print("Course with CRN", crn, "added to your schedule.")
                else:
                    self.schedule.remove(crn)
                    print("Course with CRN", crn, "removed from your schedule.")
        else:
            print("Course with CRN", crn, "does not exist.")


# Converts the 24 hour format to 12 hour format for schedule printing
def convert_time_format(time):
    hours, minutes = time.split(':')
    period = 'AM' if int(hours) < 12 else 'PM'

    if int(hours) > 12:
        hours = str(int(hours) - 12)

    return f"{hours}:{minutes} {period}"