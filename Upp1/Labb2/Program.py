# Import dependencies
from Input import Input
from Output import Output
from Inventory import Inventory

class Program():
    """
    Creates a blueprint for a program
    """

    def __init__(self):
        """
        creates a new program
        """
        self.input = Input()
        self.output = Output()
        self.inventory = Inventory()
        self.choice = None

    def run(self):
        """
        runs the program
        """
        print("\nWelcome!")

        while self.choice != 4:
            # Prints the main menu
            print(self.output.get_main_menu())

            self.choice = self.input.get_choice_in_range(4)

            if self.choice == 1:

                new_product = self.inventory.create_product()
                self.input.set_product_properties(new_product)
                self.inventory.add_product(new_product)

            elif self.choice == 2:

                products = self.inventory.get_products()
                print(self.output.get_products_list(products))

            elif self.choice == 3:

                product_name = self.input.get_input_as_str("Enter product name: ")
                product = self.inventory.get_product(product_name)
                print(self.output.get_product_information(product))


# Starts everything
if __name__ == "__main__":
    program = Program()
    program.run()
