# Python by default doesn't support abstraction, ABC - Abstract Base Classes

from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("it's running")


class Desktop(Computer):

    def process(self):
        print("it's building")

    def write(self):
        print("it's writing")


class Programmer:

    def work(self, com):
        print("Solving Bugs")
        com.process()


com1 = Laptop()
com2 = Desktop()

prog = Programmer()
prog.work(com2)
