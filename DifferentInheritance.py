'''
    Single Level Inheritance - Inheriting a single class
    Multi Level Inheritance - Inheriting a class that class in turn inherits another class
    Multiple Inheritance - Inheriting two different classes
'''


class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A): # Single Level Inheritance

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(B): # Multi Level Inheritance

    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")


class D:

    def feature7(self):
        print("Feature 7 working")

    def feature8(self):
        print("Feature 8 working")


class E(C, D): # Multiple Inheritance

    def feature9(self):
        print("Feature 9 working")

    def feature10(self):
        print("Feature 10 working")


