class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def to_string(self):
        print("Name is: " + self.name)
        print("Major is: " + self.major)
        print("GPA is: " + str(self.gpa))

    # Class function
    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
