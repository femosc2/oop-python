from Sith import Sith
from Jedi import Jedi
from ForceWieldingDuelist import ForceWieldingDuelist
from Assets import Assets

class Location():
    """ Blueprint for creating a new location """
    
    def __init__(self, location_name):
        """ Method for creating a new location """

        self.location_name = location_name # Name of the Location
        self.assets = Assets() # Loads the assets of the program
        self.jedi_at_location = [
            Jedi("Luke Skywalker", "push", 1, "master", 3),
            Jedi("Bastila Shan", "battle meditation", 3, "padawan", 1), # List of Jedi at Location
            Jedi("Anakin Skywalker", "choke", 2, "knight", 2)           # Example Jedi already added to list
        ]

        self.sith_at_location = [
            Sith("Darth Revan", "lightning", 3, "lord", 3),
            Sith("Darth Vader", "choke", 2, "lord", 3),    # List of Sith at Location
            Sith("Darth Maul", "push", 1, "apprentice", 1) # Example Sith already added to list
            
        ]

    def add_duelists(self):
        """ Allows the user to create a new duelist and adds them to the list of available fighters """
        
        user_allegiance = str(input("Is the duelist a Jedi or a Sith? ").lower())
        while user_allegiance not in ["sith", "jedi"]:
            user_allegiance = str(input("Please choose between Jedi or Sith").lower())

        user_name = str(input("What is the name of the duelist?")).title()

        print("Available Force Powers!")
        for force_power in self.assets.force_powers:
            print(force_power.force_name.capitalize())

        loop = True    
        while loop:
            user_force_power = str(input("What force power does the duelist use?")).lower()
            for force_power in self.assets.force_powers:
                if force_power.force_name == user_force_power:
                    loop = False
                    user_force_power = force_power.force_name
                    force_strenght = force_power.get_force_strenght()

        if user_allegiance == "sith":
            print("Available ranks:")
            for rank in self.assets.sith_ranks:
                print(rank)
            loop = True    
            while loop:
                user_rank = input("What is the rank of the Sith?").lower()
                for rank in self.assets.sith_ranks:
                    if rank.rank_name == user_rank:
                        rank_strenght = rank.get_rank_strenght()
                        loop = False
            self.sith_at_location.append(Sith(user_name, user_force_power, force_strenght, user_rank, rank_strenght))

        elif user_allegiance == "jedi":
            print("Available ranks:")
            for rank in self.assets.jedi_ranks:
                print(rank)
            loop = True    
            while loop:
                user_rank = input("What is the rank of the Jedi?").lower()
                for rank in self.assets.jedi_ranks:
                    if rank.rank_name == user_rank:
                        rank_strenght = rank.get_rank_strenght()
                        loop = False 
            self.jedi_at_location.append(Jedi(user_name, user_force_power, force_strenght, user_rank, rank_strenght))

    def list_duelists(self):
        """ Lists all the available duelists """

        for fighter in self.jedi_at_location + self.sith_at_location:
            print(fighter)
            print("-"*40)

    def choose_jedi(self):
        """ Lets the user choose a Jedi """

        for jedi in self.jedi_at_location:
            print(jedi.name.title())
        choose_your_fighter = input("Who do you wish to pick?").title()
        loop = True
        while loop:
            for jedi in self.jedi_at_location:
                if jedi.name == choose_your_fighter:
                    loop = False
                    return jedi
            else:
                choose_your_fighter = input("Who do you wish to pick?").title()
                
    def choose_sith(self):
        """ Lets the user choose a sith """

        for sith in self.sith_at_location:
            print(sith.name.title())
            
        choose_your_fighter = input("Who do you wish to pick?").title()
        loop = True
        while loop:
            for sith in self.sith_at_location:
                if sith.name == choose_your_fighter:
                    loop = False
                    return sith
            else:
                choose_your_fighter = input("Who do you wish to pick?").title()
