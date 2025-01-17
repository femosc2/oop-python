from ForcePower import ForcePower
from Rank import Rank
from Jedi import Jedi
from Sith import Sith

class Assets():
    """ Blueprint for a psuedo database """
    def __init__(self):
        """ Creates assets for the program """
        
        self.force_powers = [
            ForcePower("push", 1),
            ForcePower("choke", 2),
            ForcePower("heal", 2),
            ForcePower("lightning", 3),
            ForcePower("battle meditation", 3)
        ]

        self.jedi_ranks = [
            Rank("master", 3),
            Rank("knight", 2),
            Rank("padawan", 1),
        ]

        self.sith_ranks = [
            Rank("lord", 3),
            Rank("marauder", 2),
            Rank("apprentice", 1),
        ]

            