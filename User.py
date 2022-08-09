from database_functions import *
class User:
    def __init__(self, id = "W00000000", first_name = "First Name", last_name = "Last Name", email = "Email"):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
    
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_id(self, new_id):
        self.id = new_id
    
    def show_info(self):
        print (self.first_name)
        print(self.last_name)
        print(self.id)

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
        
    def edit_info(self):
        
        while True:
            user_input = input(
"""
What information would you like to edit?:
First Name(1)   Last Name(2)
ID(3)           Back(0)
Input: """)
            if (user_input == '1'):
                print("What would you like to change your first name to?")
                self.set_first_name(input("New First Name: "))
            elif (user_input == '2'):
                print("What would you like to change your last name to?")
                self.set_last_name(input("New Last Name: "))
            elif (user_input == '3'):
                print("What would you like to change your id to?")
                self.set_id(input("New ID: "))
            elif (user_input == '0'):
                return
            else:
                print("Invalid Option")
