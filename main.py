from Student import Student
from Instructor import Instructor
from Admin import Admin
from database_functions import *

conn = create_connection('assignment_5_base.db')

#---------------------------------LOGIN BLOCK----------------------------------------------#
#User inputs ID/username
#doesn't escape loop untill a user successfully logs in
while True:
    
    id = input("Enter your username or ID (including W00): ")
    password = input("Enter your password: ")

    cur = conn.cursor()

    flag = 0
    tables = get_table_names(conn)

    for table in [tables[0], tables[2], tables[5]]: #searching only student, instructor, and admin table
        cur.execute("SELECT * FROM {} WHERE ID = '{}' OR EMAIL = '{}';".format(table, id.upper(), id.lower()))
        user_info = cur.fetchall()
        if (len(user_info) > 0): #found user in database
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
                user = Admin(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4], user_info[0][5], user_info[0][6])
            break
    else:
        print("Invalid Credentials! Please Try Again.")
        continue

#-----------------------------------------MAIN CHOICES---------------------------------------------#
if (type(user)==Student):
    choice = 111
    while choice != 10:
        choice = input("Would you like to add course to schedule (0), remove course from schedule (1), print schedule (2), or exit (10): ")
        choice = int(choice)
        if choice == 0:
            course_id = input("Enter course ID: ")
            user.add_course(conn, course_id)
        elif choice == 1:
            course_id = input("Enter course ID: ")
            user.drop_course(conn, course_id)
        elif choice == 2:
            user.print_schedule(conn)
        elif choice == 10:
            print("Exiting")
        else:
            print("User input invalid")

elif (type(user)==Instructor):
    choice = 111
    while choice != 10:
        choice = input("Would you like to print schedule(0),  print classlist (1), search courses (2), or exit (10): ")
        if choice == 0:
            user.print_schedule(conn)
        elif choice == 1:
            user.print_classlist(conn)
        elif choice == 2:
            user.search_course(conn)
        elif choice == 10:
            print("Exiting")
        else:
            print("User input invalid")
    
elif (type(user)==Admin):
    choice = 111
    while choice != 10:
        choice = input("""Would you like to add course to system (0), 
        remove course from system (1), add user to system (2), 
        remove user from system (3),  add student to course (4), 
        remove student from course (5), print roster (6), 
        search course (7), or exit (10): """)
        if choice == 0:
            user.add_course()
        elif choice == 1:
            user.remove_course()
        elif choice == 2:
            user.add_user()
        elif choice == 3:
            user.remove_user()
        elif choice == 4:
            user.add_student_to_course()
        elif choice == 5:
            user.remove_student_from_course()
        elif choice == 6:
            user.print_roster()
        elif choice == 7:
            user.search_course()
        elif choice == 10:
            print("Exiting")
        else:
            print("User input invalid")
conn.commit()
conn.close()