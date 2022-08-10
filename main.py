from Student import Student
from Instructor import Instructor
from Admin import Admin
from database_functions import *

conn = create_connection('assignment_5_base.db')
cur = conn.cursor()

#---------------------------------LOGIN BLOCK----------------------------------------------#
#User inputs ID/username
#doesn't escape loop untill a user successfully logs in
while True:
    
    id = input("Enter your username or ID (including W00): ")
    password = input("Enter your password: ")


    #searching through tables for user
    tables = get_table_names(conn)
    for table in [tables[0], tables[2], tables[5]]: #searching only student, instructor, and admin table
        cur.execute("SELECT * FROM {} WHERE ID = '{}' OR EMAIL = '{}';".format(table, id.upper(), id.lower()))
        user_info = cur.fetchall()
        if (user_info): #found user in database
            break

    if (user_info): #if a user was found
        #check login table for correct password
        cur.execute("SELECT LOGIN.PASSWORD FROM LOGIN WHERE ID = '{}'".format(user_info[0][0]))
        db_password = (cur.fetchall())[0][0]

        if (password == db_password): #password correct
            #make object then break from login loop
            if(table == "STUDENT"):
                user = Student(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5])
            elif (table == "INSTRUCTOR"):
                user = Instructor(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5], user_info[0][6])
            elif (table == "ADMIN"):
                user = Admin(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5])
            break
        else:
            print("Incorrect Password")
    else:
        print("Invalid User!")
        continue

#-----------------------------------------MAIN CHOICES---------------------------------------------#
if (type(user)==Student):
    choice = 111
    while (choice != '0'):
        print(
"""
What would you like to do:
1) Search Courses               2) Add Course to Schedule
3) Remove Course from Schedule  4) Print Schedule
5) Check For Conflicts          0) Exit 
""")
        choice = input("Input: ")

        if (choice == '1'):
            user.search_course(conn)
        elif (choice == '2'):
            course_id = input("Enter course ID: ")
            user.add_course(conn, course_id)
        elif (choice == '3'):
            course_id = input("Enter course ID: ")
            user.drop_course(conn, course_id)
        elif (choice == '4'):
            user.print_schedule(conn)
        elif (choice == '5'):
            print("WIP")
        elif choice == '0':
            print("Exiting")
            break
        else:
            print("Input invalid")

elif (type(user)==Instructor):
    choice = 111
    while (choice != '0'):
        print(
"""
What would you like to do:
1) Search Courses   2)Print Schedule
3) Search Roster    0)Exit
"""
        )
        choice = input("Input: ")
        if (choice == '1'):
            user.search_course(conn)
        elif (choice == '2'):
            user.print_schedule(conn)
        elif (choice == '3'):
            user.print_classlist(conn)
        elif (choice == '0'):
            print("Exiting")
            break
        else:
            print("User input invalid")
    
elif (type(user)==Admin):
    choice = 111
    while (choice != 0):
        print(
"""
What would you like to do:
1) Add Course to System     2) Remove Course from System
3) Add User                 4) Remove User
5) Add Student to Course    6) Remove Student from Course
7) Add Instructor to Course 8) Remove Instructor from C0urse
9) Print Roster             10) Search Course
0) Exit       
"""
        )
        choice = input("Input: ")
        if (choice == '1'):
            user.add_course()
        elif (choice == '2'):
            user.remove_course()
        elif (choice == '3'):
            user.add_user()
        elif (choice == '4'):
            user.remove_user()
        elif (choice == '5'):
            user.add_student_to_course()
        elif (choice == '6'):
            user.remove_student_from_course()
        elif (choice == '7'):
            user.add_instructor_to_course()
        elif (choice == '8'):
            user.remove_instructor_from_course()
        elif (choice == '9'):
            user.print_roster()
        elif (choice == '10'):
            user.search_course()
        elif (choice == '0'):
            print("Exiting")
            break
        else:
            print("User input invalid")
conn.commit()
conn.close()
