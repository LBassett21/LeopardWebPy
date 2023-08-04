import tkinter as tk
from tkinter import Label
from tkinter import *
from PIL import ImageTk,Image
import webview
# import database
import sqlite3

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
        entry2 = Entry(white_frame, width=40, font=("Arial", 12))
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

        self.frame2 = tk.Frame(self.master)
        self.frame2.pack(fill=tk.BOTH, expand=True)

        ban_image = Image.open("banner.png")
        self.ban = ImageTk.PhotoImage(ban_image)
        ban_label = tk.Label(self.frame2, image=self.ban)
        ban_label.place(x=0, y=0, relwidth=1, relheight=1)

        #self.frame2 = Frame(self.master, width=300, height=300)
        #self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='Admin Homepage')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Go to Login", command=lambda: self.login())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Print Course Roster", command=lambda: self.adminRoster())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Add/Remove User", command=lambda: self.adminNewStudent())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Add Course", command=lambda: self.courseAdd())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Remove Course", command=lambda: self.courseRem())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Modify A User", command=lambda: Admin.modifyUser(self))
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame2, text="Print All Users", command=lambda: admin.print_database())
        self.login_btn.pack()

    def adminModStudent(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        label = tk.Label(self.frame2, text="Enter the ID of the user that you would like to edit")
        label.pack()
        entry = tk.Entry(self.frame2)
        entry.pack()
        button = tk.Button(self.frame2, text = "Continue", command =lambda: [Admin.modUserAdmin(self, entry.get()), self.adminModStudent2()] )
        button.pack()

    def adminModStudent2(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.label = tk.Label(self.frame2, text = "")
        self.button = tk.Radiobutton(text= "ID Number", value=1)
        self.button.pack()
        self.button = tk.Radiobutton(text= "First Name", value= 2)
        self.button.pack()
        self.button = tk.Radiobutton(text="Last Name", value =3 )
        self.button.pack()
        self.button = tk.Radiobutton(text="Title", value=4)
        self.button.pack()
        self.button = tk.Radiobutton(text="Office", value =5)
        self.button.pack()
        self.button = tk.Radiobutton(text="Email", value=6)
        self.button.pack()
        self.button = tk.Radiobutton(text="Last Name", value=7)
        self.button.pack()

    def courseAdd(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='~~~~Add Course~~~~')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Home", command=lambda: self.adminHome())
        self.login_btn.pack()

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
    def courseRem(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='~~~~Remove Course~~~~')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Home", command=lambda: self.adminHome())
        self.login_btn.pack()
        label = tk.Label(self.frame2, text = "Enter the CRN of the Course You want to Remove")
        label.pack()
        CRN = tk.Entry(self.frame2)
        CRN.pack()

        button = tk.Button(self.frame2, text="Remove Course", command=lambda: [Admin.addRemoveCourse(self, False,0,0,0,0,0,0,0,0, CRN.get()), self.adminHome()])
        button.pack()

    def adminNewStudent(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='~~~~New Student~~~~')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Home", command=lambda: self.adminHome())
        self.login_btn.pack()
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


# Goes to the Page to print all the courses in the database
    def adminRoster(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.login_btn = tk.Button(self.frame2, text="Home", command=lambda: self.adminHome())
        self.login_btn.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='~~~~Courses~~~~')
        self.reg_txt2.pack()

        cursor.execute("""SELECT * FROM courses""")
        course_info = cursor.fetchall()
        x = 1
        for row in course_info:
            self.label = tk.Label(self.frame2, text = row)
            self.label.pack()
            print(row)
            x +=1


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
                                   command=lambda: self.personalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Student", bg="grey", command=lambda: self.student())
        student_btn.pack(side="left")

        financial_aid_btn = Button(button_frame, text="Financial Aid", bg="grey", command=lambda: self.financial())
        financial_aid_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame3, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame3, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        main_menu_label = tk.Label(self.frame3, text="Main Menu", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame3, bg="#%02x%02x%02x" %(204,204,0), height=3)
        yellow_bar.pack(fill="x")

        personal_info_btn_bottom = Button(self.frame3, text="Personal Information", command=lambda: self.personalInfo())
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
                                   command=lambda: self.personalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame2, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        main_menu_label = tk.Label(self.frame2, text="Main Menu", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame2, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        personal_info_btn_bottom = Button(self.frame2, text="Personal Information", command=lambda: self.personalInfo())
        personal_info_btn_bottom.pack(anchor="w", padx=3, pady=2)
        personal_info_txt = "Update addresses, contact information or marital status; review name or social security number change information; Customize your directory profile."
        text_widget = tk.Label(self.frame2, text=personal_info_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0, 5), anchor="w")

        instructor_btn_bottom = Button(self.frame2, text="Instructor", command=lambda: self.instructor())
        instructor_btn_bottom.pack(anchor="w", padx=3, pady=2)
        instructor_txt = "Apply for Admission, Register and View your academic records."
        text_widget = tk.Label(self.frame2, text=instructor_txt, font=("Roboto", 8))
        text_widget.pack(pady=(0,5), anchor="w")

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
                                   command=lambda: self.personalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
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
                                   command=lambda: self.personalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
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

        acc_sum_btn = Button(self.frame2, text="Account Summary", command=lambda: self.accountSummary())
        acc_sum_btn.pack(anchor="w", padx=3, pady=2)

        acc_sum_term_btn = Button(self.frame2, text="Account Summary by Term", command=lambda: self.accountSummaryByTerm())
        acc_sum_term_btn.pack(anchor="w", padx=3, pady=2)

        course_search_btn = Button(self.frame2, text="Course Section Search", command=lambda: self.courseSectionSearch())
        course_search_btn.pack(anchor="w", padx=3, pady=2)

        deg_audit_btn = Button(self.frame2, text="Degree Audit", command=lambda: self.degreeAudit())
        deg_audit_btn.pack(anchor="w", padx=3, pady=2)

        marks_yacht_btn = Button(self.frame2, text="E-Bill", command=lambda: self.markysYachtFund())
        marks_yacht_btn.pack(anchor="w", padx=3, pady=2)

        midterm_grd_btn = Button(self.frame2, text="Midterm Grades", command=lambda: self.midtermGrades())
        midterm_grd_btn.pack(anchor="w", padx=3, pady=2)

        std_info_btn = Button(self.frame2, text="View Student Information", command=lambda: self.viewStudentInfo())
        std_info_btn.pack(anchor="w", padx=3, pady=2)

        grd_detail_btn = Button(self.frame2, text="Grade Detail", command=lambda: self.gradeDetail())
        grd_detail_btn.pack(anchor="w", padx=3, pady=2)

        course_catalog_btn = Button(self.frame2, text="Course Catalog", command=lambda: self.courseCatalog())
        course_catalog_btn.pack(anchor="w", padx=3, pady=2)

        acc_detail_term_btn = Button(self.frame2, text="Account Detail for Term", command=lambda: self.accountDetailForTerm())
        acc_detail_term_btn.pack(anchor="w", padx=3, pady=2)

        app_for_grad_btn = Button(self.frame2, text="Application for Graduation", command=lambda: self.appForGrad())
        app_for_grad_btn.pack(anchor="w", padx=3, pady=2)

        view_diploma_name = Button(self.frame2, text="View Diploma Name", command=lambda: self.viewDiplomaName())
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
        self.login_btn = tk.Button(self.frame5, text="Submit", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def accountSummary(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def accountSummaryByTerm(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def courseSectionSearch(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def degreeAudit(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def markysYachtFund(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def midtermGrades(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def viewHolds(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def viewStudentInfo(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def gradeDetail(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def courseCatalog(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def accountDetailForTerm(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def appForGrad(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
        self.login_btn.pack()

    def viewDiplomaName(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        self.login_btn = tk.Button(self.frame5, text="Go back", command=lambda: self.studentRecords())
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
        self.login_btn.pack(side=LEFT, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Personal Information", command=lambda: self.personalInfo())
        self.login_btn.pack(side=LEFT, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Student", command=lambda: self.student())
        self.login_btn.pack(side=LEFT, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Financial Aid Status", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Eligibility", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)

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
        self.login_btn.pack(side=LEFT, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Personal Information", command=lambda: self.personalInfo())
        self.login_btn.pack(side=LEFT, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Financial Aid", command=lambda: self.financial())
        self.login_btn.pack(side=LEFT, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Registration and Planning", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="E-Bill", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Online Payment Central", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Manage Your Refund Preferences", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="Student Records", command=lambda: self.studentRecords())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.login_btn = tk.Button(self.frame5, text="BookNow", command=lambda: self.home())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        webview.create_window('1098-T Form', 'https://tra.maximus.com/')
        self.login_btn = tk.Button(self.frame5, text="1098-T Form Website", command=lambda: webview.start())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)
        webview.create_window('Alumni Hub', 'https://tra.maximus.com/')
        self.login_btn = tk.Button(self.frame5, text="NSC Alumni MyHub", command=lambda: webview.start())
        self.login_btn.pack(side=BOTTOM, expand=True, fill=BOTH)

    def instructor(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame6 = Frame(self.master, width=300, height=300)
        self.frame6.pack()
        self.reg_txt2 = tk.Label(self.frame6, text='Instructor Information')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame6, text="Print Schedule", command=lambda: self.instructorHome())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame6, text="Print Class List", command=lambda: self.instructorHome())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame6, text="Search Course", command=lambda: self.instructorHome())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame6, text="Add / Drop Course", command=lambda: self.instructorHome())
        self.login_btn.pack()
        self.login_btn = tk.Button(self.frame6, text="Go to home", command=lambda: self.instructorHome())
        self.login_btn.pack()


    def personalInfo(self):
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
                                   command=lambda: self.personalInfo())
        personal_info_btn.pack(side="left")

        student_btn = Button(button_frame, text="Instructor", bg="grey", command=lambda: self.instructor())
        student_btn.pack(side="left")

        blue_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" % (0, 51, 102), height=2)
        blue_bar.pack(fill="x")

        exit_btn = Button(self.frame5, text="EXIT", command=lambda: self.login())
        exit_btn.pack(anchor="e", padx=10, pady=10)

        exit_btn = Button(self.frame5, text="Main Menu", command=lambda: self.studentHome())
        exit_btn.pack(anchor="e", padx=10)

        main_menu_label = tk.Label(self.frame5, text="Personal Information", font=("Roboto", 16))
        main_menu_label.pack(anchor="w", padx=3, pady=15)
        yellow_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" % (204, 204, 0), height=3)
        yellow_bar.pack(fill="x")

        name_chng_btn = Button(self.frame5, text="Name Change Information", command=lambda: self.home())
        name_chng_btn.pack(anchor="w", padx=3, pady=2)

        social_chng_btn = Button(self.frame5, text="Social Security Number Change Information", command=lambda: self.home())
        social_chng_btn.pack(anchor="w", padx=3, pady=2)

        ferpa_btn = Button(self.frame5, text="Directory Listing Opt-Out (FERPA)", command=lambda: self.home())
        ferpa_btn.pack(anchor="w", padx=3, pady=2)

        add_gend_btn = Button(self.frame5, text="Additional Gender Information", command=lambda: self.home())
        add_gend_btn.pack(anchor="w", padx=3, pady=2)

        blue2_bar = tk.Frame(self.frame5, bg="#%02x%02x%02x" %(0,51,102), height=2)
        blue2_bar.pack(fill="x")

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