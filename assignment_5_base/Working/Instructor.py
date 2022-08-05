from User import User

class Instructor(User):

    def __init__(self, first_name="First Name", last_name="Last Name", id="W00000000"):
        super().__init__(first_name, last_name, id)
        self.schedule = []
        self.classlist = []

    def print_schedule(self):
        print("Print Schedule for Instructor!")
    def print_classlist(self):
        print("Print Classlist for Instructor!")
    def search_course(self):
        print("Search course for Instructor!")