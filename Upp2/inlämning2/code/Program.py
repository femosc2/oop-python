from Location import Location
from Duel import Duel
from Rank import Rank

class Program():
    """ Creates a blueprint for the program """

    def __init__(self):
        """ Not used """

    def run(self):
        """ Method which shows a menu and allows the user to do inputs for selecting what action he or she wants to do """

        try:
            user_input = input("Where do you wish to fight?") #The user decides where he or she wants to fight
            location = Location(user_input)
            while True:
                print("Welcome to the Star Wars battle simulator!")
                print("1. Add a duelist! ")
                print("2. List all duelists! ")
                print("3. Duel! ")
                print("0. Exit")
                menu_input = input("What do you wish to do?")
                if menu_input == "1":
                    location.add_duelists()
                elif menu_input == "2":
                    location.list_duelists()
                elif menu_input == "3":
                    duelist1 = location.choose_jedi()
                    duelist2 = location.choose_sith()
                    Duel(duelist1, duelist2).duel()
                elif menu_input == "0":
                    print("-"*40)
                    print(" May the force be with you!")
                    print("-"*40)
                    quit()
                
        except KeyboardInterrupt: # removes the error text when the user uses keyboard shortcuts to exit the program
            print("\n", "-"*40)
            print(" May the force be with you!")
            print("-"*40)
            quit()


if __name__ == "__main__": #runs the program
    program = Program()
    program.run()
