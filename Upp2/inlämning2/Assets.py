from ForcePower import ForcePower
from Rank import Rank

class Assets():
    """ """
    def __init__(self):
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
            Rank("padawan", 1),
        ]
    def get_force_powers(self):
        return self.force_powers
    def get_jedi_ranks(self):
        return self.jedi_ranks
    def get_sith_ranks(self):
        return self.sith_ranks