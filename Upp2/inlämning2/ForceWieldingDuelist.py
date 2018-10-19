from Lightsaber import Lightsaber
from ForcePower import ForcePower
from Rank import Rank

class ForceWieldingDuelist():
    """ Blueprint for creating a new fighter """
    def __init__(self, name, force_name, rank, lightsaber_color, hilt_type):
        self.name = name
        self.lightsaber = Lightsaber(lightsaber_color, hilt_type)
        if rank in ["master", "lord"]:
            self.rank = Rank(rank, 3)
        elif rank in ["knight", "maruader"]:
            self.rank = Rank(rank, 2)
        elif rank in ["padawan" or "apprentice"]:
            self.rank = Rank(rank, 1)
        if force_name in ["lightning", "battle meditation"]:
            self.forcePower = ForcePower(force_name, 3)
        elif force_name in ["choke", "heal"]:
            self.forcePower = ForcePower(force_name, 2)
        elif force_name == "push":
            self.forcePower = ForcePower(force_name, 1)
        
        self.combatant_strenght = ForcePower.return_force_strenght(self.forcePower) + Rank.return_rank_strenght(self.rank)
    def __str__(self):
        return "{rank}, {name} \n Strenght: {combatant_strenght} \n Lightsaber: {lightsaber}".format(rank=self.rank, name=self.name, lightsaber=self.lightsaber, combatant_strenght=self.combatant_strenght)
    def return_strenght(self):
        return self.combatant_strenght