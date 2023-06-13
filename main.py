import tkinter as tk
from tkinter import Label
from tkinter import *
from PIL import ImageTk,Image

import sqlite3

# creates sql databases called courses.db and userinfo.db on the local dir
coursesdb = sqlite3.connect("courses.db")
userinfodb = sqlite3.connect("userinfo.db")



coursesCur = coursesdb.cursor()
userinfoCur=userinfodb.cursor()
# creates a table with the following categories:
# CRN (primary key) | subject | course number | section number | title | term | type | credit hours | start time | end time
# coursesCur.execute("CREATE TABLE courses (crn INTEGER PRIMARY KEY, subject TEXT ,coursenum INTEGER, sectionnum INTEGER, title TEXT, term TEXT, type TEXT, credithr INTEGER, starttime INTEGER, endtime INTEGER)")
#coursesCur.execute("INSERT INTO courses VALUES (33950, 'ELEC', 3225, 01, 'APPLIED PROGRAMMING CONCEPTS', 'Summer 2023', 'Lecture (LEC)', 3, 0800, 0950)")

# id (primary key) | username | password | user type
#userinfoCur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, type TEXT)")

setID = 403388
setUserName = "Admin"
setPassword = "Password"
setType = "Admin"

#userinfoCur.execute("INSERT INTO users (id, username, password, type) VALUES (?, ?, ?, ?)",(setID, setUserName, setPassword, setType))
#userinfodb.commit()

# variables to be added to the table, we can change these variables later, just to test if one course works
setCRN = 33950
setSubject = "ELEC"
setCourseNum = 3225
setSectNum = 1
setTitle = "APPLIED PROGRAMMING CONCEPTS"
setTerm = "Summer 2023"
setType = "Lecture (LEC)"
setCredHr = 3
setStartTime = 800
setEndTime = 950

# adds each of the variables to the database
# coursesCur.execute("INSERT INTO courses (crn, subject, coursenum, sectionnum, title, term, type, credithr, starttime, endtime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (setCRN, setSubject, setCourseNum, setSectNum, setTitle, setTerm, setType, setCredHr, setStartTime, setEndTime))
# coursesdb.commit()

# Test printout of data in courses database
#testPrint = coursesCur.execute("SELECT crn, subject, coursenum, sectionnum, title, term, type, credithr FROM courses").fetchall()
#print(testPrint)

def checkLogin(un,pw, window):
    userinfoCur.execute("SELECT username and password FROM users WHERE username = ? and password = ?", (un,pw))
    found = userinfoCur.fetchone()
    if found:
        print("Correct username & password")
        window.destroy()
        return True
    else:
        print("Incorrect username or password")

        return False


def homePage():
    window = tk.Tk()

    bg = ImageTk.PhotoImage(Image.open("banner.png"))
    canvas1 = Canvas(window, width=1100,height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0,0,image=bg, anchor="nw")
    #label = tk.Label(text = "Main Page")
    #label.pack()


def user_check():
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    window = tk.Tk()

    label = tk.Label(text = "Enter Username & Password")
    label.pack()

    bg = ImageTk.PhotoImage(Image.open("wit-background.jpg"))
    canvas1 = Canvas(window, width=400,height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0,0,image=bg,anchor="nw")

    label = tk.Label(text = "Username")
    label.pack()
    entry1 = tk.Entry()
    entry1.pack()
    label = tk.Label(text = "Password")
    label.pack()
    entry2 = tk.Entry(show='*')
    entry2.pack()
    button = tk.Button(text= "Login", background= "red", foreground="white",command=lambda: checkLogin(entry1.get(),entry2.get(), window))    #testing user input boxes: command=lambda: print(entry1.get()," ",entry2.get())
    button.pack()


    window.mainloop()




    homePage()

    window.mainloop()
