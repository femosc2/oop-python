from Sith import Sith
from Jedi import Jedi
from ForceWieldingDuelist import ForceWieldingDuelist

class Location():
    """ Blueprint for creating a new location """
    def __init__(self, location_name):
        """ Method for creating a new location """
        self.location_name = location_name
        self.jedi_at_location = [
            Jedi("Luke123", "push", "knight", "green", "single"),
            Jedi("Lol", "lightning", "knight", "blue", "single"),
            Jedi("Lukeskywalker", "heal", "knight", "green", "single")
            ]
        self.sith_at_location = [
            Sith("Vader123", "heal", "knight", "green", "single"),            
            Sith("Felix", "push", "lord", "red", "single"),
            Sith("Darthvader", "choke", "lord", "red", "single")
            ]
    def add_duelists(self):
        """ Allows the user to create a new duelist and adds them to the list of available fighters """
        user_allegiance = input("Is the duelist a Jedi or a Sith? ").lower()
        while user_allegiance not in ["sith", "jedi"]:
            user_allegiance = input("Please choose between Jedi or Sith").lower()
        user_name = str(input("What is the name of the duelist?"))
        print("Available force powers: ")
        print("Lightning ")
        print("Battle Meditation ")
        print("Choke ")
        print("Heal ")
        print("Push ")
        user_force_power = input("What force power does the duelist use?").lower()
        while user_force_power not in ["lightning", "battle meditation", "choke", "heal", "push"]:
            print("Please choose an available force power! ")
            user_force_power = input("What force power does the duelist use?").lower()
        print("Lightsabers: ")
        print("Single ")
        print("Dual-wield")
        print("Double-bladed")
        user_lightsaber_hilt = str(input("What kind of lightsaber does the duelist use?").lower())
        while user_lightsaber_hilt not in ["single", "dual-wield", "double-bladed"]:
            print("That is not available. Please choose from the following. ")
            print("Lightsabers: ")
            print("Single ")
            print("Dual-wield ")
            print("Double-bladed ")
            user_lightsaber_hilt = input("What kind of lightsaber does the duelist use?").lower()
        
        user_lightsaber_color = input("What color is the lightsaber? ")
        if user_allegiance == "sith":
            print("Available ranks:")
            print("Lord")
            print("Marauder")
            print("Apprentice")
            user_rank = input("What is the rank of the Sith?").lower()
            while user_rank not in ["lord", "apprentice", "marauder"]:
                print("Available ranks:")
                print("Lord")
                print("Marauder")
                print("Apprentice")
                user_rank = input("What is the rank of the Sith?").lower()
            self.sith_at_location.append(Sith(user_name, user_force_power, user_rank, user_lightsaber_color, user_lightsaber_hilt))
        elif user_allegiance == "jedi":
            print("Available ranks:")
            print("Master")
            print("Knight")
            print("Padawan")
            user_rank = input("What is the rank of the Jedi?").lower()
            while user_rank not in ["master", "padawan", "knight"]:
                print("Available ranks:")
                print("Master")
                print("Knight")
                print("Padawan")
                user_rank = input("What is the rank of the Jedi?").lower()
            self.jedi_at_location.append(Jedi(user_name, user_force_power, user_rank, user_lightsaber_color, user_lightsaber_hilt))

    def list_duelists(self):
        for fighter in self.sith_at_location + self.jedi_at_location:
            print(fighter)

    def choose_jedi(self):
        for jedi in self.jedi_at_location:
            print(jedi.name)
        choose_your_fighter = input("Who do you wish to pick?").capitalize()
        for jedi in self.jedi_at_location:
            while choose_your_fighter not in jedi.name:
                choose_your_fighter = input("Who do you wish to pick?").capitalize()
            if choose_your_fighter in jedi.name:
                print("success")
                return jedi
                
    def choose_sith(self):
        for sith in self.sith_at_location:
            print(sith.name)
            
        choose_your_fighter = input("Who do you wish to pick?").capitalize()
        for sith in self.sith_at_location:
            while choose_your_fighter not in sith.name:
                choose_your_fighter = input("Who do you wish to pick?").capitalize()
            if choose_your_fighter in sith.name:
                print("success")
                return sith