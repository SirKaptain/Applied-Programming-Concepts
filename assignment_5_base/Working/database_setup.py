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

#gets a list of the names of the attributes in the tables
login_attributes = []
for i in get_table_info(conn, "LOGIN"):
    login_attributes.append(i[1])

student_attributes = []
for i in get_table_info(conn, "STUDENT"):
    student_attributes.append(i[1])

instructor_attributes = []
for i in get_table_info(conn, "INSTRUCTOR"):
    instructor_attributes.append(i[1])

admin_attributes = []
for i in get_table_info(conn, "ADMIN"):
    admin_attributes.append(i[1])

schedule_attributes = []
for i in get_table_info(conn, "SCHEDULE"):
    schedule_attributes.append(i[1])

courses_attributes = []
for i in get_table_info(conn, "COURSES"):
    courses_attributes.append(i[1])

#populates all tables with ID's and the login table with ID's and passwords
#generates 100 random "W00 + 6 digit" id's and "4 character" passwords
def populate_ID_and_PW(conn):
    for i in range(100):
        id = ('W00' + '{:06}'.format(random.randrange(1, 10**6)))
        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        if (i < 60):
            insert_row(conn, "STUDENT", "('{}')".format(student_attributes[0]), "('{}')".format(id))
        elif (i < 90):
            insert_row(conn, "INSTRUCTOR", "('{}')".format(instructor_attributes[0]), "('{}')".format(id))
        elif (i <= 100):
            insert_row(conn, "ADMIN", "('{}')".format(admin_attributes[0]), "('{}')".format(id))

        insert_row(conn, "LOGIN", tuple(login_attributes), "('{}','{}')".format(id, password))

#populate the courses table from a .csv file
def populate_courses(conn):
    #populating courses table from csv file
    data = pd.read_csv ('./Working/initial_courses_table.csv')   
    df = pd.DataFrame(data)
    cur = conn.cursor()
    for row in df.itertuples():
        cur.execute("INSERT INTO COURSES (CRN, TITLE, DEPT, START_TIME, END_TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row.CRN, row.TITLE, row.DEPT, row.START_TIME, row.END_TIME, row.DAYS_OF_WEEK, row.SEMESTER, row.YEAR, row.CREDITS))

remove_all_tables(conn)
setup_all_tables(conn)
populate_ID_and_PW(conn)
conn.commit()
populate_courses(conn)

courses_table = get_table(conn, "COURSES")
for i in courses_table:
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
    print("\n\n")

#add_course_to_system(conn)

#remove_course_from_schedule(conn, "W00397674", "23456")



#ending for db modification
conn.commit()
conn.close()