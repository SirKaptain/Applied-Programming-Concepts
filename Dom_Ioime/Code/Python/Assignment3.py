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
STUDENT_ATTRIBUTES = "(ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL)"
INSTRUCTOR_ATTRIBUTES = "(ID, NAME, SURNAME, TITLE, HIREYEAR, DEPT, EMAIL)"
ADMIN_ATTRIBUTES = "(ID, NAME, SURNAME, TITLE, OFFICE, EMAIL)"


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
        cur.execute("CREATE TABLE {} ({})".format(table, attribute))
    except Error as e:
        print(e)

def remove_table(conn, table):
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE " + table)
    except Error as e:
        print(e)

def print_table(conn, table):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM {}".format(table))
        print(cur.fetchall())
    except Error as e:
        print(e)

def search_table(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM " + table + " WHERE " + attribute + " = ?", (value,))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

def insert_row(conn, table, attributes, values):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO {} ({}) VALUES {}".format(table, attributes, values))
    except Error as e:
        print(e)

def remove_row(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM " + table + " WHERE " + attribute + "=" + value)
    except Error as e:
        print(e)

def update_value(conn, table, attribute, old_value, new_value):
    cur = conn.cursor()
    try:
        cur.execute("UPDATE " + table + " SET " + attribute + " = ? WHERE " + attribute + " = ?", (new_value, old_value))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

def get_table_names(conn):
    list = []
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        for i in tables:
            list.append(i[0])
        return list
    except Error as e:
        print(e)

def get_attribute_names(conn, table):
    list = []
    cur = conn.cursor()
    try:
        cur.execute("PRAGMA table_info({})".format(table))
        info = cur.fetchall()
        for i in info:
            list.append(i[1])
        return list
    except Error as e:
        print(e)

#def find_matching_instructor(conn, course_table, instructor_table, )

def main():
    # create a database connection
    conn = create_connection('./Dom_Ioime/Code/Python/assignment3.db')

    #show current student table
    print_table(conn, STUDENT)

    #add 2 students
    ######################################FIGURE OUT####################################################
    insert_row(conn, STUDENT, str(get_attribute_names(conn, STUDENT)), "555555, 'Tom', 'Reggy', 2026, 'BSEE', 'reggyt'")
    insert_row(conn, STUDENT, "(ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL)", "(397674, 'Dom', 'Ioime', 2023, 'BSCO', 'ioimed')")

    #show updated student table
    print_table(conn, STUDENT)

    #show Instructor table
    print_table(conn, INSTRUCTOR)

    #remove instructor
    remove_row(conn, INSTRUCTOR, ID, "20004")

    #show Instructor table
    print_table(conn, INSTRUCTOR)

    #show Admin table
    print_table(conn, ADMIN)

    #update admin value
    update_value(conn, ADMIN, TITLE, "Registrar", "Vice-President")

    #show Admin table
    print_table(conn, ADMIN)

    #print initial table names
    print(get_table_names(conn))

    #create a new course table
    create_table(conn, "COURSES", "CRN text, TITLE text, DEPT text, TIME text, DAYS_OF_WEEK text, SEMESTER text, YEAR int, CREDITS int")

    #check to see if it was created with correct attributes
    print(get_table_names(conn))
    print(get_attribute_names(conn, COURSES))

    # #populate with 5 courses
    insert_row(conn, COURSES, "(CRN, TITLE, DEPT, TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS)", "('33180', 'Computer Networks for Engineers', 'BSCO', '8:00 - 9:20', 'TR', 'Summer', 2022, 4)")
    insert_row(conn, COURSES, "(CRN, TITLE, DEPT, TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS)", "('33169', 'Advanced Digital Circuit Design', 'BSCO', '8:00 - 9:20', 'WF', 'Summer', 2022, 4)")
    insert_row(conn, COURSES, "(CRN, TITLE, DEPT, TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS)", "('33185', 'Signals and Systems', 'BSCO', '10:00 - 11:50', 'MW', 'Summer', 2022, 4)")
    insert_row(conn, COURSES, "(CRN, TITLE, DEPT, TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS)", "('33175', 'Applied Programming Concepts', 'BSCO', '10:00 - 10:50', 'T', 'Summer', 2022, 3)")
    insert_row(conn, COURSES, "(CRN, TITLE, DEPT, TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS)", "('33203', 'Embedded Systems', 'BSCO', '5:00 - 6:20', 'MW', 'Summer', 2022, 3)")

    # #print updated table
    print_table(conn, COURSES)

    print("-----------------------------")

    #search 
    search_table(conn, COURSES, "(DAYS_OF_WEEK)", "MW")


    conn.commit()
    conn.close()



if __name__ == '__main__':
    main()