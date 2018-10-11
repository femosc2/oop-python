from inventory import Inventory

class Shop():
    """ Blueprint for a Shop """

    def __init__(self, name, location):
        """ Creates a new Shop """
        self.name = name
        self.location = location
        self.inventory = Inventory()
