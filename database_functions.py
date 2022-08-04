import sqlite3
from sqlite3 import Error
from datetime import datetime


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

def get_table(conn, table):
    cur = conn.cursor()
    try:
        print("SELECT * FROM {}".format(table))
        cur.execute("SELECT * FROM {}".format(table))
        return cur.fetchall()
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
        print("DELETE FROM '{}' WHERE '{}' = '{}'".format(table, attribute, value))
        cur.execute("DELETE FROM '{}' WHERE '{}' = '{}'".format(table, attribute, value))
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
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name ASC;")
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

def get_attributes(conn, table):
    attributes = []
    for i in get_table_info(conn, table):
        attributes.append(i[1])
    return attributes

def find_matching_instructors(conn):
    cur = conn.cursor()
    try:
        print("SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, COURSES.TITLE FROM INSTRUCTOR INNER JOIN COURSES ON INSTRUCTOR.DEPT = COURSES.DEPT")
        cur.execute("SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, COURSES.TITLE FROM INSTRUCTOR INNER JOIN COURSES ON INSTRUCTOR.DEPT = COURSES.DEPT")
        fetch = cur.fetchall()
        print(fetch)
    except Error as e:
        print(e)

def add_course_to_schedule(conn, student_id, course_crn):
    cur = conn.cursor()
    try:
        print("INSERT INTO SCHEDULE('STUDENT_ID', 'COURSE_ID') VALUES ('{}', '{}')".format(student_id, course_crn))
        cur.execute("INSERT INTO SCHEDULE('STUDENT_ID', 'COURSE_ID') VALUES ('{}', '{}')".format(student_id, course_crn))
        conn.commit()
    except Error as e:
        print(e)
def remove_course_from_schedule(conn, student_id, course_crn ):
    cur = conn.cursor()
    try:
        print("DELETE FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(student_id, course_crn))
        cur.execute("DELETE FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(student_id, course_crn))
    except Error as e:
        print(e)

def print_student_schedule(conn, student_id):
    cur = conn.cursor()
    try:
        print("SELECT COURSE_ID FROM SCHEDULE, COURSES, STUDENT WHERE STUDENT.ID = SCHEDULE.STUDENT_ID AND COURSES.CRN = SCHEDULE.COURSE_ID AND ID = '{}'".format(student_id))
        cur.execute("SELECT COURSE_ID FROM SCHEDULE, COURSES, STUDENT WHERE STUDENT.ID = SCHEDULE.STUDENT_ID AND COURSES.CRN = SCHEDULE.COURSE_ID AND ID = '{}'".format(student_id))
        print(cur.fetchall())
    except Error as e:
        print(e)
        
#print all students in class
#def assemble_roster():
    
def print_instructor_schedule(conn, instructor_id):
    cur = conn.cursor()
    try:
        print("SELECT COURSES FROM SCHEDULE, COURSES, STUDENT WHERE INSTRUCTOR.ID = SCHEDULE.INSTRUCTOR_ID AND COURSES.CRN = SCHEDULE.COURSE_ID AND ID = '{}'".format(instructor_id))
        cur.execute("SELECT COURSES FROM SCHEDULE, COURSES, STUDENT WHERE INSTRUCTOR.ID = SCHEDULE.INSTRUCTOR_ID AND COURSES.CRN = SCHEDULE.COURSE_ID AND ID = '{}'".format(instructor_id))
    except Error as e:
        print(e)
        
#assign class to instructor based off department

def add_course_to_system(conn):
    #getting list of attributes in COURSES table
    courses_attributes = []
    for i in get_table_info(conn, "COURSES"):
        courses_attributes.append(i[1])

    #getting list of CRN #'s from COURSES table (make sure no duplicates when adding)
    crn_list = []
    cur = conn.cursor()
    cur.execute("SELECT COURSES.CRN FROM COURSES")
    fetch = cur.fetchall()
    crn_list = [int(item) for t in fetch for item in t]

    #prompting user for course information and error checking inputs
    response = []
    i = 0
    while i < len(courses_attributes[0:9]):
        answer = input(courses_attributes[i] + "?: ")
        #crn
        if (i == 0):
            try: 
                int(answer)
            except ValueError:
                print("Input is not an integer!")
                continue
            if ((len(answer) == 5) and (int(answer) not in crn_list)):
                response.append(int(answer))
            else:
                print("Error Adding " + courses_attributes[i] + ". (Make sure not already a CRN and is 5 digits long)")
                continue
        #title
        if (i == 1):
            if (len(answer) > 0):
                response.append(answer.upper())
            else:
                print("Error Adding " + courses_attributes[i] + ". (Make sure to enter a string)")
                continue
        #department
        if (i == 2):
            if((len(answer) == 4) and not(any([char.isdigit() for char in answer]))):
                response.append(answer.upper())
            else:
                print("Error Adding " + courses_attributes[i] + ". (Make sure answer is 4 characters long).")
                continue
        #start/end time
        if (i == 3 or i == 4):
            format = '%I:%M %p'
            try: 
                time = datetime.strptime(answer, format)
                response.append(time.strftime(format))
            except ValueError:
                print("Error Adding " + courses_attributes[i] + ". (Make sure in format hh:mm AM/PM).")
                continue
        #days of week
        if(i == 5):
            flag = 0
            days = []
            possible_days = ('M', 'T', 'W', 'TR', 'F')
            if (len(answer) > 0):
                for j in answer.split():
                    if (j.upper() in possible_days):
                        days.append(j.upper())
                    else:
                        flag = 1
                        break
            else:
                flag = 1
            if (flag):
                print("Error Adding " + courses_attributes[i] + ". (Make sure answer is M T W TR or F. For multiple days, seperate with a space).")
                continue
            delim = ','
            response.append(delim.join(days))
        #semester
        if (i == 6):
            semester_list = ['SPRING', 'SUMMER', 'FALL']
            if((len(answer) > 0) & (answer.upper() in semester_list)):
                response.append(answer.upper())
            else:
                print("Error Adding " + courses_attributes[i] + ". (Make sure answer is SPRING, SUMMER, or FALL).")
                continue
        #year
        if (i == 7):
            try: 
                int(answer)
            except ValueError:
                print("Input is not an integer!")
                continue
            if ((len(answer) == 4)):
                response.append(int(answer))
            else:
                print("Error Adding " + courses_attributes[i] + ". (Make sure answer is a 4 digit year).")
                continue
        #credits
        if (i == 8):
            try: 
                int(answer)
                response.append(int(answer))
            except ValueError:
                print("Error Adding " + courses_attributes[i] + ". (Make sure answer is an integer).")
                continue
        print(response)
        i += 1
    insert_row(conn, "COURSES", tuple(courses_attributes[0:9]), tuple(response))

def remove_course_from_system(conn, course_crn):
    cur = conn.cursor()
    crn_list = []
    cur = conn.cursor()
    cur.execute("SELECT COURSES.CRN FROM COURSES")
    fetch = cur.fetchall()
    crn_list = [int(item) for t in fetch for item in t]

    crn = 1
    while (crn != '0'):
        crn = input("What course would you like to remove? (Enter 0 to exit): ")
        if (crn in crn_list):
            print("DELETE FROM COURSES WHERE CRN = '{}'".format(crn))
            cur.execute("DELETE FROM COURSES WHERE CRN = '{}'".format(crn))
        elif(crn == '0'):
            break
        else:
            print("Invalid CRN")

def remove_course_from_schedule(conn, student_id, course_crn):
    cur = conn.cursor()
    try:
        print("DELETE FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(student_id, course_crn))
        cur.execute("DELETE FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(student_id, course_crn))
    except Error as e:
        print(e)

def remove_student(conn, student_id):
    cur = conn.cursor()
    try:
        print("DELETE FROM STUDENT WHERE ID = '{}'".format(student_id))
        cur.execute("DELETE FROM STUDENT WHERE ID = '{}'".format(student_id))
    except Error as e:
        print(e)
def search_courses(conn):
    #gets a set of all possible departments in the list
        dept_list = {}
        cur = conn.cursor()
        cur.execute("SELECT COURSES.DEPT FROM COURSES")
        fetch = cur.fetchall()
        dept_list = {item for t in fetch for item in t}

        #actual loop that runs to search for course
        while True:
            print("Enter a department or leave blank for everything!")
            print("0) Exit      1)List Deprtments")
            parameter = (input("Input: ")).upper()

            if (parameter == ''): #search for everything
                courses_table = get_table(conn, "COURSES")
                for i in courses_table:
                    print("\n")
                    print("CRN:", i[0])
                    print("TITLE:", i[1])
                    print("DEPT:", i[2])
                    print("START_TIME:", i[3])
                    print("END_TIME:", i[4])
                    print("DAYS_OF_WEEK:", i[5])
                    print("SEMESTER:", i[6])
                    print("YEAR:", i[7])
                    print("CREDITS:", i[8])
                    print("INSTRUCTOR:", i[9])
                    print("\n")
            elif (parameter == '1'):    #list departments
                for i in dept_list:
                    print(i, end='\t')
                print("\n")
            elif ((len(parameter) == 4) and not(any([char.isdigit() for char in parameter])) and (parameter in dept_list)): #correct input
                courses = search_table(conn, "COURSES", "DEPT", "{}".format(parameter))
                for i in courses:
                    print("\n")
                    print("CRN:", i[0])
                    print("TITLE:", i[1])
                    print("DEPT:", i[2])
                    print("START_TIME:", i[3])
                    print("END_TIME:", i[4])
                    print("DAYS_OF_WEEK:", i[5])
                    print("SEMESTER:", i[6])
                    print("YEAR:", i[7])
                    print("CREDITS:", i[8])
                    print("INSTRUCTOR:", i[9])
                    print("\n")
            elif (parameter == '0'):    #exit
                break
            else:
                print("Invalid Option! Enter a department name or one of the options!\n")
def print_course_roster(conn):
    cur = conn.cursor()
    crn = input("Please enter the course ID you would like to search")
    cur.execute("SELECT SCHEDULE.STUDENT_ID FROM SCHEDULE WHERE COURSE_ID = '{}'".format(crn.upper()))
    course_roster = cur.fetchall()
    print(course_roster)

def add_user(conn):
    while (response != 0):
        print("Would you like to add 1) Student 2) Instructor 3) Admin 0) Exit")
        response = input("Input: ")
        if (response == '1'):
            table = "STUDENT"
        elif (response == '2'):
            table = "INSTRUCTOR"
        elif (response == '3'):
            table = "ADMIN"
        elif (response == '0'):
            break
        else:
            print("Invalid Response!")
            continue
        answer = []
        for i in get_attributes(conn, table):
            answer.append(input(i + "?: "))
        insert_row(conn, table, get_attributes(conn, table), tuple(answer))

def remove_user(conn):
    while (response != 0):
        print("Would you like to remove 1) Student 2) Instructor 3) Admin 0) Exit")
        response = input("Input: ")
        if (response == '1'):
            table = "STUDENT"
        elif (response == '2'):
            table = "INSTRUCTOR"
        elif (response == '3'):
            table = "ADMIN"
        elif (response == '0'):
            break
        else:
            print("Invalid Response!")
            continue
        id = input("Please enter ID number to remove: ")
        remove_row(conn, table, "ID", id)
        
