from random import randint
from ForcePower import ForcePower
from Rank import Rank

class ForceWieldingDuelist():
    """ Blueprint for creating a new fighter """

    def __init__(self, name, force_name, force_strenght, rank, rank_strenght):
        """ Creates a new Force Wielding Duelist """
        self.name = name # The name of the duelist
        self.rank = Rank(rank, rank_strenght)
        self.forcePower = ForcePower(force_name, force_strenght)
        
        self.combatant_strenght = ForcePower.get_force_strenght(self.forcePower) + Rank.get_rank_strenght(self.rank) # Takes the force_strenght and rank_strenght and combines them into a value

    def __str__(self):
        """ Decides how the print of an object looks """

        return "{rank} {name} \n Strenght: {combatant_strenght}".format(rank=self.rank, name=self.name, combatant_strenght=self.combatant_strenght)

    def get_strenght(self):
        """ Returns the strenght of the combatant + random number to make sure that the same combatant doesnt win all the time """
        
        return self.combatant_strenght + randint(0,2) 