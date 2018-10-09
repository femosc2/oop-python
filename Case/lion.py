from animal import Animal
class Lion(Animal):
    """
        Klass för lejon
    """

    def __init__(self, rating, type_of_food, name):
        super().__init__(rating, type_of_food, name)

    def __str__(self):
        return "Lion: {name}, rating {rating}, favourite type of food {food}".format(name=self.name, rating=self.rating, food=self.type_of_food) 