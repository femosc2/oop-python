from shop import Shop

class Menu():
    """ Blueprint for a menu """
    def __init__(self):
        """ pass """
        pass
    def printMenu():
        shopName = input("What is the name of the shop?")
        shopLocation = input("What is the location of the shop")
        s1 = Shop(shopName, shopLocation)
        while True:
            print("-"*40)
            print("1. Add Product ")
            print("2. Sell Product ")
            print("3. Show Products ")
            print("4. Exit ")

            userInput = int(input("Choose a menu option."))

            if userInput == 1:
                s1.inventory.addProduct()
            elif userInput == 2:
                s1.inventory.sellProduct()
            elif userInput == 3:
                s1.inventory.showInventory()
            elif userInput == 4:
                quit()
            else:
                pass
                

