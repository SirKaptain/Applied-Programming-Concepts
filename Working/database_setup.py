from database_functions import *
import random
import string
import pandas as pd


# create a database connection
conn = create_connection('./Working/database.db') 

#removing tables if already exists
def remove_all_tables(conn):
    remove_table(conn, "LOGIN")
    remove_table(conn, "STUDENT")
    remove_table(conn, "INSTRUCTOR")
    remove_table(conn, "ADMIN")
    remove_table(conn, "COURSES")
    remove_table(conn, "SCHEDULE")

#creating necessary tables
def setup_all_tables(conn):
    create_table(conn, "LOGIN", "ID text primary key, PASSWORD text")
    create_table(conn, "STUDENT", "ID text primary key, NAME text, SURNAME text, GRADYEAR int, MAJOR char(4), EMAIL text")
    create_table(conn, "INSTRUCTOR", "ID text primary key, NAME text, SURNAME text, TITLE text, HIREYEAR int, DEPT char(4), EMAIL text")
    create_table(conn, "ADMIN", "ID text primary key, NAME text, SURNAME text, TITLE text, OFFICE text, EMAIL text")
    create_table(conn, "COURSES", "CRN int primary key, TITLE text, DEPT text, START_TIME text, END_TIME text, DAYS_OF_WEEK text, SEMESTER text, YEAR int, CREDITS int, INSTRUCTOR_ID text, FOREIGN KEY (INSTRUCTOR_ID) REFERENCES INSTRUCTOR(ID)")

    #creating many-to-many mapping table for student schedules (one student belongs to many courses, and one course belongs to many students)
    create_table(conn, "SCHEDULE", "STUDENT_ID text, COURSE_ID text, FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT(ID), FOREIGN KEY(COURSE_ID) REFERENCES COURSES(CRN)")

#initially populate the students table from a .csv file
def populate_students(conn):
    data = pd.read_csv ('./Working/initial_student_table.csv')   
    df = pd.DataFrame(data)
    cur = conn.cursor()
    for row in df.itertuples():
        cur.execute("INSERT INTO STUDENT (ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL) VALUES ('{}','{}','{}','{}','{}','{}')".format(row.ID, row.NAME, row.SURNAME, row.GRADYEAR, row.MAJOR, row.EMAIL))

#initially populate the instructor table from a .csv file
def populate_instructors(conn):
    data = pd.read_csv ('./Working/initial_instructor_table.csv')   
    df = pd.DataFrame(data)
    cur = conn.cursor()
    for row in df.itertuples():
        cur.execute("INSERT INTO INSTRUCTOR (ID, NAME, SURNAME, TITLE, HIREYEAR, DEPT, EMAIL) VALUES ('{}', '{}','{}','{}','{}','{}','{}')".format(row.ID, row.NAME, row.SURNAME, row.TITLE, row.HIREYEAR, row.DEPT, row.EMAIL))

#initially populate the admin table from a .csv file
def populate_admins(conn):
    data = pd.read_csv ('./Working/initial_admin_table.csv')   
    df = pd.DataFrame(data)
    cur = conn.cursor()
    for row in df.itertuples():
        cur.execute("INSERT INTO ADMIN (ID, NAME, SURNAME, TITLE, OFFICE, EMAIL) VALUES ('{}','{}','{}','{}','{}','{}')".format(row.ID, row.NAME, row.SURNAME, row.TITLE, row.OFFICE, row.EMAIL))

#initially populate the courses table from a .csv file
def populate_courses(conn):
    data = pd.read_csv ('./Working/initial_courses_table.csv')   
    df = pd.DataFrame(data)
    cur = conn.cursor()
    for row in df.itertuples():
        cur.execute("INSERT INTO COURSES (CRN, TITLE, DEPT, START_TIME, END_TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row.CRN, row.TITLE, row.DEPT, row.START_TIME, row.END_TIME, row.DAYS_OF_WEEK, row.SEMESTER, row.YEAR, row.CREDITS))

#initially populate the login table from a .csv file
def populate_login(conn):
    data = pd.read_csv ('./Working/initial_login_table.csv')   
    df = pd.DataFrame(data)
    cur = conn.cursor()
    for row in df.itertuples():
        cur.execute("INSERT INTO LOGIN (ID, PASSWORD) VALUES ('{}','{}')".format(row.ID, row.PASSWORD))


remove_all_tables(conn)
setup_all_tables(conn)
populate_students(conn)
populate_instructors(conn)
populate_admins(conn)
populate_courses(conn)
populate_login(conn)
conn.commit()
conn.close()