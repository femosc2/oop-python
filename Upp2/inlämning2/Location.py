from Sith import Sith
from Jedi import Jedi
from ForceWieldingDuelist import ForceWieldingDuelist
from Assets import Assets

class Location():
    """ Blueprint for creating a new location """
    def __init__(self, location_name):
        """ Method for creating a new location """
        self.location_name = location_name
        self.jedi_at_location = [
            Jedi("Luke 123", "push", "knight", "green", "single"),
            Jedi("Lol", "lightning", "knight", "blue", "single"),
            Jedi("Luke skywalker", "heal", "knight", "green", "single")
            ]
        self.sith_at_location = [
            Sith("Vader 123", "heal", "knight", "green", "single"),            
            Sith("Felix", "push", "lord", "red", "single"),
            Sith("Darth vader", "choke", "lord", "red", "single")
            ]
        self.assets = Assets()

    def add_duelists(self):
        """ Allows the user to create a new duelist and adds them to the list of available fighters """
        
        user_allegiance = str(input("Is the duelist a Jedi or a Sith? ").lower())
        while user_allegiance not in ["sith", "jedi"]:
            user_allegiance = str(input("Please choose between Jedi or Sith").lower())

        user_name = str(input("What is the name of the duelist?"))

        print("Available Force Powers!")
        for force_power in self.assets.get_force_powers():
            print(force_power.force_name.capitalize())

        loop = True    
        while loop:
            user_force_power = str(input("What force power does the duelist use?")).lower()
            for force_power in self.assets.force_powers:
                if force_power.force_name == user_force_power:
                    loop = False
                    user_force_power == force_power.force_name

        for lightsaber in ["single", "dual-wield", "double-bladed"]:
            print(lightsaber.capitalize())
        user_lightsaber_hilt = str(input("What kind of lightsaber does the duelist use?").lower())
        while user_lightsaber_hilt not in ["single", "dual-wield", "double-bladed"]:
            print("That is not available. Please choose from the following. ")
            for lightsaber in ["single", "dual-wield", "double-bladed"]:
                print(lightsaber.capitalize())
            user_lightsaber_hilt = input("What kind of lightsaber does the duelist use?").lower()
        
        user_lightsaber_color = input("What color is the lightsaber? ")
        if user_allegiance == "sith":
            print("Available ranks:")
            for rank in self.assets.get_sith_ranks():
                print(rank)
            loop = True    
            while loop:
                user_rank = input("What is the rank of the Sith?").lower()
                for rank in self.assets.sith_ranks:
                    if rank.rank_name == user_rank:
                        loop = False
            self.sith_at_location.append(Sith(user_name, user_force_power, user_rank, user_lightsaber_color, user_lightsaber_hilt))

        elif user_allegiance == "jedi":
            print("Available ranks:")
            for rank in self.assets.jedi_ranks:
                print(rank)
            loop = True    
            while loop:
                user_rank = input("What is the rank of the Jedi?").lower()
                for rank in self.assets.jedi_ranks:
                    if rank.rank_name == user_rank:
                        loop = False 
            self.jedi_at_location.append(Jedi(user_name, user_force_power, user_rank, user_lightsaber_color, user_lightsaber_hilt))

    def list_duelists(self):
        for fighter in self.sith_at_location + self.jedi_at_location:
            print(fighter)

    def choose_jedi(self):
        """ Lets the user choose a Jedi """
        for jedi in self.jedi_at_location:
            print(jedi.name.capitalize())
        choose_your_fighter = input("Who do you wish to pick?").capitalize()
        loop = True
        while loop:
            for jedi in self.jedi_at_location:
                if jedi.name == choose_your_fighter:
                    loop = False
                    return jedi
                
    def choose_sith(self):
        """ Lets the user choose a sith """
        for sith in self.sith_at_location:
            print(sith.name.capitalize())
            
        choose_your_fighter = input("Who do you wish to pick?").capitalize()

        loop = True
        while loop:
            for sith in self.sith_at_location:
                if sith.name == choose_your_fighter:
                    loop = False
                    return sith