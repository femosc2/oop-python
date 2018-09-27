from Software import Software

class Inventory():
    """
    """

    def __init__(self):
        """
        Not used
        """
        pass

    def create_product(self):
        """
        Creates a new product
        """
        product = Software()
        return product

    def add_product(self, product):
        """
        Gets a product from the txt file, reads it and allows the user to append the product to the list
        """
        line = product.convert_to_csv() + "\n" 

        # Open "products.txt" and append "line" (the product)
        # then close the file
        with open("products.txt", "a") as f:
            f.write(line)
        f.close()

    def get_product(self, choice):
        """
        Gets a product, choose what product you want as the choice parameter
        """
        with open("products.txt") as f:
            # Split the file by each line and
            # store them as a list in "lines"
            lines = f.read().splitlines()
        f.close()

        products = []

        # Loop through all lines in the file
        for line in lines:
            # All data for each product is divided by a comma
            # split by that character to get a list of values
            # in the format [name, manufacturer, category, etc.]
            products.append(line.split(","))

        found_product = None

        # Loop through all products
        for product in products:
            if product[0] == choice:
                found_product = product

        if found_product:
            software = Software()
            software.set_name(found_product[0])
            software.set_manufacturer(found_product[1])
            software.set_category(found_product[2])
            software.set_type(found_product[3])
            software.set_price(found_product[4])
            return software

        return None

    def get_products(self):
        """
        Get all products from the txt file and puts them nicely formatted into a list
        """
        with open("products.txt") as f:
            # Split the file by each line and
            # store them as a list in "lines"
            lines = f.read().splitlines()
        f.close()

        products = []

        for line in lines:
            # All data for each product is divided by a comma
            # split by that character to get a list of values
            # in the format [name, manufacturer, category, etc.]
            product = line.split(",")
            software = Software()
            software.set_name(product[0])
            software.set_manufacturer(product[1])
            software.set_category(product[2])
            software.set_type(product[3])
            software.set_price(product[4])
            products.append(software)

        # We could possibly sort the list here

        return products
