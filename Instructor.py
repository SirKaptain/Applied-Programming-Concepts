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

    def print_schedule(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM COURSES WHERE COURSES.INSTRUCTOR_ID = '{}'".format(self.id))
        courses = cur.fetchall()
        if (len(courses) == 0):
            print("No Courses in Schedule!")
        else:
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
                print("\n")

    def print_classlist(self, conn):
        cur = conn.cursor()
        crn = input("Please enter the course ID you would like to view the roster for: ")
        cur.execute("SELECT SCHEDULE.STUDENT_ID FROM SCHEDULE WHERE COURSE_ID = '{}'".format(crn.upper()))
        course_roster = cur.fetchall()
        for i in course_roster:
            cur.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT WHERE STUDENT.ID = '{}'".format(i[0]))
            student_name = (cur.fetchall())
            print(''.join(student_name[0][0] + ' '+ student_name[0][1]))
