from User import User
from database_functions import *

class Student(User):

    def __init__(self, id, first_name, last_name, gradyear, major, email):
        super().__init__(id, first_name, last_name, email)
        self.gradyear = gradyear
        self.major = major

    def show_info(self):
        print(self.id)
        print (self.first_name)
        print(self.last_name)
        print(self.gradyear)
        print(self.major)
        print(self.email)

    def add_course(self, conn, course_crn):
        add_course_to_schedule(conn, self.id, course_crn)
    def drop_course(self, conn, course_crn):
        remove_course_from_schedule(conn, self.id, course_crn)
    def print_schedule(self, conn):
        print_student_schedule(conn, self.id)