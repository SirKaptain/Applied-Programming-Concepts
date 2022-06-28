import sqlite3
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
COURSES = "COURSES"


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, table, attribute):
    cur = conn.cursor()
    try:
        print("CREATE TABLE {} ({})".format(table, attribute))
        cur.execute("CREATE TABLE {} ({})".format(table, attribute))
    except Error as e:
        print(e)

def remove_table(conn, table):
    cur = conn.cursor()
    try:
        print("DROP TABLE {}".format(table))
        cur.execute("DROP TABLE {}".format(table))
    except Error as e:
        print(e)

def print_table(conn, table):
    cur = conn.cursor()
    try:
        print("SELECT * FROM {}".format(table))
        cur.execute("SELECT * FROM {}".format(table))
        print(cur.fetchall())
    except Error as e:
        print(e)

def search_table(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        print("SELECT * FROM {} WHERE {} = '{}'".format(table, attribute, value))
        cur.execute("SELECT * FROM {} WHERE {} = '{}'".format(table, attribute, value))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

def insert_row(conn, table, attributes, values):
    cur = conn.cursor()
    try:
        print("INSERT INTO {} {} VALUES {}".format(table, attributes, values))
        cur.execute("INSERT INTO {} {} VALUES {}".format(table, attributes, values))
    except Error as e:
        print(e)

def remove_row(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        print("DELETE FROM {} WHERE {} = {}".format(table, attribute, value))
        cur.execute("DELETE FROM {} WHERE {} = {}".format(table, attribute, value))
    except Error as e:
        print(e)

def update_value(conn, table, id, id_value, attribute, new_value):
    cur = conn.cursor()
    try:
        print("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, attribute, new_value, id, id_value))
        cur.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, attribute, new_value, id, id_value))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

def get_table_names(conn):
    list = []
    cur = conn.cursor()
    try:
        print("SELECT name FROM sqlite_master WHERE type='table';")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        for i in tables:
            list.append(i[0])
        return list
    except Error as e:
        print(e)

def get_table_info(conn, table):
    list = []
    cur = conn.cursor()
    try:
        cur.execute("PRAGMA table_info({})".format(table))
        info = cur.fetchall()
        for i in info:
            list.append(i)
        return list
    except Error as e:
        print(e)

def find_matching_instructors(conn):
    cur = conn.cursor()
    print("SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, COURSES.TITLE FROM INSTRUCTOR INNER JOIN COURSES ON INSTRUCTOR.DEPT = COURSES.DEPT")
    cur.execute("SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, COURSES.TITLE FROM INSTRUCTOR INNER JOIN COURSES ON INSTRUCTOR.DEPT = COURSES.DEPT")
    fetch = cur.fetchall()
    print(fetch)

def main():
    # # create a database connection
    conn = create_connection('./Dom_Ioime/Code/Python/assignment3.db') 

    # #show current student table
    print_table(conn, STUDENT)

    # #add 2 students
    student_attributes = []
    for i in get_table_info(conn, STUDENT):
        student_attributes.append(i[1])

    insert_row(conn, STUDENT, tuple(student_attributes), "(555555, 'Tom', 'Reggy', 2026, 'BSEE', 'reggyt')")
    insert_row(conn, STUDENT, tuple(student_attributes), "(397674, 'Dom', 'Ioime', 2023, 'BSCO', 'ioimed')")

    #show updated student table
    print_table(conn, STUDENT)

    print("------------------------------------------------------------------------------------------------------------\n")

    #show Instructor table
    print_table(conn, INSTRUCTOR)

    #remove instructor
    remove_row(conn, INSTRUCTOR, ID, "20004")

    #show Instructor table
    print_table(conn, INSTRUCTOR)

    print("------------------------------------------------------------------------------------------------------------\n")

    #show Admin table
    print_table(conn, ADMIN)

    #update admin value
    update_value(conn, ADMIN, ID, 30002, TITLE, "Vice-President")

    #show Admin table
    print_table(conn, ADMIN)

    print("------------------------------------------------------------------------------------------------------------\n")

    #print initial table names
    print(get_table_names(conn))

    #create a new course table
    create_table(conn, "COURSES", "CRN int primary key, TITLE text, DEPT text, TIME text, DAYS_OF_WEEK text, SEMESTER text, YEAR int, CREDITS int")

    #check to see if it was created with correct attributes
    print(get_table_names(conn))
    print(get_table_info(conn, COURSES))

    print("------------------------------------------------------------------------------------------------------------\n")

    courses_attributes = []
    for i in get_table_info(conn, COURSES):
        courses_attributes.append(i[1])

    #populate with 5 courses
    insert_row(conn, COURSES, tuple(courses_attributes), "(33180, 'Computer Networks for Engineers', 'BSCO', '8:00 - 9:20', 'TR', 'Summer', 2022, 4)")
    insert_row(conn, COURSES, tuple(courses_attributes), "(33169, 'Advanced Digital Circuit Design', 'BSCO', '8:00 - 9:20', 'WF', 'Summer', 2022, 4)")
    insert_row(conn, COURSES, tuple(courses_attributes), "(33185, 'Signals and Systems', 'BSCO', '10:00 - 11:50', 'MW', 'Summer', 2022, 4)")
    insert_row(conn, COURSES, tuple(courses_attributes), "(33175, 'Applied Programming Concepts', 'BSCO', '10:00 - 10:50', 'T', 'Summer', 2022, 3)")
    insert_row(conn, COURSES, tuple(courses_attributes), "(33203, 'Embedded Systems', 'BSCO', '5:00 - 6:20', 'MW', 'Summer', 2022, 3)")

    #print updated table
    print_table(conn, COURSES)

    print("------------------------------------------------------------------------------------------------------------\n")

    #Random Querys on courses DB
    print(search_table(conn, COURSES, "DAYS_OF_WEEK", 'MW'))
    update_value(conn, COURSES, "CRN", "33203", DEPT, "HUSS")
    
    #print updated table
    print_table(conn, COURSES)

    print("------------------------------------------------------------------------------------------------------------\n")

    #find matching instructors for the courses
    find_matching_instructors(conn)

    #ending for db modification
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

##for inserting courses using menu option
    # response = []
    # for i in courses_attributes:
    #     answer = input(i + "?: ")
    #     response.append(answer)
    #
    #insert_row(conn, COURSES, tuple(courses_attributes), tuple(response))