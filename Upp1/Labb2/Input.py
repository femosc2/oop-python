class Input():
    """ A blueprint for the class Input """

    def __init__(self):
        """ init not used but required for OOP python """
        """
        Not used
        """
        pass
    
    def get_choice_in_range(self, r=1):
        """
        Gets input from user, while the users input is invalid it prompts the user for a new number
        """
        user_input = None

        while user_input not in list(range(1, r + 1)):
            user_input = input("Your choice: ")

            if user_input.isdigit():
                user_input = int(user_input)

        return user_input

    def get_input_as_str(self, message):
        """
        Returns the message the user puts in
        """
        return input(message)

    def get_input_as_number(self, message):
        """
        Tries to convert user input to an integer or float
        """
        user_input = None

        while type(user_input).__name__ not in ["int", "float"]:

            user_input = input(message)

            try:
                user_input = float(user_input) if "." in user_input else int(user_input)
            except ValueError:
                print("The input has to be a numeric value!")

        return user_input

    def set_product_properties(self, product):
        """
        Defines the attribute of an object
        """
        # Sets the product name 
        product.set_name(self.get_input_as_str("Enter name: "))
        # Sets the product manufacturer
        product.set_manufacturer(self.get_input_as_str("Enter manufacturer: "))
        # Sets the product type
        product.set_type(self.get_input_as_str("Enter software type: "))
        # Sets the product price
        product.set_price(self.get_input_as_number("Enter price: "))
        # ?
        product.set_category(product.__class__.__name__)
