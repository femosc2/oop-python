from Location import Location
from Duel import Duel
from ForcePower import ForcePower
from Rank import Rank

class Program():
    """ Creates a blueprint for the program """

    def __init__(self):
        """ pass """

    def create_assets(self):
        pass

    def run(self):
        try:
            self.create_assets()
            user_input = input("Where do you wish to fight?")
            location = Location(user_input)
            while True:
                print("Welcome to the Star Wars battle simulator!")
                print("1. Add a duelist! ")
                print("2. List all Jedi ")
                print("3. List all Sith ")
                print("4. Duel! ")
                print("0. Exit")
                menu_input = input("What do you wish to do?")
                if menu_input == "1":
                    Location.add_duelists(location)
                elif menu_input == "2":
                    Location.list_jedi(location)
                elif menu_input == "3":
                    Location.list_sith(location)
                elif menu_input == "4":
                    duelist1 = Location.choose_duelists(location)
                    duelist2 = Location.choose_duelists(location)
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
