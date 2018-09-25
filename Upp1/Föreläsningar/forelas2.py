import time

#Inheritence

#Inheritence is a way to stop rewriting the same code

#Inheritence between parent classes (veichle)and children classes (taxi, bus, truck etc)

# 1. Create a parent class with the common attributes and common methods

# 2. Create Child classes eg bus and taxi with extended atributes and extend methods

#class Vehicle():
    #""" My class"""
    #def __init__(self, driver_name, wheels, seats):
        #self.driver_name = driver_name
        #self.wheels = wheels
        #self.seats = seats

#class Taxi(Vehicle):
    #"Class which inherits Veichle"
    #def __init__(self, driver_name, wheels, seats, on_duty):
        #super().__init__(self, driver_name, wheels, seats)
        #self.on_duty = on_duty


#MEthod overriding is an object-oriented porgramming feature that allows a subclass to rpovcie a different implementation
#In situations where i want to tailor the behaviour of my children different from the parent
class Humans():
    "Class creating a Human"
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return "Hi, my name is {name}".format(name=self.first_name)

class Student(Humans):
    "Class which inherits humans"
    def __init__(self, first_name, last_name, skype):
        super().__init__(first_name, last_name)
        self.skype = skype
    def __str__(self):
        return super().__str__() + " and I'm a student"

class Researcher(Humans):
    """ Researcher class which inherits Humans """
    def __init__(self, first_name, last_name, degree):
        super().__init__(first_name, last_name)
        self.degree = degree
    def __str__(self):
        return super().__str__() + " and I'm a researcher"

def test():
    s1 = Student("Frida", "Studentsson",  "frida32")
    r1 = Researcher("Lars", "Forskaresson", "PhD")
    h1 = Humans("Olof", "Efternamnsson")


    print(s1)
    print(r1)
    print(h1)

test()

