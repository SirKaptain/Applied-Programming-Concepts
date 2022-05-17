
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


student = Student("Dom", "Ioime", "w00397674")
print(student.show_first_name())
print(student.show_last_name())
print(student.show_id())