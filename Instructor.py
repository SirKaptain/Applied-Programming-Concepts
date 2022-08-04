from User import User
from database_functions import *

class Instructor(User):

    def __init__(self, id, first_name, last_name, title, hireyear, dept, email):
        super().__init__(id, first_name, last_name, email)
        self.title = title
        self.hireyear = hireyear
        self.dept = dept

    def show_info(self):
        print(self.id)
        print (self.first_name)
        print(self.last_name)
        print(self.title)
        print(self.hireyear)
        print(self.dept)
        print(self.email)

    def print_schedule(conn, self):
        print_instructor_schedule(conn, self.id)
    def print_classlist(conn):
        print_course_roster(conn)
    def search_course(self, conn):
        search_courses(self.id, conn)