'''
    Instance Methods (Accessor & Mutator) - Dependence on instance variables
    Class Methods - Dependence on class variables
    Static Methods - No dependence on class or instance variables
'''


class Student:

    school = "Auxilium"

    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

    @classmethod
    def get_school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a student class")


s1 = Student(12, 31, 54)

print(s1.average())
print(Student.get_school_name())

Student.info()
