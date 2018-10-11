class Product():
    """ Blueprint for an Product """
    def __init__(self, price, name, id):
        """ Creates a new Product object """
        self.price = price
        self.name = name
        self.id = id
    def __str__(self):
        return "name: {name}, price: {price}, id: {id}".format(name=self.name, price=self.price, id=self.id)