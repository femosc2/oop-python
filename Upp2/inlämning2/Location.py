from Sith import Sith
from Jedi import Jedi
from ForceWieldingDuelist import ForceWieldingDuelist
from Assets import Assets

class Location():
    """ Blueprint for creating a new location """
    def __init__(self, location_name):
        """ Method for creating a new location """
        self.location_name = location_name
        self.assets = Assets()
        self.jedi_at_location = []
        self.sith_at_location = []

    def add_duelists(self):
        """ Allows the user to create a new duelist and adds them to the list of available fighters """
        
        user_allegiance = str(input("Is the duelist a Jedi or a Sith? ").lower())
        while user_allegiance not in ["sith", "jedi"]:
            user_allegiance = str(input("Please choose between Jedi or Sith").lower())

        user_name = str(input("What is the name of the duelist?"))

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
        for fighter in self.jedi_at_location + self.sith_at_location:
            print(fighter)
            print("-"*40)

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
                else:
                    choose_your_fighter = input("Who do you wish to pick?").capitalize()
                
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
                else:
                    choose_your_fighter = input("Who do you wish to pick?").capitalize()
