class Person:

    def __init__(self):
        self.name = "Anamitra"
        self.age = 20

    def compare(self, person):
        if self.name == person.name and self.age == person.age:
            return True
        else:
            return False


person1 = Person()
person2 = Person()


if person1.compare(person2):
    print("They are same")
