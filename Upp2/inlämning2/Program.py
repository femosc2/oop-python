from Location import Location
from Duel import Duel
from ForcePower import ForcePower
from Rank import Rank
from Assets import Assets

class Program():
    """ Creates a blueprint for the program """

    def __init__(self):
        """ pass """

    def run(self):
        try:
            user_input = input("Where do you wish to fight?")
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
                
        except KeyboardInterrupt:
            print("\n", "-"*40)
            print(" May the force be with you!")
            print("-"*40)
            quit()
if __name__ == "__main__":
    program = Program()
    program.run()
