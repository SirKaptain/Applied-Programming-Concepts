from User import User
from database_functions import *
from datetime import datetime

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
        #getting list of attributes in COURSES table
        courses_attributes = []
        for i in get_table_info(conn, "COURSES"):
            courses_attributes.append(i[1])

        #getting list of CRN #'s from COURSES table (make sure no duplicates when adding)
        crn_list = []
        cur = conn.cursor()
        cur.execute("SELECT COURSES.CRN FROM COURSES")
        fetch = cur.fetchall()
        crn_list = [int(item) for t in fetch for item in t]

        #prompting user for course information and error checking inputs
        response = []
        i = 0
        while i < len(courses_attributes[0:9]):
            answer = input(courses_attributes[i] + "?: ")
            #crn
            if (i == 0):
                try: 
                    int(answer)
                except ValueError:
                    print("Input is not an integer!")
                    continue
                if ((len(answer) == 5) and (int(answer) not in crn_list)):
                    response.append(int(answer))
                else:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure not already a CRN and is 5 digits long)")
                    continue
            #title
            if (i == 1):
                if (len(answer) > 0):
                    response.append(answer.upper())
                else:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure to enter a string)")
                    continue
            #department
            if (i == 2):
                if((len(answer) == 4) and not(any([char.isdigit() for char in answer]))):
                    response.append(answer.upper())
                else:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure answer is 4 characters long).")
                    continue
            #start/end time
            if (i == 3 or i == 4):
                format = '%I:%M %p'
                try: 
                    time = datetime.strptime(answer, format)
                    response.append(time.strftime(format))
                except ValueError:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure in format hh:mm AM/PM).")
                    continue
            #days of week
            if(i == 5):
                flag = 0
                days = []
                possible_days = ('M', 'T', 'W', 'TR', 'F')
                if (len(answer) > 0):
                    for j in answer.split():
                        if (j.upper() in possible_days):
                            days.append(j.upper())
                        else:
                            flag = 1
                            break
                else:
                    flag = 1
                if (flag):
                    print("Error Adding " + courses_attributes[i] + ". (Make sure answer is M T W TR or F. For multiple days, seperate with a space).")
                    continue
                delim = ','
                response.append(delim.join(days))
            #semester
            if (i == 6):
                semester_list = ['SPRING', 'SUMMER', 'FALL']
                if((len(answer) > 0) & (answer.upper() in semester_list)):
                    response.append(answer.upper())
                else:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure answer is SPRING, SUMMER, or FALL).")
                    continue
            #year
            if (i == 7):
                try: 
                    int(answer)
                except ValueError:
                    print("Input is not an integer!")
                    continue
                if ((len(answer) == 4)):
                    response.append(int(answer))
                else:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure answer is a 4 digit year).")
                    continue
            #credits
            if (i == 8):
                try: 
                    int(answer)
                    response.append(int(answer))
                except ValueError:
                    print("Error Adding " + courses_attributes[i] + ". (Make sure answer is an integer).")
                    continue
            print(response)
            i += 1
        insert_row(conn, "COURSES", tuple(courses_attributes[0:9]), tuple(response))
        conn.commit()

    def remove_course(self, conn):
        cur = conn.cursor()
        crn_list = []
        cur = conn.cursor()
        cur.execute("SELECT COURSES.CRN FROM COURSES")
        fetch = cur.fetchall()
        crn_list = [int(item) for t in fetch for item in t]

        crn = 1
        while (crn != '0'):
            crn = input("What course crn would you like to remove? (Enter 0 to exit): ")
            if (crn in crn_list):
                cur.execute("DELETE FROM COURSES WHERE CRN = '{}'".format(crn))
                conn.commit()
            elif(crn == '0'):
                break
            else:
                print("Invalid CRN")

    def add_user(self, conn):
        while (response != 0):
            print("Would you like to add 1) Student 2) Instructor 3) Admin 0) Exit")
            response = input("Input: ")
            if (response == '1'):
                table = "STUDENT"
            elif (response == '2'):
                table = "INSTRUCTOR"
            elif (response == '3'):
                table = "ADMIN"
            elif (response == '0'):
                break
            else:
                print("Invalid Response!")
                continue
            answer = []
            for i in get_attributes(conn, table):
                answer.append(input(i + "?: "))
            insert_row(conn, table, get_attributes(conn, table), tuple(answer))
            conn.commit()

    def remove_user(self, conn):
        cur = conn.cursor()
        id = input("Please enter ID number to remove: ")

        tables = get_table_names(conn)
        for table in [tables[0], tables[2], tables[5]]: #searching only student, instructor, and admin table
            cur.execute("SELECT * FROM {} WHERE ID = '{}'".format(table, id.upper(), id.lower()))
            user_info = cur.fetchall()
        
        if (user_info):
            remove_row(conn, table, "ID", id)
        else:
            print("No User Found!")
        conn.commit()

    def add_student_to_course(self, conn):
        cur = conn.cursor()
        student_id = input("Enter the Student ID: ")
        cur.execute("SELECT * FROM STUDENT WHERE STUDENT.ID = '{}'".format(student_id))
        student_info = cur.fetchall()
        course_crn = input("Enter the Course CRN: ")
        cur.execute("SELECT * FROM COURSES WHERE COURSES.CRN = '{}'".format(course_crn))
        course_info = cur.fetchall()

        if (student_info and course_info): #if found a course with correct crn and student with correct ID
            cur.execute("INSERT INTO SCHEDULE('STUDENT_ID', 'COURSE_ID') VALUES ('{}', '{}')".format(student_id, course_crn))
            conn.commit()
            cur.execute("SELECT COURSES.TITLE FROM COURSES WHERE COURSES.CRN = '{}'".format(course_crn))
            print("Added: " + (cur.fetchall())[0][0] + " to schedule!")
        else:
            print("Invalid student ID or course CRN")

    def remove_student_from_course(self, conn, student_id, course_crn):
        cur = conn.cursor()
        #check if user has course in their schedule
        cur.execute("SELECT * FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(student_id, course_crn))
        if (cur.fetchall()):
            cur.execute("SELECT COURSES.TITLE FROM COURSES WHERE COURSES.CRN = '{}'".format(course_crn)) #get couse title for nice printing
            print("Removed: " + (cur.fetchall())[0][0] + " from schedule!")
            cur.execute("DELETE FROM SCHEDULE WHERE STUDENT_ID = '{}' AND COURSE_ID = '{}'".format(student_id, course_crn))
            conn.commit()
        else:
            print("No such course in schedule!")
        
    def add_instructor_to_course(self, conn):
        cur = conn.cursor()
        instructor_id = input("Enter an Instructor ID: ")
        cur.execute("SELECT INSTRUCTOR.ID FROM INSTRUCTOR WHERE ID = '{}'".format(instructor_id.upper()))
        instructor_info = cur.fetchall()
        course_crn = input("Enter a Course CRN: ")
        cur.execute("SELECT COURSES.CRN FROM COURSES WHERE CRN = '{}'".format(course_crn.upper()))
        course_info = cur.fetchall()

        if(instructor_info and course_info):    #If found valid instructor ID and course CRN
            cur.execute("UPDATE COURSES SET INSTRUCTOR_ID = '{}' WHERE COURSES.CRN = '{}'".format(instructor_info, course_info))
            conn.commit()
        else:
            print("Invalid Instructor ID or Course CRN")

    def remove_instructor_from_course(self, conn):
        cur = conn.cursor()
        instructor_id = input("Enter an Instructor ID: ")
        course_crn = input("Enter a Course CRN: ")
        cur.execute("SELECT * FROM COURSES WHERE INSTRUCTOR_ID = '{}' AND COURSES.CRN = '{}'".format(instructor_id.upper(), course_crn))
        if (cur.fetchall()):
            cur.execute("UPDATE COURSES SET INSTRUCTOR_ID = NULL WHERE INSTRUCTOR_ID = '{}' AND CRN = '{}'".format(instructor_id, course_crn))
            conn.commit()
        else:
            print("No such course in schedule!")

    def print_roster(self, conn):
        cur = conn.cursor()
        crn = input("Please enter the course ID you would like to view the roster for: ")
        try:
            cur.execute("SELECT SCHEDULE.STUDENT_ID FROM SCHEDULE WHERE COURSE_ID = '{}'".format(crn.upper()))
            course_roster = cur.fetchall()
            print(course_roster)
        except:
            print("No such course!")