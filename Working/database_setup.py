from database_functions import *
import random
import string

# create a database connection
conn = create_connection('./Working/database.db') 


remove_table(conn, "LOGIN")
remove_table(conn, "STUDENT")
remove_table(conn, "INSTRUCTOR")
remove_table(conn, "ADMIN")
remove_table(conn, "COURSES")
remove_table(conn, "SCHEDULE")


#creating necessary tables
create_table(conn, "LOGIN", "ID text primary key, PASSWORD text")
create_table(conn, "STUDENT", "ID text primary key, NAME text, SURNAME text, GRADYEAR int, MAJOR char(4), EMAIL text")
create_table(conn, "INSTRUCTOR", "ID text primary key, NAME text, SURNAME text, TITLE text, HIREYEAR int, DEPT char(4), EMAIL text")
create_table(conn, "ADMIN", "ID text primary key, NAME text, SURNAME text, TITLE text, OFFICE text, EMAIL text")
create_table(conn, "COURSES", "CRN text primary key, TITLE text, DEPT text, TIME text, DAYS_OF_WEEK text, SEMESTER text, YEAR int, CREDITS int")

#creating many-to-many mapping table for schedules (one student belongs to many courses, and one course belongs to many students)
create_table(conn, "SCHEDULE", "STUDENT_ID text, COURSE_ID text, FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT(ID), FOREIGN KEY(COURSE_ID) REFERENCES COURSES(CRN)")


#gets a list of the names of the attributes
login_attributes = []
for i in get_table_info(conn, "LOGIN"):
    login_attributes.append(i[1])

tuple(login_attributes)

student_attributes = []
for i in get_table_info(conn, "STUDENT"):
    student_attributes.append(i[1])

instructor_attributes = []
for i in get_table_info(conn, "INSTRUCTOR"):
    instructor_attributes.append(i[1])

admin_attributes = []
for i in get_table_info(conn, "ADMIN"):
    admin_attributes.append(i[1])


#populates all tables with ID's and the login table with ID's and passwords
#generates 100 random "W00 + 6 digit" id's and "4 character" passwords
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
    


#ending for db modification
conn.commit()
conn.close()
