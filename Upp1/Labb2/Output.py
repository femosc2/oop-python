class Output():
    """
    Blueprint for what output should be shown to the user
    """

    def __init__(self):
        """
        Initializes the Output class
        """
        self.divider = "----" * 5

    def get_main_menu(self):
        """
        Shows a menu to the user
        """
        choice_1 = "1. Add product"
        choice_2 = "2. View all products"
        choice_3 = "3. View a product"
        choice_4 = "4. Exit"

        return "%s\n%s\n%s\n%s\n%s\n%s\n" % (self.divider,
                                             choice_1,
                                             choice_2,
                                             choice_3,
                                             choice_4,
                                             self.divider)

    def get_products_list(self, products):
        """
        Shows the products
        """
        output = ""
        output += self.divider + "\n"

        for product in products:
            output += str(product) + "\n"

        output += self.divider + "\n"

        return output

    def get_product_information(self, product):
        """
        Outputs the attributes of the product
        """
        if product is None:
            return "The chosen product does not exist!\n"

        return "\n%s\n%s\n%s\n" % (self.divider,
                                   str(product),
                                   self.divider)
