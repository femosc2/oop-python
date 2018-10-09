from animal import Animal
from person import Person
from frequentVisitor import FrequentVisitor
from oneTimeVisitor import OneTimeVisitor
from zooKeeper import ZooKeeper
from lion import Lion
from hippo import Hippo
from giraffe import Giraffe

class Zoo():
    """ pass """
    frequentVisitors = []
    oneTimeVisitors = []
    workers = []
    animals = []
    def __init__(self):
        """ pass """
    def listAnimals(self):
        print("There are", Animal.numberOfAnimals())
    def createAnimals():
        """ lol"""
        animal = True
        while animal:
            name = input("What is the name of the animal")
            type_of_food = input("What does the animal eat?")
            rating = input("What rating does the animal have?")
            species = input("What species is the animal?")

            if species == "Lion":
                Zoo.animals.append(Lion(name, type_of_food, rating))
            elif species == "Giraffe":
                Zoo.animals.append(Giraffe(name, type_of_food, rating))
            else:
                Zoo.animals.append(Hippo(name, type_of_food, rating))

            isThereMoreAnimals = input("Are there more animals to be added? ")
            if isThereMoreAnimals == "n":
                animal = False
    def visitorEnter():
        queue = True
        while queue:
            membership = input("Is this visitor a member? y or n")
            age = input("How old is the visitor?")
            timestamp = input("What time did the visitor enter the zoo?")
            if membership == "y":
                id = input("What is the visitors id?")
                name = input("A new visitor is visiting the zoo! What is his name?")
                Zoo.frequentVisitors.append(FrequentVisitor(name, id, timestamp, age))
            else:
                Zoo.oneTimeVisitors.append(OneTimeVisitor(timestamp, age))
            isThereAQueue = input("Are there more people in the queue? ")
            if isThereAQueue == "n":
                queue = False
    def printPeople():
        visitors = Zoo.frequentVisitors + Zoo.oneTimeVisitors
        for visitor in visitors:
            print("Visitor:", visitor)
        for worker in workers:
            print(worker)
    def printAnimals():
        for animal in Zoo.animals:
            print(animal)
    def createWorker():
        name = input("How old is the worker?")
        emp_id = input("What is the employees id?")
        age =  input("How old is the worker?")
        Zoo.worker.append(ZooKeeper(age, emp_id, name))
    
            


        
