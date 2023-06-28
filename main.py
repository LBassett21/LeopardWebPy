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
# # creates a table with the following categories:
# # CRN (primary key) | subject | course number | section number | title | term | type | credit hours | start time | end time
# # coursesCur.execute("CREATE TABLE courses (crn INTEGER PRIMARY KEY, subject TEXT ,coursenum INTEGER, sectionnum INTEGER, title TEXT, term TEXT, type TEXT, credithr INTEGER, starttime INTEGER, endtime INTEGER)")
# #coursesCur.execute("INSERT INTO courses VALUES (33950, 'ELEC', 3225, 01, 'APPLIED PROGRAMMING CONCEPTS', 'Summer 2023', 'Lecture (LEC)', 3, 0800, 0950)")
#
# # id (primary key) | username | password | user type
# #userinfoCur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, type TEXT)")
#
# class app:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("200x200")
#         self.login()
#
#
#
#
#
#
#
# setID = 403388
# setUserName = "Admin"
# setPassword = "Password"
# setType = "Admin"
#
# #userinfoCur.execute("INSERT INTO users (id, username, password, type) VALUES (?, ?, ?, ?)",(setID, setUserName, setPassword, setType))
# #userinfodb.commit()
#
# # variables to be added to the table, we can change these variables later, just to test if one course works
# setCRN = 33950
# setSubject = "ELEC"
# setCourseNum = 3225
# setSectNum = 1
# setTitle = "APPLIED PROGRAMMING CONCEPTS"
# setTerm = "Summer 2023"
# setType = "Lecture (LEC)"
# setCredHr = 3
# setStartTime = 800
# setEndTime = 950
#
# # adds each of the variables to the database
# # coursesCur.execute("INSERT INTO courses (crn, subject, coursenum, sectionnum, title, term, type, credithr, starttime, endtime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (setCRN, setSubject, setCourseNum, setSectNum, setTitle, setTerm, setType, setCredHr, setStartTime, setEndTime))
# # coursesdb.commit()
#
# # Test printout of data in courses database
# #testPrint = coursesCur.execute("SELECT crn, subject, coursenum, sectionnum, title, term, type, credithr FROM courses").fetchall()
# #print(testPrint)
#

#
#
#
#
# label = tk.Label(text="Enter Username & Password")
# label.pack()
# bg = ImageTk.PhotoImage(Image.open("wit-background.jpg"))
# canvas1 = Canvas(my_w, width=400, height=400)
# canvas1.pack(fill="both", expand=True)
# canvas1.create_image(0, 0, image=bg, anchor="nw")
#
# label = tk.Label(text="Username")
# label.pack()
# entry1 = tk.Entry()
# entry1.pack()
# label = tk.Label(text="Password")
# label.pack()
# entry2 = tk.Entry(show='*')
# entry2.pack()
# button = tk.Button(text="Login", background="red", foreground="white",
#                    command=lambda:checkLogin(entry1.get(), entry2.get()))  # testing user input boxes: command=lambda: print(entry1.get()," ",entry2.get())
# button.pack()
#
#
#
# def mainPage():
#     my_w_child = Toplevel(my_w)
#     label = tk.Label(text = "Main Page")
#     label.pack()
#     bg = ImageTk.PhotoImage(Image.open("banner.png"))
#     canvas1 = Canvas(my_w_child, width=1100,height=400)
#
#     canvas1.create_image(0,0,image=bg, anchor="nw")
#     canvas1.pack(fill="both", expand=True)
#     personalInfo = tk.Button(my_w_child, text = "Personal Information", command=print("Personal Info Tab"))
#     personalInfo.pack()
#
#     student = tk.Button(my_w_child, text="Student", command=print("student")
#
#     )
#     student.pack()
#     financial = tk.Button(my_w_child, text="Financial Aid", command=print("Financial Aid")
#
#     )
#     financial.pack()
#
#     my_w_child.mainloop()


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.login()

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = tk.Label(self.frame1, text='Welcome to Leopardweb')
        self.reg_txt.pack()
        entry1 = Entry()
        entry1.pack()
        entry2 = Entry()
        entry2.pack()
        self.login_btn = Button(self.frame1, text="Login", command= lambda: self.checkLogin(str(entry1), str(entry2)))
        self.login_btn.pack()

    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Go to Login", command=lambda: self.login)
        self.login_btn.pack()

    def financial(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.reg_txt2 = tk.Label(self.frame5, text='Financial Aid')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame5, text="Go to home", command=lambda: self.home())
        self.login_btn.pack()

    def student(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.reg_txt2 = tk.Label(self.frame5, text='Student Information')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame5, text="Go to home", command=lambda: self.home())
        self.login_btn.pack()

    def personalInfo(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.reg_txt2 = tk.Label(self.frame5, text='Personal Information')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame5, text="Go to home", command=lambda: self.home())
        self.login_btn.pack()

    def home(self):

        for i in self.master.winfo_children():
            i.destroy()

        label = Label(text="Main Page")
        label.pack()
        bg = ImageTk.PhotoImage(Image.open("banner.png"))

        self.frame3 = Frame(self.master)
        self.frame3.pack()
        canvas1 = Canvas(self.master, width=1100, height=400)
        canvas1.pack()
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        self.reg_txt3 = Label(self.frame3, text='register')
        self.reg_txt3.pack()
        self.login_btn = Button(self.frame3, text="Home", command=lambda: self.login())
        self.login_btn.pack()
        self.login_btn = Button(self.frame3, text="Financial Aid", command=lambda: self.financial())
        self.login_btn.pack()
        self.login_btn = Button(self.frame3, text="Personal Information", command=lambda: self.personalInfo())
        self.login_btn.pack()
        self.login_btn = Button(self.frame3, text="Student", command=lambda: self.student())
        self.login_btn.pack()
    def checkLogin(self, un,pw):
        userinfoCur.execute("SELECT username and password FROM users WHERE username = ? and password = ?", (un, pw))
        found = userinfoCur.fetchone()
        if not found:
            print("Correct username & password")
            self.home()
        else:
            print("WRONG")


def main():
    # my_w = tk.Tk()
    # my_w.mainloop()
    root = Tk()
    app(root)
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


