from Student import Student
from Instructor import Instructor
from Admin import Admin
from database_functions import *

conn = create_connection('./Working/database.db')

while True:
    #login block, searches each table for input and makes object based off of search result
    id = input("Enter your username or ID (including W00): ")
    password = input("Enter your password: ")

    cur = conn.cursor()

    flag = 0
    tables = get_table_names(conn)
    for table in [tables[0], tables[2], tables[5]]:
        cur.execute("SELECT * FROM {} WHERE ID = '{}' OR EMAIL = '{}';".format(table, id.upper(), id.lower()))
        user_info = cur.fetchall()
        if (len(user_info) > 0): #found user in database
            print(table)
            break
        else:
            flag += 1
    if (flag == 3):
        print("No user found!")

    if (user_info): #if a user was found
        #check login table for correct password
        cur.execute("SELECT LOGIN.PASSWORD FROM LOGIN WHERE ID = '{}'".format(user_info[0][0]))
        user_password = cur.fetchall()
        print(user_password)

        if (password == user_password[0][0]): #password correct
            #make object then break from login loop
            if(table == "STUDENT"):
                user = Student(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5])
            elif (table == "INSTRUCTOR"):
                user = Instructor(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5], user_info[0][6])
            elif (table == "ADMIN"):
                user = Admin(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5], user_info[0][6])
            break
        else:
            print("Incorrect Credentials! Pleas Try Again.")

user.show_info()

# if (len(student_info) > 0): #if found an entry
#     user = Student(student_info[0][0], student_info[0][1], student_info[0][2], student_info[0][3], student_info[0][4], student_info[0][5])
# elif (len(instructor_info) > 0): #if found an entry
#     user = Instructor(instructor_info[0][0], instructor_info[0][1], instructor_info[0][2], instructor_info[0][3], instructor_info[0][4], instructor_info[0][5], instructor_info[0][6])
# elif (len(admin_info) > 0): #if found an entry
#     user = Admin(admin_info[0][0], admin_info[0][0], admin_info[0][1], admin_info[0][2], admin_info[0][3], admin_info[0][4], admin_info[0][5], admin_info[0][6])
# else:
#     print("Invalid Username!")




