from User import User
from database_functions import *

class Student(User):

    def __init__(self, first_name="First Name", last_name="Last Name", id="W00000000"):
        super().__init__(first_name, last_name, id)

    def search_course(self, conn):
        courses_attributes = []
        for i in get_table_info(conn, "COURSES"):
            courses_attributes.append(i[1])
        response = input("What parameter would you like to search by (leave blank for all courses)?: ")
        if (response)
        search_table(conn, "COURSES", attribute, value)
        #leave empty for all courses
    def add_course(self):
        add_course_to_schedule(conn, student_id, course_crn)
    def drop_course(self):
        remove_course_from_schedule(conn, student_id, course_crn )
    def print_schedule(self):
        print_student_schedule(conn, student_id)