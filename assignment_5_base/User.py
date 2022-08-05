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

    def search_course(conn):
        search_courses(conn)
        
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
