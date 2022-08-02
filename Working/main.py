from dis import Instruction
from Student import Student
from Instructor import Instructor
from Admin import Admin
from database_functions import *

conn = create_connection('./Working/database.db')

#login block, searches each table for input and makes object based off of search result
id = input("Enter your username or ID (including W00): ")
password = input("Enter your password: ")

cur = conn.cursor()

cur.execute("SELECT * FROM STUDENT WHERE STUDENT.ID = '{}' OR STUDENT.EMAIL = '{}'".format(id.upper(), id.lower()))
student_info = cur.fetchall()

cur.execute("SELECT * FROM INSTRUCTOR WHERE INSTRUCTOR.ID = '{}' OR INSTRUCTOR.EMAIL = '{}'".format(id.upper(), id.lower()))
instructor_info = cur.fetchall()

cur.execute("SELECT * FROM ADMIN WHERE ADMIN.ID = '{}' OR ADMIN.EMAIL = '{}'".format(id.upper(), id.lower()))
admin_info = cur.fetchall()

if (len(student_info) > 0): #if found an entry
    user = Student(student_info[0][0], student_info[0][1], student_info[0][2], student_info[0][3], student_info[0][4], student_info[0][5])
    print(user.show_info())
elif (len(instructor_info) > 0): #if found an entry
    user = Instructor(instructor_info[0][0], instructor_info[0][1], instructor_info[0][2], instructor_info[0][3], instructor_info[0][4], instructor_info[0][5], instructor_info[0][6])
elif (len(admin_info) > 0): #if found an entry
    user = Admin(admin_info[0][0], admin_info[0][0], admin_info[0][1], admin_info[0][2], admin_info[0][3], admin_info[0][4], admin_info[0][5], admin_info[0][6])
else:
    print("Invalid Username!")


#check login table for correct password
#finds password
cur.execute("SELECT LOGIN.PASSWORD FROM LOGIN WHERE ID = '{}'".format(user.id))
user_password = cur.fetchall()
print(user_password)
