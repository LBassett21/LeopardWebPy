from user import user
import sqlite3
db = sqlite3.connect('assignment3.db')
cursor = db.cursor()


# Student class definition.
class student(user):
    def __init__(self, ID, firstname, lastname, expdgradyr, major, email):
        super().__init__(ID, firstname, lastname)
        self.expdgradyr = expdgradyr
        self.major = major
        self.email = email
        self.schedule = [] # Schedule is a list of CRN's that can be added
    # Searches for course
    def searchCourse(self):
        # Opens up courses database
        cursor.execute("PRAGMA table_info(courses)")
        columns = cursor.fetchall()
        # pulls the headers of each of the columns
        column_names = [column[1] for column in columns]

        # Prints out to the user column names that they can query by
        print("Available columns for search:")
        for i, column in enumerate(column_names, start=1):
            print(f"{i}. {column}")

        # Based on choice, it will query the user's choice and print all rows that meet the requirements.
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

    # Add drop course. Takes in ad. If ad == true, then it will add course, else it will drop.
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
                    # Checks for conflicting courses in schedule
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

    # Prints the schedule of the user based on the CRN's in their schedule
    def printSchedule(self):
         print("------ Schedule ------")

         cursor.execute("""SELECT * FROM courses WHERE CRN IN ({}) ORDER BY TIME""".format(','.join(self.schedule)))
         scheduled_courses = cursor.fetchall()

         # Maps the days based on the database format to text format
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