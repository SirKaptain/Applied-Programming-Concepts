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
    
    #searches course table based on parameter from user, leave blank to display all courses
    def search_course(self, conn):

        #gets a set of all possible departments in the list
        dept_list = {}
        cur = conn.cursor()
        cur.execute("SELECT COURSES.DEPT FROM COURSES")
        fetch = cur.fetchall()
        dept_list = {item for t in fetch for item in t}

        #actual loop that runs to search for course
        while True:
            print("Enter a department or leave blank for everything!")
            print("0) Exit      1)List Deprtments")
            parameter = (input("Input: ")).upper()

            if (parameter == ''): #search for everything
                courses_table = get_table(conn, "COURSES")
                for i in courses_table:
                    print("\n")
                    print("CRN:", i[0])
                    print("TITLE:", i[1])
                    print("DEPT:", i[2])
                    print("START_TIME:", i[3])
                    print("END_TIME:", i[4])
                    print("DAYS_OF_WEEK:", i[5])
                    print("SEMESTER:", i[6])
                    print("YEAR:", i[7])
                    print("CREDITS:", i[8])
                    print("INSTRUCTOR:", i[9])
                    print("\n")
            elif (parameter == '1'):    #list departments
                for i in dept_list:
                    print(i, end='\t')
                print("\n")
            elif ((len(parameter) == 4) and not(any([char.isdigit() for char in parameter])) and (parameter in dept_list)): #correct input
                courses = search_table(conn, "COURSES", "DEPT", "{}".format(parameter))
                for i in courses:
                    print("\n")
                    print("CRN:", i[0])
                    print("TITLE:", i[1])
                    print("DEPT:", i[2])
                    print("START_TIME:", i[3])
                    print("END_TIME:", i[4])
                    print("DAYS_OF_WEEK:", i[5])
                    print("SEMESTER:", i[6])
                    print("YEAR:", i[7])
                    print("CREDITS:", i[8])
                    print("INSTRUCTOR:", i[9])
                    print("\n")
            elif (parameter == '0'):    #exit
                break
            else:
                print("Invalid Option! Enter a department name or one of the options!\n")

        #leave empty for all courses

    def add_course(self, conn, course_crn):
        add_course_to_schedule(conn, self.id, course_crn)
    def drop_course(self, conn, course_crn):
        remove_course_from_schedule(conn, self.id, course_crn)
    def print_schedule(self, conn):
        print_student_schedule(conn, self.id)