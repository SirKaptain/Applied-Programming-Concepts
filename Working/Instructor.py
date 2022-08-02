from User import User

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

    def print_schedule(self):
        print("Print Schedule for Instructor!")
    def print_classlist(self):
        print("Print Classlist for Instructor!")
    def search_course(self):
        print("Search course for Instructor!")