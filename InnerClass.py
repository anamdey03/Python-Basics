class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)
        self.lap.show()

    class Laptop:
        # brand = 'Dell'
        # cpu = 'i5'
        # ram = 8

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)

        # @classmethod
        # def show(cls):
        #     print(cls.brand, cls.cpu, cls.ram)


lap1 = Student.Laptop()
lap1.show()

s1 = Student('Anamitra', 2)
s1.show()
