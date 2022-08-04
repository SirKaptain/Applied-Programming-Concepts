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
    def remove_course(self, conn, course_crn):
        remove_course_from_system(conn, course_crn)
    def add_user(self, conn):
        add_user(conn)
    def remove_user(self, conn):
        remove_user(conn)
    def add_student_to_course(self, conn, student_id, course_crn):
        add_course_to_schedule(conn, student_id, course_crn)
    def remove_student_from_course(self, conn, student_id, course_crn):
        remove_course_from_schedule(conn, student_id, course_crn)
    def print_roster(self, conn):
        print_course_roster(conn)