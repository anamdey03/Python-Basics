'''
    Duck Typing -
    Operator Overloading -
    Method Overloading -
    Method Overriding -
'''


# Duck Typing
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Intellij:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = Intellij()

lap1 = Laptop()
lap1.code(ide)


# Operator Overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        student = Student(m1, m2)
        return student

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        student = Student(m1, m2)
        return student

    def __ge__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 >= r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(10, 40)
s2 = Student(40, 10)

s3 = s1 + s2
s4 = s1 - s2

print(s3.m1)
print(s4.m2)

if s1 >= s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)


# Method Overloading
# Direct method Overloading is not supported in Python
class Sum:

    def sum(self, a=None, b=None, c=None):
        result = 0
        if a != None and b != None and c != None:
            result = a + b + c
        elif a != None and b != None:
            result = a + b
        else:
            result = a
        return result


s = Sum()
print(s.sum(10, 20, 30))
print(s.sum(10, 20))
print(s.sum(10))


# Method Overriding

class SuperClass:

    def show(self):
        print("in Super Class")


class SubClass(SuperClass):
    def show(self):
        super().show()
        print("in Sub Class")


sub_class = SubClass()
sub_class.show()
