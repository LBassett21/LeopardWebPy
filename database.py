import sqlite3

# creates sql database called web.db
db = sqlite3.connect("web.db")

cursor = db.cursor()

def create_tables():
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


setID = 10000
setType = "Admin"
setFN = "Admin"
setLN = "Admin"
setEmail = "AdminA"
setPW = "Password"

#cursor.execute("""INSERT INTO users (ID, TYPE, FN, LN, EMAIL, PASSWORD) VALUES (?,?,?,?,?,?)""",(setID, setType, setFN, setLN, setEmail, setPW))
#db.commit()

def print_users():
    cursor.execute("""SELECT * FROM users""")
    user_info = cursor.fetchall()
    for user in user_info:
        print(user)