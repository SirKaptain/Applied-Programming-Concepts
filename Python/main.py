
class User:
    def __init__(self, first_name = "First Name", last_name = "Last Name", id = "W00000000"):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
    def show_first_name(self):
        return self.first_name
    
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
    def show_last_name(self):
        return self.last_name

    def set_id(self, new_id):
        self.id = new_id
    def show_id(self):
        return self.id

class Student(User):
    def search_course():
        print("Search course for Student!")
    def add_course():
        print("Add Course for Student!")
    def drop_course():
        print("Drop Course for Student!")
    def print_schedule():
        print("Print Schedule for Student!")

class Instructor(User):
    def print_schedule():
        print("Print Schedule for Instructor!")
    def print_classlist():
        print("Print Classlist for Instructor!")
    def search_course():
        print("Search course for Instructor!")

class Admin(User):
    def add_course():
        print("Add Course for Admin!")
    def remove_course():
        print("Remove Course for Admin!")
    def add_user():
        print("Add User for Admin!")
    def remove_user():
        print("Remove User for Admin!")
    def add_student_to_course():
        print("Add Student to Course for Admin!")
    def remove_student_from_course():
        print("Remove Student from Course for Admin!")
    def search_roster():
        print("Search Roster for Admin!")
    def print_roster():
        print("Print Roster for Admin!")
    def search_course():
        print("Search Course for Admin!")
    def print_course():
        print("Print Course for Admin!")

print("Welcome to Leopard Web!")
user_input = 1
while (user_input != 0):
    print("Choose an option:")
    print("Student(1)")
    print("Instructor(2)")
    print("Admin(3)")
    print("Exit(0)")
    user_input = input("Input:")

    if (user_input == 1):
        student = Student("Dom", "Ioime", "W00397674")
        while (user_input != 0):
            print("Choose an option:")
            print("Add Course(1)")
            print("Drop Course(2)")
            print("Print Schedule(3)")
            print("Search Course(4)")
            print("Exit(0)")
            user_input = input("Input:")
            if (user_input == 1):
                student.add_course()
            elif (user_input == 2):
                student.drop_course()
            elif (user_input == 3):
                student.print_schedule()
            elif (user_input == 4):
                student.search_course()
            elif (user_input == 0):
                continue
            else:
                print("Invalid Option!")
    
    elif (user_input == 2):
        instructor = Instructor("Ahmed", "Hassebo", "W00111111")
        while (user_input != 0):
            print("Choose an option:")
            print("Print Schedule(1)")
            print("Print Classlist(2)")
            print("Search Course(3)")
            print("Exit(0)")
            user_input = input("Input:")
            if (user_input == 1):
                instructor.print_schedule()
            
            elif (user_input == 2):
                instructor.print_classlist()
            
            elif (user_input == 3):
                instructor.search_course()
            
            elif (user_input == 0):
                continue
            
            else:
                print("Invalid Option!")
    
    elif (user_input == 3):
        admin = Admin("Mark", "Thompson", "W00999999")
        while (user_input != 0):
            print("Choose an option:")
            print("Add Course(1)")
            print("Remove Course(2)")
            print("Add User(3)")
            print("Remove User(4)")
            print("Add a Student to a Course(5)")
            print("Remove a Student from a Course(6)")
            print("Search Roster(7)")
            print("Print Roster(8)")
            print("Search Course(9)")
            print("Print Course(10)")
            print("Exit(0)")
            user_input = input("Input:")
            if (user_input == 1):
                admin.add_course()
            
            elif (user_input == 2):
                admin.remove_course()
            
            elif (user_input == 3):
                admin.add_user()
            
            elif (user_input == 4):
                admin.remove_user()
            
            elif (user_input == 5):
                admin.add_student_to_course()
            
            elif (user_input == 6):
                admin.remove_student_from_course()
            
            elif (user_input == 7):
                admin.search_roster()
            
            elif (user_input == 8):
                admin.print_roster()
            
            elif (user_input == 9):
                admin.search_course()
            
            elif (user_input == 10):
                admin.print_course()
            
            elif (user_input == 0):
                continue
            
            else:
                print("Invalid Option!")
    
    elif (user_input == 0):
        print("Have a nice day!")
        break
    
    else :
        print("Invalid Option!")