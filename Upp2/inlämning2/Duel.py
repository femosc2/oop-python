from Location import Location

class Duel():
    """ Blueprint for creating a new duel """
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        
    def duel(self):
        if self.fighter1.return_strenght() < self.fighter2.return_strenght():
            print("Fighter 1 won!")
        elif self.fighter1.return_strenght() == self.fighter2.return_strenght():
            print("It is a draw!")
        else:
            print(" Fighter 2 won!")