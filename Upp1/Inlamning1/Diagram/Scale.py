from Luggage import Luggage

class Scale():
    """ A blueprint for a scale """
    def __init__(self, model):
        """ Creates a scale """
        self.model = model

    def sendWeight(self, weight):
        """ Weighs the luggage """
        pass
    def weightLuggage(self, luggage):
        """ Weighs the luggage and returns the weight as an int """
        pass