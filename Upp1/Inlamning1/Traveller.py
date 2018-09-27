from Ticket import Ticket
from Luggage import Luggage

class Traveller():
    """ Creates the blueprint for a traveller """
    def __init__(self, name, age):
        """ Creates a new traveller object """
        self.name = name
        self.age = age
        self.ticket = Ticket(True, 123)
        self.luggage = Luggage(20, 10, 10)

    def putLuggageOnScale(self, luggage):
        """ The traveller puts the luggage on the scale """
        pass
    def scanTicket(self, ticket):
        """ The user scans their ticket """
        pass
        