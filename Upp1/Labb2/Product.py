# Product (base class)
class Product():
    """
    Creates a blueprint for the product
    """

    def __init__(self, name="", manufacturer="", category="", price=0):
        """
        Initializes a product with the values, name, manufracturer, category and price
        """
        self.name = name
        self.manufacturer = manufacturer
        self.category = category
        self.price = price

    def set_name(self, name):
        """
        sets the name of the product
        """
        self.name = name

    def get_name(self):
        """
        returns the nameof a product
        """
        return self.name

    def set_manufacturer(self, manufacturer):
        """
        sets the name of the manufacturer
        """
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        """
        returns the name of the manufacturer
        """
        return self.manufacturer

    def set_category(self, category):
        """
        sets the category of the product
        """
        self.category = category

    def get_category(self):
        """
        returns the category of the product
        """
        return self.category

    def set_price(self, price):
        """
        sets the price of the product
        """
        self.price = price

    def get_price(self):
        """
        returns the priuce of the product
        """
        return self.price
