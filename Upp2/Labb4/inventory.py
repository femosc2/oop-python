from product import Product
from usb import Usb

class Inventory():
    """ Blueprint for an Inventory """
    def __init__(self):
        """ Creates a new Inventory object """
        self.products = []
        
    def addProduct(self):
        """ adds a product to the inventory """
        name = str(input("What is the name of the product? "))
        price = int(input("What is the price of the product? "))
        id = int(input("What is the id of the product? "))
        type = str(input("What is the type of the product? "))
        if type == "usb":
            gb = int(input("How large is the USB? "))
            usb = Usb(price, name, id, gb )
            self.products.append(usb)
        else:
            print("Wrong store mang. ")


    def sellProduct(self):

        for product in self.products:
            print(self.products.index(product))
        
        userInput = int(input("What product id do you wish to sell "))

        for product in self.products:
            if userInput == int(product.id):
                self.products.remove(userInput)


    def returnInventory(self):
        """ returns the Inventory list """
        return self.products
    def showInventory(self):
        for product in self.products:
            print(product)
        
