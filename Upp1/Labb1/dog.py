import time

class Dog(object):
    "Class to define dog objects"

    number_of_dogs = 0
    @classmethod
    def amount_of_dogs(cls):
        """ Returns the current amount of dogs """
        return cls.number_of_dogs
    def __init__(self, name, breed, age, asleep, colors):
        """ Creates a dog object """
        self.name = name
        self.breed = breed
        self.age = age
        self.asleep = asleep
        self.colors = colors
        Dog.number_of_dogs += 1
    def get_name(self):
        """ Prints the name of the dog """
        return self.name
    def __str__(self):
        """ Prints the name of the dog """
        return "\n Name: %s \n Breed: %s \n Age: %s \n Is the dog sleeping? %s \n Colors: %s" %(self.name, self.breed, self.age, self.asleep, ", ".join(self.colors))
    def is_asleep(self, dog):
        """ Checks if the dogs are sleeping, if they are, wake them up """
        if dog.asleep == True:
            print(dog.get_name(), "just woke up!")
            dog.wake_up()
        else:
            print(dog.get_name(), "is awake!")
    def wake_up(self):
        """ Sets the asleep attribute to False """
        self.asleep = False

dogs = [
Dog("Felix", "Corgi", "2", False, ["White", "Orange"]),
Dog("Victor", "Tax", "1", True, ["Brown"]),
Dog("Adam", "Boxer", "6", False, ["Brown", "White"]),
Dog("Adam", "Schäfer", "4", False, ["Brown", "Black"]),
Dog("John", "Dalmatin", "8", False, ["White", "Black"])
]

for dog in dogs:
    dog.is_asleep(dog)
    time.sleep(1)
    print(dog)
    time.sleep(1)


print("There are", Dog.number_of_dogs, "dogs in the system!")