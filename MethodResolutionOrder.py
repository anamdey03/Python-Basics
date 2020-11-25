'''
    MRO- Method Resolution Order means always checks from left to write in case
    a class is inheriting multiple classes
'''

class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print("in B Init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("in C Init")

    def feat(self):
        super().feature2()


c = C()
c.feature1()
c.feat()
