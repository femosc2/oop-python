from Lightsaber import Lightsaber
from ForcePower import ForcePower
from Rank import Rank
from Species import Species

class ForceWieldingDuelist():
    """ Blueprint for creating a new fighter """
    def __init__(self, name, force_power, rank, lightsaber_color, hilt_type, force_name, species):
        self.name = name
        self.lightsaber = Lightsaber(lightsaber_color, hilt_type)
        self.rank = rank
        self.combatant_strenght = ForcePower.return_force_strenght(force_name) + Rank.return_rank_strenght(rank)
        self.species = Species(species)
    def __str__(self):
        return "{rank}, {name} \n Strenght: {combatant_strenght} \n Species: {species} \n Lightsaber: {lightsaber}".format(rank=self.rank, name=self.name, combatant_stenght = self.combatant_strenght, lightsaber=self.lightsaber) 
