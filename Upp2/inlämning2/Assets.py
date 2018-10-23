from ForcePower import ForcePower
from Rank import Rank
from Jedi import Jedi
from Sith import Sith

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
        self.jedi = [
            Jedi("Bastila Shan", "battle meditation", "padawan"),
            Jedi("Luke Skywalker", "push", "master"),
            Jedi("Anakin Skywalker", "choke", "knight")
            ]
        self.sith = [
            Sith("Darth Vader", "choke", "lord"),            
            Sith("Darth Revan", "lightning", "lord"),
            Sith("Darth Maul", "push", "apprentice")
            ]

            