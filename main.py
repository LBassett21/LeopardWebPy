import tkinter as tk
from tkinter import Label
from tkinter import *
from PIL import ImageTk,Image
import webview
# import database
import sqlite3
from tkinter import ttk

import admin
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

TRANSCRIPTOPTIONBOX1 = ["All Levels", "Undergraduate"]
TRANSCRIPTOPTIONBOX2 = ["Self Service"]

class app:
    def __init__(self, master):
        self.master = master
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" %(width,height))
        self.login()

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame1 = tk.Frame(self.master)
        self.frame1.pack(fill=tk.BOTH, expand=True)

        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()

        bg_image = Image.open("wit-background.png")
        bg_image = bg_image.resize((width, height), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.frame1, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        black_bar = tk.Frame(self.frame1, bg="black", height=50)
        black_bar.pack(fill="x")

        logo_image = Image.open("Logo_Lockup_Red-Dark_Bkgd.png")
        logo_height = 50
        logo_width = int((logo_image.width / logo_image.height) * logo_height)
        logo_image = logo_image.resize((logo_width, logo_height), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(black_bar, image=self.logo, bg="black")
        logo_label.pack(side="left", padx=10)

        white_frame = tk.Frame(self.frame1, bg="white", relief="raised", borderwidth=5)
        white_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

        self.reg_txt = tk.Label(white_frame, text='Enter Username and Password', font=("Roboto", 18), bg="white")
        self.reg_txt.pack(pady=10, padx=10, anchor="w")
        self.un_txt = tk.Label(white_frame, text='Username:', font=("Roboto", 10), bg="white")
        self.un_txt.pack(pady=5, padx=10, anchor="w")
        entry1 = Entry(white_frame, width=40, font=("Roboto", 12))
        entry1.pack(pady=5)
        self.pw_txt = tk.Label(white_frame, text='Password:', font=("Roboto", 10), bg="white")
        self.pw_txt.pack(pady=5, padx=10, anchor="w")
        entry2 = Entry(white_frame, width=40, font=("Arial", 12), show="*")
        #entry2 = Entry(white_frame, show="*")      #Uncomment for final version
        entry2.pack(pady=5)
        self.login_btn = Button(white_frame, text="LOGIN", width=20, relief="raised", bg="#%02x%02x%02x" %(209,0,3), fg="white", font=("Roboto", 20), command=lambda: self.checkLogin(entry1.get(), entry2.get()))
        self.login_btn.pack(pady=10)
        warning_text = "For security reasons, please log out and exit your web browser when you are done accessing services that require authentication!"
        text_widget = tk.Label(white_frame, text=warning_text, font=("Roboto", 10), bg="white", wraplength=350, anchor="w")
        text_widget.pack(pady=(0, 10))


    def adminHome(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Main Menu", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        print_roster_btn = Button(self.frame2, text="Print Course Roster", command=lambda: self.adminRoster())
        print_roster_btn.pack(anchor="w", padx=3, pady=2)

        add_remove_usr_btn = Button(self.frame2, text="Add Student", command=lambda: self.adminNewStudent())
        add_remove_usr_btn.pack(anchor="w", padx=3, pady=2)

        add_course_btn = Button(self.frame2, text="Remove User", command=lambda: self.removeUser())
        add_course_btn.pack(anchor="w", padx=3, pady=2)

        add_course_btn = Button(self.frame2, text="Add Course", command=lambda: self.courseAdd())
        add_course_btn.pack(anchor="w", padx=3, pady=2)

        rem_course_btn = Button(self.frame2, text="Remove Course", command=lambda: self.courseRem())
        rem_course_btn.pack(anchor="w", padx=3, pady=2)

        mod_user_btn = Button(self.frame2, text="Modify An Admin", command=lambda: self.adminModAdmin())
        mod_user_btn.pack(anchor="w", padx=3, pady=2)

        mod_user_btn = Button(self.frame2, text="Modify An Instructor", command=lambda: self.adminModInstructor())
        mod_user_btn.pack(anchor="w", padx=3, pady=2)

        mod_user_btn = Button(self.frame2, text="Modify A Student", command=lambda: self.adminModStudent())
        mod_user_btn.pack(anchor="w", padx=3, pady=2)

        print_users_btn = Button(self.frame2, text="Print All Users", command=lambda: self.print_All())
        print_users_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def removeUser(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="All Users", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        label = tk.Label(self.frame2, text = "User ID You Would Like to Remove")
        label.pack()

        entry = tk.Entry(self.frame2)
        entry.pack()

        button = tk.Button(self.frame2, text= "Remove User", command=lambda: [Admin.addRemoveUser(self, False, entry.get(), "yes"), self.adminHome()])
        button.pack()





    def print_All(self):
        admin_objects = admin.add_admin()
        student_objects = admin.add_student()
        instructor_object = admin.add_instructor()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="All Users", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")
        self.label = tk.Label(self.frame2, text="Students", font=("Roboto", 14)).place(x=200, y=295)

        cursor.execute("""SELECT * FROM STUDENT""")
        student_info = cursor.fetchall()

        self.label = tk.Label(self.frame2, text='ID', font=("Roboto", 10)).place(x=50, y=350)
        self.label = tk.Label(self.frame2, text="NAME", font=("Roboto", 10)).place(x=100, y=350)
        self.label = tk.Label(self.frame2, text="SURNAME", font=("Roboto", 10)).place(x=150, y=350)
        self.label = tk.Label(self.frame2, text="GRAD YEAR", font=("Roboto", 10)).place(x=250, y=350)
        self.label = tk.Label(self.frame2, text="MAJOR", font=("Roboto", 10)).place(x=400, y=350)
        self.label = tk.Label(self.frame2, text="EMAIL", font=("Roboto", 10)).place(x=500, y=350)



        y = 375

        for row in student_info:
            self.label = tk.Label(self.frame2, text=row[0], font=("Roboto", 10)).place(x=50, y=y)
            self.label = tk.Label(self.frame2, text=row[1], font=("Roboto", 10)).place(x=100, y=y)
            self.label = tk.Label(self.frame2, text=row[2], font=("Roboto", 10)).place(x=150, y=y)
            self.label = tk.Label(self.frame2, text=row[3], font=("Roboto", 10)).place(x=250, y=y)
            self.label = tk.Label(self.frame2, text=row[4], font=("Roboto", 10)).place(x=400, y=y)
            self.label = tk.Label(self.frame2, text=row[5], font=("Roboto", 10)).place(x=500, y=y)

            print(row)

            y += 20

        self.label = tk.Label(self.frame2, text="Instructors", font=("Roboto", 14)).place(x=700, y=295)

        cursor.execute("""SELECT * FROM INSTRUCTOR""")
        student_info = cursor.fetchall()
        self.label = tk.Label(self.frame2, text='ID', font=("Roboto", 10)).place(x=650, y=350)
        self.label = tk.Label(self.frame2, text="NAME", font=("Roboto", 10)).place(x=725, y=350)
        self.label = tk.Label(self.frame2, text="SURNAME" ,font=("Roboto", 10)).place(x=800, y=350)
        self.label = tk.Label(self.frame2, text="TITLE", font=("Roboto", 10)).place(x=875, y=350)
        self.label = tk.Label(self.frame2, text="HIRE YEAR", font=("Roboto", 10)).place(x=975, y=350)
        self.label = tk.Label(self.frame2, text="DEPT.", font=("Roboto", 10)).place(x=1100, y=350)
        self.label = tk.Label(self.frame2, text="EMAIL", font=("Roboto", 10)).place(x=1175, y=350)
        y = 375
        for row in student_info:
            self.label = tk.Label(self.frame2, text=row[0], font=("Roboto", 10)).place(x=650, y=y)
            self.label = tk.Label(self.frame2, text=row[1], font=("Roboto", 10)).place(x=725, y=y)
            self.label = tk.Label(self.frame2, text=row[2], font=("Roboto", 10)).place(x=800, y=y)
            self.label = tk.Label(self.frame2, text=row[3], font=("Roboto", 10)).place(x=875, y=y)
            self.label = tk.Label(self.frame2, text=row[4], font=("Roboto", 10)).place(x=975, y=y)
            self.label = tk.Label(self.frame2, text=row[5], font=("Roboto", 10)).place(x=1100, y=y)
            self.label = tk.Label(self.frame2, text=row[6], font=("Roboto", 10)).place(x=1175, y=y)
            print(row)
            y += 20

        self.label = tk.Label(self.frame2, text="Admins", font=("Roboto", 14)).place(x=1500, y=295)
        cursor.execute("""SELECT * FROM ADMIN""")
        student_info = cursor.fetchall()

        self.label = tk.Label(self.frame2, text='ID', font=("Roboto", 10)).place(x=1300, y=350)
        self.label = tk.Label(self.frame2, text="NAME", font=("Roboto", 10)).place(x=1375, y=350)
        self.label = tk.Label(self.frame2, text="SURNAME", font=("Roboto", 10)).place(x=1475, y=350)
        self.label = tk.Label(self.frame2, text="TITLE", font=("Roboto", 10)).place(x=1550, y=350)
        self.label = tk.Label(self.frame2, text="OFFICE", font=("Roboto", 10)).place(x=1650, y=350)
        self.label = tk.Label(self.frame2, text="EMAIL", font=("Roboto", 10)).place(x=1800, y=350)

        y = 375
        for row in student_info:
            self.label = tk.Label(self.frame2, text=row[0], font=("Roboto", 10)).place(x=1300, y=y)
            self.label = tk.Label(self.frame2, text=row[1], font=("Roboto", 10)).place(x=1375, y=y)
            self.label = tk.Label(self.frame2, text=row[2], font=("Roboto", 10)).place(x=1475, y=y)
            self.label = tk.Label(self.frame2, text=row[3], font=("Roboto", 10)).place(x=1550, y=y)
            self.label = tk.Label(self.frame2, text=row[4], font=("Roboto", 10)).place(x=1650, y=y)
            self.label = tk.Label(self.frame2, text=row[5], font=("Roboto", 10)).place(x=1800, y=y)

            print(row)
            y += 20

    def adminModInstructor(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Modify Student", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        label = tk.Label(self.frame2, text="Enter the ID of the user that you would like to edit")
        label.pack()
        entry = tk.Entry(self.frame2)
        entry.pack()
        label = tk.Label(self.frame2, text="Enter the number associated with the feature you would like to change")
        label.pack()
        label = tk.Label(self.frame2, text="(1) ID, (2) Name, (3) Surname, (4) Title, (5) Hire Year, (6) Dept., (7) Email")
        label.pack()
        entry2 = tk.Entry(self.frame2)
        entry2.pack()
        label = tk.Label(self.frame2, text="New Value")
        label.pack()
        entry3 = tk.Entry(self.frame2)
        entry3.pack()
        button = tk.Button(self.frame2, text = "Continue", command =lambda: [Admin.modifyInstructor(self, entry.get() ,entry2.get(), entry3.get(), ), self.adminHome() ] )
        button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def adminModStudent(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Modify Student", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        label = tk.Label(self.frame2, text="Enter the ID of the user that you would like to edit")
        label.pack()
        entry = tk.Entry(self.frame2)
        entry.pack()
        label = tk.Label(self.frame2, text="Enter the number associated with the feature you would like to change")
        label.pack()
        label = tk.Label(self.frame2, text="(1) ID, (2) Firstname, (3) Lastname, (4) Title, (5) Office, (6) Email")
        label.pack()
        entry2 = tk.Entry(self.frame2)
        entry2.pack()
        label = tk.Label(self.frame2, text="New Value")
        label.pack()
        entry3 = tk.Entry(self.frame2)
        entry3.pack()
        button = tk.Button(self.frame2, text = "Continue", command =lambda: [Admin.modUserAdmin(self, entry.get() ,entry2.get(), entry3.get(), ), self.adminHome() ] )
        button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def adminModAdmin(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Modify Student", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        label = tk.Label(self.frame2, text="Enter the ID of the user that you would like to edit")
        label.pack()
        entry = tk.Entry(self.frame2)
        entry.pack()
        label = tk.Label(self.frame2, text="Enter the number associated with the feature you would like to change")
        label.pack()
        label = tk.Label(self.frame2, text="(1) ID, (2) Firstname, (3) Lastname, (4) Title, (5) Office, (6) Email")
        label.pack()
        entry2 = tk.Entry(self.frame2)
        entry2.pack()
        label = tk.Label(self.frame2, text="New Value")
        label.pack()
        entry3 = tk.Entry(self.frame2)
        entry3.pack()
        button = tk.Button(self.frame2, text = "Continue", command =lambda: [Admin.modUserAdmin(self, entry.get() ,entry2.get(), entry3.get(), ), self.adminHome() ] )
        button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def adminModStudent2(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        admin_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        admin_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Add Course", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        self.button = tk.Radiobutton(self.frame2, text= "ID Number", value=1)
        self.button.pack()
        self.button = tk.Radiobutton(self.frame2, text= "First Name", value= 2)
        self.button.pack()
        self.button = tk.Radiobutton(self.frame2, text="Last Name", value =3 )
        self.button.pack()
        self.button = tk.Radiobutton(self.frame2, text="Title", value=4)
        self.button.pack()
        self.button = tk.Radiobutton(self.frame2, text="Office", value =5)
        self.button.pack()
        self.button = tk.Radiobutton(self.frame2, text="Email", value=6)
        self.button.pack()
        self.button = tk.Radiobutton(self.frame2, text="Last Name", value=7)
        self.button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def courseAdd(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        admin_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        admin_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Add Course", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        label = tk.Label(self.frame2, text= "CRN: ")
        label.pack()
        CRN = tk.Entry(self.frame2)
        CRN.pack()
        label = tk.Label(self.frame2, text="Title: ")
        label.pack()
        title = tk.Entry(self.frame2)
        title.pack()
        label = tk.Label(self.frame2, text="Department: ")
        label.pack()
        dept = tk.Entry(self.frame2)
        dept.pack()
        label = tk.Label(self.frame2, text="Time: ")
        label.pack()
        time = tk.Entry(self.frame2)
        time.pack()
        label = tk.Label(self.frame2, text="Days: ")
        label.pack()
        days = tk.Entry(self.frame2)
        days.pack()
        label = tk.Label(self.frame2, text="Semester: ")
        label.pack()
        semester = tk.Entry(self.frame2)
        semester.pack()
        label = tk.Label(self.frame2, text="Year: ")
        label.pack()
        Year = tk.Entry(self.frame2)
        Year.pack()
        label = tk.Label(self.frame2, text="Credit Num: ")
        label.pack()
        credit_num = tk.Entry(self.frame2)
        credit_num.pack()
        button = tk.Button(self.frame2, text="Add Course", command=lambda:[Admin.addRemoveCourse(self, True, CRN.get(), title.get(),dept.get(),time.get(), days.get(), semester.get(),Year.get(), credit_num.get(), 0),self.adminHome()])
        button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")


    def courseRem(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        admin_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        admin_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Remove Course", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        label = tk.Label(self.frame2, text="Enter the CRN of the Course You want to Remove")
        label.pack()
        CRN = tk.Entry(self.frame2)
        CRN.pack()

        button = tk.Button(self.frame2, text="Remove Course", command=lambda: [Admin.addRemoveCourse(self, False,0,0,0,0,0,0,0,0, CRN.get()), self.adminHome()])
        button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def adminNewStudent(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Add New Student", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        #ID, first_name, last_name, expectedgradyear, major, email
        label = tk.Label(self.frame2, text="ID")
        label.pack()
        ID = tk.Entry(self.frame2)
        ID.pack()
        label = tk.Label(self.frame2, text="First Name")
        label.pack()
        first = tk.Entry(self.frame2)
        first.pack()
        label = tk.Label(self.frame2, text="Last Name")
        label.pack()
        last = tk.Entry(self.frame2)
        last.pack()
        label = tk.Label(self.frame2, text="Graduation Year")
        label.pack()
        year = tk.Entry(self.frame2)
        year.pack()
        label = tk.Label(self.frame2, text="Major")
        label.pack()
        major = tk.Entry(self.frame2)
        major.pack()
        label = tk.Label(self.frame2, text="Email")
        label.pack()
        email = tk.Entry(self.frame2)
        email.pack()

        button = tk.Button(self.frame2, text= "Add New Student",command=lambda:[admin.new_student(ID.get(), first.get(), last.get(), year.get(), major.get(), email.get()), self.adminHome()])
        button.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue2_bar.pack(fill="x")


# Goes to the Page to print all the courses in the database
    def adminRoster(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)


        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Roster", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        cursor.execute("""SELECT * FROM courses""")
        course_info = cursor.fetchall()
        x = 1
        for row in course_info:
            self.label = tk.Label(self.frame2, text = row)
            self.label.pack()
            print(row)
            x +=1

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue2_bar.pack(fill="x")


    def studentHome(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame3 = Frame(self.master)
        self.frame3.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame3, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame3)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        financial_aid_btn = Button(button_frame, text="Financial Aid", bg="grey", command=lambda: self.financial())
        financial_aid_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame3, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame3, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame3, text="Main Menu", command=lambda: self.studentHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame3, text="Main Menu", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame3, bg="#%02x%02x%02x" %(204,204,0), height=3)
        yellow_bar.pack(fill="x")

        personal_info_btn_bottom = Button(self.frame3, text="Personal Information", command=lambda: self.studentPersonalInfo())
        personal_info_btn_bottom.pack(anchor="w", padx=3, pady=2)
        personal_info_txt = "Update addresses, contact information or marital status; review name or social security number change information; Customize your directory profile."
        text_widget = tk.Label(self.frame3, text=personal_info_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0, 5), anchor="w")

        student_btn_bottom = Button(self.frame3, text="Student", command=lambda: self.student())
        student_btn_bottom.pack(anchor="w", padx=3, pady=2)
        student_txt = "Apply for Admission, Register and View your academic records."
        text_widget = tk.Label(self.frame3, text=student_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0,5), anchor="w")

        financial_aid_btn_bottom = Button(self.frame3, text="Financial Aid", command=lambda: self.financial())
        financial_aid_btn_bottom.pack(anchor="w", padx=3, pady=2)
        financial_aid_txt = "View Financial Aid Information."
        text_widget = tk.Label(self.frame3, text=financial_aid_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0, 5), anchor="w")

        blue2_bar = tk.Frame(self.frame3, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")


    def instructorHome(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.instructorPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.instructorHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Main Menu", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        personal_info_btn_bottom = Button(self.frame2, text="Personal Information", command=lambda: self.instructorPersonalInfo())
        personal_info_btn_bottom.pack(anchor="w", padx=3, pady=2)
        personal_info_txt = "Update addresses, contact information or marital status; review name or social security number change information; Customize your directory profile."
        text_widget = tk.Label(self.frame2, text=personal_info_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0, 5), anchor="w")

        instructor_btn_bottom = Button(self.frame2, text="Instructor", command=lambda: self.instructor())
        instructor_btn_bottom.pack(anchor="w", padx=3, pady=2)
        instructor_txt = "View schedule, Search courses, Print course roster."
        text_widget = tk.Label(self.frame2, text=instructor_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0,5), anchor="w")

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def instructor(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.instructorPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        home_btn = Button(self.frame2, text="Main Menu", command=lambda: self.instructorHome())
        home_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Instructor Menu", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        print_schedule_btn = Button(self.frame2, text="Print Schedule", command=lambda: self.instructorHome())
        print_schedule_btn.pack()

        print_roster_btn = Button(self.frame2, text="Print Class List", command=lambda: self.instructorHome())
        print_roster_btn.pack()

        search_course_btn = Button(self.frame2, text="Search Course", command=lambda: self.instructorHome())
        search_course_btn.pack()

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def register(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Register", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")


    def studentRecords(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Student Records", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        transcript_btn = Button(self.frame2, text="Academic Transcript", command=lambda: self.transcriptOptions())
        transcript_btn.pack(anchor="w", padx=3, pady=2)

        acc_sum_btn = Button(self.frame2, text="Account Summary", command=lambda: self.studentUnfinishedPage())
        acc_sum_btn.pack(anchor="w", padx=3, pady=2)

        acc_sum_term_btn = Button(self.frame2, text="Account Summary by Term", command=lambda: self.studentUnfinishedPage())
        acc_sum_term_btn.pack(anchor="w", padx=3, pady=2)

        course_search_btn = Button(self.frame2, text="Course Section Search", command=lambda: self.courseSectionSearch())
        course_search_btn.pack(anchor="w", padx=3, pady=2)

        deg_audit_btn = Button(self.frame2, text="Degree Audit", command=lambda: self.studentUnfinishedPage())
        deg_audit_btn.pack(anchor="w", padx=3, pady=2)

        marks_yacht_btn = Button(self.frame2, text="E-Bill", command=lambda: self.open_marks_toy_window())
        marks_yacht_btn.pack(anchor="w", padx=3, pady=2)

        midterm_grd_btn = Button(self.frame2, text="Midterm Grades", command=lambda: self.studentUnfinishedPage())
        midterm_grd_btn.pack(anchor="w", padx=3, pady=2)

        std_info_btn = Button(self.frame2, text="View Student Information", command=lambda: self.viewStudentInfo())
        std_info_btn.pack(anchor="w", padx=3, pady=2)

        grd_detail_btn = Button(self.frame2, text="Grade Detail", command=lambda: self.studentUnfinishedPage())
        grd_detail_btn.pack(anchor="w", padx=3, pady=2)

        course_catalog_btn = Button(self.frame2, text="Course Catalog", command=lambda: self.courseCatalog())
        course_catalog_btn.pack(anchor="w", padx=3, pady=2)

        acc_detail_term_btn = Button(self.frame2, text="Account Detail for Term", command=lambda: self.studentUnfinishedPage())
        acc_detail_term_btn.pack(anchor="w", padx=3, pady=2)

        app_for_grad_btn = Button(self.frame2, text="Application for Graduation", command=lambda: self.studentUnfinishedPage())
        app_for_grad_btn.pack(anchor="w", padx=3, pady=2)

        view_diploma_name = Button(self.frame2, text="View Diploma Name", command=lambda: self.studentUnfinishedPage())
        view_diploma_name.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")


    def transcriptOptions(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.reg_txt2 = tk.Label(self.frame5, text='Transcript Options')
        self.reg_txt2.pack()
        variable1 = StringVar(self.master)
        variable1.set(TRANSCRIPTOPTIONBOX1[0])
        self.login_btn = OptionMenu(self.frame5, variable1, *TRANSCRIPTOPTIONBOX1)
        self.login_btn.pack()
        variable2 = StringVar(self.master)
        variable2.set(TRANSCRIPTOPTIONBOX2[0])
        self.login_btn = OptionMenu(self.frame5, variable2, *TRANSCRIPTOPTIONBOX2)
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame5, text="Submit", command=lambda: self.studentUnfinishedPage())
        self.login_btn.pack()

    def courseCatalog(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Course Section Search", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        coursesCur.execute("SELECT DISTINCT term FROM courses")
        result = coursesCur.fetchall()

        semester_term_list = [term[0] for term in result]

        selected_term = tk.StringVar(self.frame2, semester_term_list[0])

        semester_year_label = tk.Label(self.frame2, text="Select a Term for Class Search:")
        semester_year_label.pack(anchor="w", padx=3, pady=10)

        semester_year_dropdown = tk.OptionMenu(self.frame2, selected_term, *semester_term_list)
        semester_year_dropdown.pack(anchor="w", padx=3)

        coursesCur.execute("SELECT DISTINCT subject FROM courses")
        result_subjects = coursesCur.fetchall()
        subject_list = [subject[0] for subject in result_subjects]
        selected_subject = tk.StringVar(self.frame2, subject_list[0])
        subject_label = tk.Label(self.frame2, text="Select a Subject:")
        subject_label.pack(anchor="w", padx=3, pady=10)
        subject_dropdown = tk.OptionMenu(self.frame2, selected_subject, *subject_list)
        subject_dropdown.pack(anchor="w", padx=3)

        search_btn = Button(self.frame2, text="Submit", command=lambda: self.display_catalog(selected_term.get(), selected_subject.get()))
        search_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue2_bar.pack(fill="x")

    def display_catalog(self, term, subject):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)
        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Course Section Search", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        coursesCur.execute("SELECT * FROM courses WHERE term = ? AND subject = ?", (term, subject))
        data = coursesCur.fetchall()

        tree = ttk.Treeview(self.frame2)
        tree["columns"] = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("#1", anchor=tk.W)
        tree.column("#2", anchor=tk.W)
        tree.column("#3", anchor=tk.W)
        tree.column("#4", anchor=tk.W)
        tree.column("#5", anchor=tk.W)
        tree.column("#6", anchor=tk.W)
        tree.column("#7", anchor=tk.W)
        tree.column("#8", anchor=tk.W)
        tree.heading("#1", text="CRN")
        tree.heading("#2", text="Subject")
        tree.heading("#3", text="Course Number")
        tree.heading("#4", text="Section Number")
        tree.heading("#5", text="Title")
        tree.heading("#6", text="Term")
        tree.heading("#7", text="Type")
        tree.heading("#8", text="Credit Hours")

        for row in data:
            tree.insert("", tk.END, values=row)

        tree.pack()

        back_btn = Button(self.frame2, text="Go Back To Search", command=lambda: self.courseCatalog())
        back_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue2_bar.pack(fill="x")

    def viewStudentInfo(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def courseSectionSearch(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Course Section Search", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        coursesCur.execute("SELECT DISTINCT term FROM courses")
        result = coursesCur.fetchall()

        semester_term_list = [term[0] for term in result]

        selected_term = tk.StringVar(self.frame2, semester_term_list[0])

        semester_year_label = tk.Label(self.frame2, text="Select a Term for Class Search:")
        semester_year_label.pack(anchor="w", padx=3, pady=10)

        semester_year_dropdown = tk.OptionMenu(self.frame2, selected_term, *semester_term_list)
        semester_year_dropdown.pack(anchor="w", padx=3)

        crn_label = tk.Label(self.frame2, text="Enter CRN:")
        crn_label.pack(anchor="w", padx=3, pady=10)
        crn_entry = tk.Entry(self.frame2)
        crn_entry.pack(anchor="w", padx=3, pady=10)

        search_btn = Button(self.frame2, text="Submit", command=lambda: self.display_course(selected_term.get(), crn_entry.get()))
        search_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue2_bar.pack(fill="x")

    def display_course(self, term, crn):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Course Search Results", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        coursesCur.execute("SELECT * FROM courses WHERE term = ? AND crn = ?", (term, crn))
        data = coursesCur.fetchone()

        tree = ttk.Treeview(self.frame2)
        tree["columns"] = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("#1", anchor=tk.W)
        tree.column("#2", anchor=tk.W)
        tree.column("#3", anchor=tk.W)
        tree.column("#4", anchor=tk.W)
        tree.column("#5", anchor=tk.W)
        tree.column("#6", anchor=tk.W)
        tree.column("#7", anchor=tk.W)
        tree.column("#8", anchor=tk.W)
        tree.heading("#1", text="CRN")
        tree.heading("#2", text="Subject")
        tree.heading("#3", text="Course Number")
        tree.heading("#4", text="Section Number")
        tree.heading("#5", text="Title")
        tree.heading("#6", text="Term")
        tree.heading("#7", text="Type")
        tree.heading("#8", text="Credit Hours")

        tree.insert("", tk.END, values=data)

        tree.pack()

        back_btn = Button(self.frame2, text="Go Back To Search", command=lambda: self.courseCatalog())
        back_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue2_bar.pack(fill="x")

    def reg_and_planning(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Registration and Planning", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        course_search_btn = Button(self.frame2, text="Course Section Search",
                                   command=lambda: self.courseSectionSearch())
        course_search_btn.pack(anchor="w", padx=3, pady=2)

        course_catalog_btn = Button(self.frame2, text="Course Catalog", command=lambda: self.courseCatalog())
        course_catalog_btn.pack(anchor="w", padx=3, pady=2)

        reg_btn = Button(self.frame2, text="Register for Course", command=lambda: self.register())
        reg_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def financial(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Financial Aid", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        financial_status_btn = Button(self.frame2, text="Financial Aid Status", command=lambda: self.studentUnfinishedPage())
        financial_status_btn.pack(anchor="w", padx=3, pady=2)

        elegibility_btn = Button(self.frame2, text="Eligibility", command=lambda: self.studentUnfinishedPage())
        elegibility_btn.pack(anchor="w", padx=3, pady=2)

        aid_pkg_btn = Button(self.frame2, text="Financial Aid Package", command=lambda: self.studentUnfinishedPage())
        aid_pkg_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def student(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Student Records", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        reg_plan_btn = Button(self.frame2, text="Registration and Planning", command=lambda: self.reg_and_planning())
        reg_plan_btn.pack(anchor="w", padx=3, pady=2)

        marks_yacht_btn = Button(self.frame2, text="E-Bill", command=lambda: self.open_marks_toy_window())
        marks_yacht_btn.pack(anchor="w", padx=3, pady=2)

        online_payment_btn = Button(self.frame2, text="Online Payment Central", command=lambda: self.studentUnfinishedPage())
        online_payment_btn.pack(anchor="w", padx=3, pady=2)

        manage_ref_btn = Button(self.frame2, text="Manage Your Refund Preferences", command=lambda: self.studentUnfinishedPage())
        manage_ref_btn.pack(anchor="w", padx=3, pady=2)

        std_rec_btn = Button(self.frame2, text="Student Records", command=lambda: self.studentRecords())
        std_rec_btn.pack(anchor="w", padx=3, pady=2)

        booknow_btn = Button(self.frame2, text="BookNow", command=self.open_booknow_window)
        booknow_btn.pack(anchor="w", padx=3, pady=2)

        some_form_web_btn = Button(self.frame2, text="1098-T Form Website", command=self.open_form_window)
        some_form_web_btn.pack(anchor="w", padx=3, pady=2)

        alumni_btn = Button(self.frame2, text="NSC Alumni MyHub", command=self.open_alumni_window)
        alumni_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def open_booknow_window(self):
        webview.create_window('BookNow', 'http://thewitshop.com')
        webview.start()

    def open_form_window(self):
        webview.create_window('1098-T Form', 'https://tra.maximus.com/')
        webview.start()

    def open_alumni_window(self):
        webview.create_window('Alumni Hub', 'https://tra.maximus.com/')
        webview.start()

    def open_marks_toy_window(self):
        webview.create_window('Marks Yacht', 'https://www.yachtworld.com/yacht/2023-doerries-90m-6192006/')
        webview.start()

    def studentPersonalInfo(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame5 = Frame(self.master)
        self.frame5.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame5, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame5)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame5, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        menu_btn = Button(self.frame5, text="Main Menu", command=lambda: self.studentHome())
        menu_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame5, text="Personal Information", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        name_chng_btn = Button(self.frame5, text="Name Change Information", command=lambda: self.studentUnfinishedPage())
        name_chng_btn.pack(anchor="w", padx=3, pady=2)

        social_chng_btn = Button(self.frame5, text="Social Security Number Change Information", command=lambda: self.studentUnfinishedPage())
        social_chng_btn.pack(anchor="w", padx=3, pady=2)

        ferpa_btn = Button(self.frame5, text="Directory Listing Opt-Out (FERPA)", command=lambda: self.studentUnfinishedPage())
        ferpa_btn.pack(anchor="w", padx=3, pady=2)

        add_gend_btn = Button(self.frame5, text="Additional Gender Information", command=lambda: self.studentUnfinishedPage())
        add_gend_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")


    def instructorPersonalInfo(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame5 = Frame(self.master)
        self.frame5.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame5, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame5)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructorHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame5, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        menu_btn = Button(self.frame5, text="Main Menu", command=lambda: self.instructorHome())
        menu_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame5, text="Personal Information", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        name_chng_btn = Button(self.frame5, text="Name Change Information", command=lambda: self.instructorUnfinishedPage())
        name_chng_btn.pack(anchor="w", padx=3, pady=2)

        social_chng_btn = Button(self.frame5, text="Social Security Number Change Information", command=lambda: self.instructorUnfinishedPage())
        social_chng_btn.pack(anchor="w", padx=3, pady=2)

        ferpa_btn = Button(self.frame5, text="Directory Listing Opt-Out (FERPA)", command=lambda: self.instructorUnfinishedPage())
        ferpa_btn.pack(anchor="w", padx=3, pady=2)

        add_gend_btn = Button(self.frame5, text="Additional Gender Information", command=lambda: self.instructorUnfinishedPage())
        add_gend_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def studentUnfinishedPage(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.studentPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        menu_btn = Button(self.frame2, text="Main Menu", command=lambda: self.studentHome())
        menu_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Page Under Construction", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        construction_label = tk.Label(self.frame2, text="Page Under Construction!", font=("Roboto", 16))
        construction_label.pack(pady=5)

        menu_low_btn = Button(self.frame2, text="Go Back to Main Menu", font=("Roboto", 12), command=lambda: self.studentHome())
        menu_low_btn.pack(pady=10)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")


    def instructorUnfinishedPage(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        personal_info_btn = Button(button_frame, text="Personal Information", bg="grey",
                                   command=lambda: self.instructorPersonalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        menu_btn = Button(self.frame2, text="Main Menu", command=lambda: self.instructorHome())
        menu_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Page Under Construction", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        construction_label = tk.Label(self.frame2, text="Page Under Construction!", font=("Roboto", 16))
        construction_label.pack(pady=5)

        menu_low_btn = Button(self.frame2, text="Go Back to Main Menu", font=("Roboto", 12), command=lambda: self.instructorHome())
        menu_low_btn.pack(pady=10)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

    def adminUnfinishedPage(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        banner_image = Image.open("banner.png")
        self.banner = ImageTk.PhotoImage(banner_image)
        banner_label = tk.Label(self.frame2, image=self.banner)
        banner_label.pack(anchor="nw")

        button_frame = tk.Frame(self.frame2)
        button_frame.pack(fill="x", padx=10)

        student_btn = Button(button_frame, text="Admin", bg="grey", command=lambda: self.adminHome())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        menu_btn = Button(self.frame2, text="Main Menu", command=lambda: self.adminHome())
        menu_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame2, text="Page Under Construction", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)

        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        construction_label = tk.Label(self.frame2, text="Page Under Construction!", font=("Roboto", 16))
        construction_label.pack(pady=5)

        menu_low_btn = Button(self.frame2, text="Go Back to Main Menu", font=("Roboto", 12), command=lambda: self.adminHome())
        menu_low_btn.pack(pady=10)

        blue2_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

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
            self.adminHome()
            print(admin_data)
            Admin(admin_data[0],admin_data[1],admin_data[2],admin_data[3],admin_data[4],admin_data[5])

            return Admin(*admin_data)
        elif instructor_data:
            print("Welcome, Instructor!")
            access_granted = True
            self.instructorHome()
            print(instructor_data)
            instructor(instructor_data[0],instructor_data[1],instructor_data[2],instructor_data[3],instructor_data[4],instructor_data[5],instructor_data[6])

            return instructor(*instructor_data)
        elif student_data:
            print("Welcome, Student!")
            access_granted = True
            loggedinUser = student(*student_data)
            print(student_data)
            student(student_data[0], student_data[1],student_data[2],student_data[3],student_data[4],student_data[5])
            self.studentHome()
            return student(*student_data)

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