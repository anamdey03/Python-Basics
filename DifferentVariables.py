'''
    Instance Variable
    Class or Static Variable
'''


class Car:
    wheel = 4  # class or static variable

    def __init__(self):
        self.mileage = 10
        self.company = "BMW"


c1 = Car()
c2 = Car()

c1.mileage = 8

print(c1.mileage, c1.company, c1.wheel)
print(c2.mileage, c2.company, c2.wheel)
