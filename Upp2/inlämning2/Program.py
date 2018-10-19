from Location import Location
from Duel import Duel
from ForcePower import ForcePower
from Rank import Rank
from Sith import Sith ###GLÖM INTE TA BORT
from Jedi import Jedi  ###GLÖM INTE TA BORT

class Program():
    """ Creates a blueprint for the program """
    def __init__(self):
        """ pass """
        self.jedi_at_location = [Jedi("Lol", "lightning", "knight", "blue", "single")]
        self.sith_at_location = [Sith("Felix", "push", "lord", "red", "single")]

    def create_assets(self):
        pass
    def run(self):
        try:
            self.create_assets()
            user_input= input("Where do you wish to fight?")
            Location(user_input)
            while True:
                print("Welcome to the Star Wars battle simulator!")

                print("1. Add a duelist! ")
                print("2. List all Jedi ")
                print("3. List all Sith ")
                print("4. Duel! ")
                print("0. Exit")

                menu_input = input("What do you wish to do?")
                if menu_input == "1":
                    Location.add_duelists(self)
                if menu_input == "2":
                    Location.list_jedi(self)
                if menu_input == "3":
                    Location.list_sith(self)
                if menu_input == "4":
                    duelist1 = Location.choose_duelists(self)
                    duelist2 = Location.choose_duelists(self)
                    Duel(duelist1, duelist2).duel()
        except KeyboardInterrupt:
            print("\n", "-"*40)
            print(" May the force be with you!")
            print("-"*40)
            quit()


if __name__ == "__main__":
    program = Program()
    program.run()

        
