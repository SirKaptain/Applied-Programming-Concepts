import sqlite3
import os
from sqlite3 import Error

STUDENT = "STUDENT"
INSTRUCTOR = "INSTRUCTOR"
ADMIN = "ADMIN"
ID = "ID"
NAME = "NAME"
SURNAME = "SURNAME"
GRADYEAR = "GRADYEAR"
MAJOR = "MAJOR"
EMAIL = "EMAIL"
TITLE = "TITLE"
HIREYEAR = "HIREYEAR"
DEPT = "DEPT"
OFFICE = "OFFICE"

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


def print_table(conn, table):
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table)
    print(cur.fetchall())

def search_table(conn, table, attribute, value):
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table + " WHERE " + attribute + " = ?", (value,))
    data = cur.fetchall()
    return data

def insert_values(conn, table, attribute, value):
    cur = conn.cursor()
    print("INSERT INTO " + table + " " + attribute + " VALUES (%s, %s, %s, %s, %s, %s)", value)
    cur.execute("INSERT INTO " + table + " " + attribute + " VALUES (?,?,?,?,?,?)", value)


def main():

    # create a database connection
    conn = create_connection('./Dom_Ioime/Code/Python/assignment3.db')
    #create_courses_table(conn)
    print_table(conn, "STUDENT")
    print(search_table(conn, STUDENT, NAME, "Thomas"))
    attributes = (ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL)
    str = ''.join(attributes)
    insert_values(conn, STUDENT, str, "(WOO397674, Dom, Ioime, 2023, BSCO, ioimed)")
    conn.commit()
    conn.close()



if __name__ == '__main__':
    main()