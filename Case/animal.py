class Animal():
    """
        Klass för djur
    """
    numberOfAnimals = 0
    @classmethod
    def how_many(cls):
        return cls.numberOfAnimals
    def __init__(self, rating, type_of_food, name):
        self.rating = rating
        self.type_of_food = type_of_food
        self.name = name
        Animal.numberOfAnimals =+ 1