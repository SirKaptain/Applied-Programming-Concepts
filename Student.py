from datetime import date
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
        cur = conn.cursor()
        cur.execute("SELECT * FROM COURSES WHERE COURSES.CRN = '{}'".format(course_crn))
        course_info = cur.fetchall()
        if (course_info): #if found a course with correct crn
            #check for conflicts
            cur.execute("SELECT COURSES.START_TIME, COURSES.END_TIME, COURSES.DAYS_OF_WEEK, COURSES.SEMESTER, COURSES.YEAR FROM COURSES, SCHEDULE, STUDENT WHERE STUDENT.ID = SCHEDULE.STUDENT_ID AND COURSES.CRN = SCHEDULE.COURSE_ID AND STUDENT.ID = '{}'".format(self.id))
            schedule_info = cur.fetchall()
            print(schedule_info)
            format = "%I:%M %p"
            flag = 0
            for i in schedule_info:
                if ((datetime.strptime(i[0], format) < datetime.strptime(course_info[0][4], format)) and (datetime.strptime(i[1], format) > datetime.strptime(course_info[0][3], format))): #time overlap
                    if(i[2] == course_info[0][5] or (i[3] == course_info[0][6] and i[4] == course_info[0][7])):
                        print("\nCourse time conflicts with another course!\n")
                        flag = 1
            if (flag == 0):
                cur.execute("INSERT INTO SCHEDULE('STUDENT_ID', 'COURSE_ID') VALUES ('{}', '{}')".format(self.id, course_crn))
                conn.commit()
                cur.execute("SELECT COURSES.TITLE FROM COURSES WHERE COURSES.CRN = '{}'".format(course_crn))
                print("Added: " + (cur.fetchall())[0][0] + " to your schedule!")
  
        else:
            print("Invalid CRN!")

    def drop_course(self, conn, course_crn):
        cur = conn.cursor()
        #check if user has course in their schedule
        cur.execute("SELECT * FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(self.id, course_crn))
        if (cur.fetchall()):
            cur.execute("SELECT COURSES.TITLE FROM COURSES WHERE COURSES.CRN = '{}'".format(course_crn)) #get couse title for nice printing
            print("Removed: " + (cur.fetchall())[0][0] + " from schedule!")
            cur.execute("DELETE FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(self.id, course_crn))
            conn.commit()
        else:
            print("No such course in your schedule!")

    def print_schedule(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM COURSES, SCHEDULE, STUDENT, INSTRUCTOR WHERE STUDENT.ID = SCHEDULE.STUDENT_ID AND COURSES.CRN = SCHEDULE.COURSE_ID AND INSTRUCTOR.ID = COURSES.INSTRUCTOR_ID AND STUDENT.ID = '{}'".format(self.id))
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
                print("INSTRUCTOR:", i[19] + ' ' + i[20])
                print("\n")
