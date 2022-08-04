from Student import Student
from Instructor import Instructor
from Admin import Admin
from database_functions import *

conn = create_connection('assignment_5_base.db')

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
            print("Incorrect Credentials! Please Try Again.")

user.show_info()

if (type(user)==Student):
    choice = input("Would you like to add course to schedule(0), remove course from schedule(1), print schedule(2), or search a course(3)")
    choice = int(choice)
    if choice == 0:
        user.add_course(cur, )
    elif choice == 1:
        user.drop_course()
    elif choice == 2:
        user.print_schedule()
    elif choice == 3:
        user.search_course()

elif (type(user)==Instructor):
    choice = input("Would you like to search courses, or print classlist")
    if choice == 0:
        user.search_course()
    elif choice == 1:
        user.print_classlist()

    
elif (type(user)==Admin):
    choice = input("Would you like to add course to system")
    if choice == 0:
        user.add_course_to_system()
    elif choice == 1:
        user.remove_course_from_system()
    elif choice == 2:
        user.remove_student()