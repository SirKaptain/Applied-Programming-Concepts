from User import User

class Student(User):

    def __init__(self, first_name="First Name", last_name="Last Name", id="W00000000"):
        super().__init__(first_name, last_name, id)
        self.courses = []
        self.schedule = []

    def search_course(self):
        print("Search course for Student!")
        #leave empty for all courses
    def add_course(self):
        print("Add Course for Student!")
    def drop_course(self):
        print("Drop Course for Student!")
    def print_schedule(self):
        print("Print Schedule for Student!")