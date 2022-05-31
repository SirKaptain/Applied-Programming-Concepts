import sqlite3
import os
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_courses_table(conn):
    cur = conn.cursor()

    #Doping COURSES table if already exists.
    cur.execute("DROP TABLE IF EXISTS COURSES")

    cur.execute("CREATE TABLE COURSES(CRN text, TITLE text, DEPARTMENT text, TIME text, DAYS_OF_WEEK text, SEMESTER text, YEAR int, CREDITS int)")


def print_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENT")
    print(cur.fetchall())

def print_instructors(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM INSTRUCTOR")
    print(cur.fetchall())

def print_admins(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM ADMIN")
    print(cur.fetchall())

def main():

    # create a database connection
    print(os.getcwd())
    conn = create_connection('./Dom_Ioime/Code/Python/assignment3.db')
    create_courses_table(conn)
    print_students(conn)
    print_instructors(conn)
    print_admins(conn)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    main()