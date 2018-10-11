from product import Product

class Usb(Product):
    """ Blueprint for an USB """
    def __init__(self, price, name, id, gb):
        """ Creates a new USB object """
        super().__init__(price, name, id)
        self.gb = gb
    def __str__(self):
        return super().__str__() + "gb: {gb} ".format(gb=self.gb) 