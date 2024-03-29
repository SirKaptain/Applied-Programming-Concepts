from User import User
from database_functions import *

class Admin(User):

    def __init__(self, id, first_name, last_name, title, office, email):
        super().__init__(id, first_name, last_name, email)
        self.title = title
        self.office = office

    def show_info(self):
        print(self.id)
        print (self.first_name)
        print(self.last_name)
        print(self.title)
        print(self.office)
        print(self.email)

    def add_course(self, conn):
        add_course_to_system(conn)
    def remove_course(self, conn):
        remove_course_from_system(conn)
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
    def search_course(self, conn):
        search_courses(conn)
    def print_course(self):
        print("Print Course for Admin!")