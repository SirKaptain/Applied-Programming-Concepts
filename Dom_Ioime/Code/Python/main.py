from Student import Student
from Instructor import Instructor
from Admin import Admin

print("Welcome to Leopard Web!")
user_input = 1
while (user_input != 0):
    user_input = input(
"""
Choose an option:
Student(1)      Instructor(2)
Admin(3)        Exit(0)
Input: """)

    if (user_input == '1'):
        student = Student("Dom", "Ioime", "W00397674")
        while (user_input != '0'):
            user_input = input(
"""
Choose an option:
Add Course(1)       Drop Course(2)      Print Schedule(3)
Search Course(4)    Show Info(5)        Edit Info(6)            Exit(0)
Input: """)
            if (user_input == '1'):
                student.add_course()

            elif (user_input == '2'):
                student.drop_course()

            elif (user_input == '3'):
                student.print_schedule()

            elif (user_input == '4'):
                student.search_course()

            elif (user_input == '5'):
                student.show_info()

            elif (user_input == '6'):
                student.edit_info()

            elif (user_input == '0'):
                continue

            else:
                print("Invalid Option!")
    
    elif (user_input == '2'):
        instructor = Instructor("Ahmed", "Hassebo", "W00111111")
        while (user_input != '0'):
            user_input = input(
            """
Choose an option:
Print Schedule(1)       Print Classlist(2)      Search Course(3)
Show Info(4)            Edit Info(5)            Exit(0)
Input: """)
            if (user_input == '1'):
                instructor.print_schedule()
            
            elif (user_input == '2'):
                instructor.print_classlist()
            
            elif (user_input == '3'):
                instructor.search_course()

            elif (user_input == '4'):
                instructor.show_info()

            elif (user_input == '5'):
                instructor.edit_info()

            elif (user_input == '0'):
                continue
            
            else:
                print("Invalid Option!")
    
    elif (user_input == '3'):
        admin = Admin("Mark", "Thompson", "W00999999")
        while (user_input != '0'):
            user_input = input("""
Choose an option:
Add Course(1)       Remove Course(2)    Add User(3)         Remove User(4)      
Add a Student to a Course(5)    Remove a Student from a Course(6)
Search Roster(7)    Print Roster(8)     Search Course(9)    Print Course(10)    
Show Info(11)       Edit Info(12)       Exit(0)
Input: """)
            if (user_input == '1'):
                admin.add_course()
            
            elif (user_input == '2'):
                admin.remove_course()
            
            elif (user_input == '3'):
                admin.add_user()
            
            elif (user_input == '4'):
                admin.remove_user()
            
            elif (user_input == '5'):
                admin.add_student_to_course()
            
            elif (user_input == '6'):
                admin.remove_student_from_course()
            
            elif (user_input == '7'):
                admin.search_roster()
            
            elif (user_input == '8'):
                admin.print_roster()
            
            elif (user_input == '9'):
                admin.search_course()
            
            elif (user_input == '10'):
                admin.print_course()
            
            elif (user_input == '11'):
                admin.show_info()

            elif (user_input == '12'):
                admin.edit_info()

            elif (user_input == '0'):
                continue

            else:
                print("Invalid Option!")
    
    elif (user_input == '0'):
        print("Have a nice day!")
        break
    
    else :
        print("Invalid Option!")
