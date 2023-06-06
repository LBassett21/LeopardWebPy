import tkinter as tk
from tkinter import Label

import sqlite3

# creates sql databases called courses.db and userinfo.db on the local dir
coursesdb = sqlite3.connect("courses.db")
#userinfodb = sqlite3.connect("userinfo.db")

coursesCur = coursesdb.cursor()
# creates a table with the following categories:
# CRN (primary key) | subject | course number | section number | title | term | type | credit hours
# coursesCur.execute("CREATE TABLE courses (crn INTEGER PRIMARY KEY, subject TEXT ,coursenum INTEGER, sectionnum INTEGER, title TEXT, term TEXT, type TEXT, credithr INTEGER)")
##coursesCur.execute("INSERT INTO courses VALUES (33950, 'ELEC', 3225, 01, 'APPLIED PROGRAMMING CONCEPTS', 'Summer 2023', 'Lecture (LEC)', 3)")

# variables to be added to the table, we can change these variables later, just to test if one course works
setCRN = 33950
setSubject = "ELEC"
setCourseNum = 3225
setSectNum = 1
setTitle = "APPLIED PROGRAMMING CONCEPTS"
setTerm = "Summer 2023"
setType = "Lecture (LEC)"
setCredHr = 3

# adds each of the variables to the database
# coursesCur.execute("INSERT INTO courses (crn, subject, coursenum, sectionnum, title, term, type, credithr) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (setCRN, setSubject, setCourseNum, setSectNum, setTitle, setTerm, setType, setCredHr))
# coursesdb.commit()

# Test printout of data in courses database
testPrint = coursesCur.execute("SELECT crn, subject, coursenum, sectionnum, title, term, type, credithr FROM courses").fetchall()
print(testPrint)

class leopardWeb():
    def build(self):
        return Label(text= "La website")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    window = tk.Tk()

    label = tk.Label(text = "Enter Username & Password")
    label.pack()

    label = tk.Label(text = "Username")
    label.pack()
    entry = tk.Entry()
    entry.pack()
    label = tk.Label(text = "Password")
    label.pack()
    entry = tk.Entry()
    entry.pack()
    button = tk.Button(text= "Login", background= "red", foreground="white")
    button.pack()

    window.mainloop()
