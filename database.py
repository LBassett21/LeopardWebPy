import sqlite3

# creates sql database called web.db
db = sqlite3.connect("web.db")

cursor = db.cursor()
class database():
    def create_tables(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                ID INTEGER PRIMARY KEY,
                TYPE TEXT NOT NULL,
                FN TEXT NOT NULL,
                LN TEXT NOT NULL,
                GRADYR INTEGER,
                TITLE TEXT,
                OFFICE TEXT,
                EMAIL TEXT NOT NULL,
                PASSWORD TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                CRN INTEGER PRIMARY KEY,
                TITLE TEXT NOT NULL,
                TERM TEXT NOT NULL,
                TYPE TEXT NOT NULL,
                SECTION INTEGER NOT NULL,
                SUBJECT TEXT NOT NULL,
                CREDITS INTEGER NOT NULL,
                INSTRUCTOR INTEGER NOT NULL,
                LOCATION TEXT NOT NULL,
                STIME INTEGER NOT NULL,
                ETIME INTEGER NOT NULL,
                DAYS TEXT NOT NULL,
                ENROLLMAX INTEGER NOT NULL,
                ENROLLACT INTEGER NOT NULL
            )
        """)
    def print_users(self):
        cursor.execute("""SELECT * FROM users""")
        user_info = cursor.fetchall()
        for user in user_info:
            print(user)
    def print_courses(self):
        cursor.execute("""SELECT * FROM courses""")
        course_info = cursor.fetchall()
        for course in course_info:
            print(course)
    def add_admin(self, ID, type, fn, ln, title, office, email, pw):
        cursor.execute("""SELECT ID FROM users WHERE ID = ?""", (ID,))
        existing_id = cursor.fetchone()

        if not existing_id:
            cursor.execute("""INSERT INTO users 
            (ID, TYPE, FN, LN, TITLE, OFFICE, EMAIL, PASSWORD) 
            VALUES (?,?,?,?,?,?,?,?)""",
                           (ID, type, fn, ln, title, office, email, pw))
            db.commit()

    def add_instructor(self, ID, type, fn, ln, office, email, pw):
        cursor.execute("""SELECT ID FROM users WHERE ID = ?""", (ID,))
        existing_id = cursor.fetchone()

        if not existing_id:
            cursor.execute("""INSERT INTO users 
            (ID, TYPE, FN, LN, OFFICE, EMAIL, PASSWORD) 
            VALUES (?,?,?,?,?,?,?)""",
                           (ID, type, fn, ln, office, email, pw))
            db.commit()
    def add_student(self, ID, type, fn, ln, gradyr, email, pw):
        cursor.execute("""SELECT ID FROM users WHERE ID = ?""", (ID,))
        existing_id = cursor.fetchone()

        if not existing_id:
            cursor.execute("""INSERT INTO users 
            (ID, TYPE, FN, LN, GRADYR, EMAIL, PASSWORD) 
            VALUES (?,?,?,?,?,?,?)""",
                           (ID, type, fn, ln, gradyr, email, pw))
            db.commit()



setID = 10000
setType = "Admin"
setFN = "Admin"
setLN = "Admin"
setEmail = "AdminA"
setPW = "Password"

#cursor.execute("""INSERT INTO users (ID, TYPE, FN, LN, EMAIL, PASSWORD) VALUES (?,?,?,?,?,?)""",(setID, setType, setFN, setLN, setEmail, setPW))
#db.commit()
