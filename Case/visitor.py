from person import Person

class Visitor(Person):
    """ time """
    numberOfPersons = 0
    @classmethod
    def how_many(cls):
        return cls.numberOfPersons
    def __init__(self, age, timestamp):
        super().__init__(age)
        self.timestamp = timestamp
    def setRating(self):
        """ Gives an animal a rating"""
        int(input("Give an animal a rating"))
        