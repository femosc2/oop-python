# Import dependencies
from Product import Product

# Software (subclass)
class Software(Product):
    """
    Creates a blueprint for the software of a product
    """

    def __init__(self, software_type=""):
        """
        Creates the software
        """
        # Subclass specific attribute
        self.software_type = software_type

    def set_type(self, software_type):
        """
        sets the type of the software
        """
        self.software_type = software_type

    def get_type(self):
        """
        returns the type of the software
        """
        return self.software_type

    def __str__(self):
        """
        Formats the print of the software
        """
        return "%s - %s, %s, %s (%s)" % (self.name,
                                         self.manufacturer,
                                         self.category,
                                         self.software_type,
                                         str(self.price))

    def convert_to_csv(self):
        """
        Converts all the product information
        to the CSV format so we can store the
        information in a textfile and then retrieve it
        """
        return "%s,%s,%s,%s,%s" % (self.name,
                                   self.manufacturer,
                                   self.category,
                                   self.software_type,
                                   str(self.price))
