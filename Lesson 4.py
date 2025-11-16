# #class Human:
#     #height = 170

# #class Student(Human):
#     #money = 0

# #class Worker(Human):
#     #money = 50

# #nick = Student()
# #ann = Worker()
# #print(ann.height)
# #print(nick.height)


# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60

# class parent(Grandparent):
#     age = 40

# class Child(parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)

# nick = Child()



# class Hello_world:
#     hello = "hello"
#     _hello = "_hello"
#     __hello = "__hello"
#     def __init__(self):
#         self.world = "world"
#         self._world = "_world"
#         self.__world = "__world"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)

# class Hi(Hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)

# hello = Hello_world()





# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10

# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)

# hello = Class1()


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 256
    def calculate(self):
        print("Calculating...")

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"
    def display(self):
        print("I display the image on the screen...")


class Phone(Display, Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)

phone = Phone()
phone.calculate()
phone.display()
phone.print_info()




