import tkinter as tk
from tkinter import Label
from tkinter import *
from PIL import ImageTk,Image
import webview
# import database
import sqlite3
from admin import Admin
from student import student
from instructor import instructor
import database


# creates sql databases called courses.db and userinfo.db on the local dir
coursesdb = sqlite3.connect("courses.db")
userinfodb = sqlite3.connect("userinfo.db")
db = sqlite3.connect('assignment3.db')
cursor = db.cursor()

coursesCur = coursesdb.cursor()
userinfoCur=userinfodb.cursor()

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

        bg = PhotoImage(file="banner.png")
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        label1 = Label(self.frame1, image=bg)
        label1.pack()
        self.reg_txt = tk.Label(self.frame1, text='Welcome to Leopardweb')
        self.reg_txt.pack()
        entry1 = Entry()
        entry1.pack()
        entry2 = Entry()
        entry2.pack()
        self.login_btn = Button(self.frame1, text="Login", command=lambda: self.checkLogin(entry1.get(), entry2.get()))
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

    def studentRecords(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='Student Records')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Go to Login", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Academic Transcript", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Account Summary", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Account Summary by Term", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Course Section Search", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Degree Audit", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="E-Bill", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Midterm Grades", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="View Student Information", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Grade Detail", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Course Catalog", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Account Detail for Term", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Application for Graduation", command=lambda: self.login)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="View Diploma Name", command=lambda: self.login)
        self.login_btn.pack()

    def registratation(self):
        for i in self.master.winfo_children():
            i.destroy()
            self.frame5 = Frame(self.master, width=300, height=300)
            self.frame5.pack()
            # self.button = tk.Button(self.frame5, text= "show courses", command= lambda: )

    def financial(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.reg_txt2 = tk.Label(self.frame5, text='Financial Aid')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame5, text="Go to home", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Financial Aid Status", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Eligibility", command=lambda: self.home())
        self.login_btn.pack()

        self.login_btn = tk.Button(self.frame5, text="Financial Aid Package", command=lambda: self.home())
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
        self.login_btn = tk.Button(self.frame5, text="Registration and Planning", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="E-Bill", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Online Payment Central", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Manage Your Refund Preferences", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Student Records", command=lambda: self.studentRecords())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="BookNow", command=lambda: self.home())
        self.login_btn.pack()
        webview.create_window('1098-T Form', 'https://tra.maximus.com/')
        self.login_btn = tk.Button(self.frame5, text="1098-T Form Website", command=lambda: webview.start())
        self.login_btn.pack()
        webview.create_window('Alumni Hub', 'https://tra.maximus.com/')
        self.login_btn = tk.Button(self.frame5, text="NSC Alumni MyHub", command=lambda: webview.start())
        self.login_btn.pack()

    def personalInfo(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()

        img = ImageTk.PhotoImage(Image.open("banner.png"))
        self.banner = tk.Label(self.frame5, image = img)
        self.banner.pack()
        self.reg_txt2 = tk.Label(self.frame5, text='Personal Information')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame5, text="Go to home", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Name Change Information", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Social Security Number Change Information", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Directory Listing Opt-Out (FERPA)", command=lambda: self.home())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Additional Gender Information", command=lambda: self.home())
        self.login_btn.pack()

    def home(self):

        for i in self.master.winfo_children():
            i.destroy()

        label = Label(text="Main Page")
        label.pack()
        self.frame3 = Frame(self.master)
        self.frame3.pack()
        bg=Image.open("banner.png")
        bg = ImageTk.PhotoImage(bg)
        label = Label(self.master, image = bg)
        label.pack()
        canvas1 = Canvas(self.master, width=1100, height=400)
        canvas1.pack()
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        self.login_btn = Button(self.frame3, text="Home", command=lambda: self.login())
        self.login_btn.pack()
        self.login_btn = Button(self.frame3, text="Personal Information", command=lambda: self.personalInfo())
        self.login_btn.pack()
        self.login_btn = Button(self.frame3, text="Financial Aid", command=lambda: self.financial())
        self.login_btn.pack()
        self.login_btn = Button(self.frame3, text="Student", command=lambda: self.student())
        self.login_btn.pack()
    def checkLogin(self, username, password):

        print(username)
        print(password)

        cursor.execute("""SELECT * FROM STUDENT""")
        debug = cursor.fetchall()
        print(debug)


        cursor.execute("""SELECT * FROM admin WHERE EMAIL=? AND ID=?""", (username, password))
        admin_data = cursor.fetchone()

        cursor.execute("""SELECT * FROM instructor WHERE EMAIL=? AND ID=?""", (username, password))
        instructor_data = cursor.fetchone()

        cursor.execute("""SELECT * FROM student WHERE EMAIL=? AND ID=?""", (username, password))
        student_data = cursor.fetchone()



        if admin_data:
            print("Welcome, Admin!")
            access_granted = True
            return Admin(*admin_data)
        elif instructor_data:
            print("Welcome, Instructor!")
            access_granted = True
            return instructor(*instructor_data)
        elif student_data:
            print("Welcome, Student!")
            access_granted = True
            self.home()

        else:
            print("Incorrect username or password, please try again")





def main():
    # my_w = tk.Tk()
    # my_w.mainloop()

    root = Tk()
    app(root)
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()