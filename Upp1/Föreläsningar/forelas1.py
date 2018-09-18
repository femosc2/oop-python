# Introduction to Object Oriented Programming in Python

# OOP = easy to reuse written code

# Object in python is a representation of ap rsonl a place, a bank, a car or any item a program should handle.

# Example object data (name, cities, passangers), method (pickUp, dropOff, setDriverName)

# Classes are the blueprints for a new data type in your program.



class Computer(object):
    "Class to define a computer"
    def __init__(self, computerColor, computerBrand, computerSize):
        self.color = computerColor
        self.brand = computerBrand
        self.size = computerSize
    def changeColor(self, newComputerColor):
        self.color = newComputerColor

class Bus(object):
    
    numberOfBuses = 0
    @classmethod
    def how_many(cls):
        """ return current amount of busses """
        return cls.numberOfBuses
    def __init__(self, passengers, route, onDuty, driverName, seats):
        self.passengers = passengers
        self.route = route
        self.onDuty = onDuty
        self.driver = driverName
        self.seats = seats
        Bus.numberOfBuses += 1;
    def letOnPassengers(self, newPassengers):
        if newPassengers > self.seats:
            print("The bus can not fit that many passengers!")
        else:
            self.passengers += newPassengers
    def letOffPassengers(self, leavingPassengers):
        self.passengers -= leavingPassengers
        if self.passengers <= 0:
            self.passengers = 0
    def changeDriver(self, newDriverName):
        self.driver = newDriverName
    def changeRoute(self, newRoute):
        self.route = newRoute

def bus():
    firstBus = Bus(10, "Värnhem till Västra Hamnen", True, "Felix", 30)
    secondBus = Bus(22, "Kronprinsen till Västra Hamnen", True, "Jens", 45)

    print("Amount of passengers on the first bus:", firstBus.passengers)
    print("Is the second bus on duty?", secondBus.onDuty)
    print("Number of Buses:", Bus.numberOfBuses)


def computer():
    myFirstComputer = Computer("Grey", "Apple", 13)
    mySecondComputer = Computer("Black", "Lenovo", 15)
    myFirstComputer.changeColor("white")
    print("The color of my first computer is", myFirstComputer.color)
    print("The brand of my second computer is", mySecondComputer.brand)

bus()
    


# Bus klassdiagram
    # Attributes
        # driverName
        # passengers
        # route
        # onDuty
    # Methods
        # letOnPassengers
        # changeDriver
        # changeRoute