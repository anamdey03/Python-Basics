
class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):

    def __init__(self):
        super().__init__()
        print("in B Init")

    def feature1(self):
        print("Feature 1 working")

    def feature4(self):
        print("Feature 4 working")


b = B()