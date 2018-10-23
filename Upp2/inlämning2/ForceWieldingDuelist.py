from random import randint

from Lightsaber import Lightsaber
from ForcePower import ForcePower
from Rank import Rank

class ForceWieldingDuelist():
    """ Blueprint for creating a new fighter """
    def __init__(self, name, force_name, rank, lightsaber_color, hilt_type):
        """ Creates a new Force Wielding Duelist """
        self.name = name # The name of the duelist
        self.lightsaber = Lightsaber(lightsaber_color, hilt_type) # Creates a new lightsaber object with the arguments the user declared.
        if rank in ["master", "lord"]: # Creates a new rank depending on what name the rank has.
            self.rank = Rank(rank, 3)
        elif rank in ["knight", "marauder"]:
            self.rank = Rank(rank, 2)
        elif rank in ["padawan", "apprentice"]:
            self.rank = Rank(rank, 1)
        else:
            self.rank = Rank(rank, 2)
        if force_name in ["lightning", "battle meditation"]: # Creates a new forcepower depending on what rank the forcepower has.
            self.forcePower = ForcePower(force_name, 3)
        elif force_name in ["choke", "heal"]:
            self.forcePower = ForcePower(force_name, 2)
        elif force_name == "push":
            self.forcePower = ForcePower(force_name, 1)
        else:
            self.forcePower = ForcePower(force_name, 2)
        
        self.combatant_strenght = ForcePower.get_force_strenght(self.forcePower) + Rank.get_rank_strenght(self.rank) # Takes the force_strenght and rank_strenght and combines them into a value
    def __str__(self):
        """ Decides how the print of an object looks """
        return "{rank} {name} \n Strenght: {combatant_strenght} \n Lightsaber: {lightsaber}".format(rank=self.rank, name=self.name, lightsaber=self.lightsaber, combatant_strenght=self.combatant_strenght)
    def get_strenght(self):
        """ Returns the strenght of the combatant + random number to make sure that the same combatant doesnt win all the time """
        return self.combatant_strenght + randint(0,2) 