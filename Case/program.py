from zoo import Zoo

class Program():
    """ lol """
    def __init__(self):
        """ asd """

    def menu():
        while True:
            print("-"*40)
            menuInput = input("1. Add visitor to park, 2. Add animal to park, 3. Show all people in the park, 4. Print all animals.")
            if menuInput == "1": 
                Zoo.visitorEnter()
            elif menuInput == "2":
                Zoo.createAnimals()
            elif menuInput == "3":
                Zoo.createWorker()
            elif menuInput == "4":
                Zoo.printPeople()
            elif menuInput == "5":
                Zoo.printAnimals()
            else:
                print("lool")


if __name__ == "__main__":
    Program.menu()