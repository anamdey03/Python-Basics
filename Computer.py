class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram)


com1 = Computer("i5", "16gb")
print(id(com1))
com1.config()
