from User import User

class Admin(User):

    def __init__(self, first_name="First Name", last_name="Last Name", id="W00000000"):
        super().__init__(first_name, last_name, id)


    def add_course(self):
        print("Add Course for Admin!")
    def remove_course(self):
        print("Remove Course for Admin!")
    def add_user(self):
        print("Add User for Admin!")
    def remove_user(self):
        print("Remove User for Admin!")
    def add_student_to_course(self):
        print("Add Student to Course for Admin!")
    def remove_student_from_course(self):
        print("Remove Student from Course for Admin!")
    def search_roster(self):
        print("Search Roster for Admin!")
    def print_roster(self):
        print("Print Roster for Admin!")
    def search_course(self):
        print("Search Course for Admin!")
    def print_course(self):
        print("Print Course for Admin!")