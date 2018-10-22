from Location import Location

class Duel():
    """ Blueprint for creating a new duel """
    def __init__(self, fighter1, fighter2):
        """ Creates a new duel """

        self.fighter1 = fighter1
        self.fighter2 = fighter2
        
    def duel(self):
        """ Checks the combatant_strenght attributes of two different fighters and decides the winner """
        if self.fighter1.return_strenght() < self.fighter2.return_strenght():
            print("*"*40)
            print(self.fighter1.name, "won!")
            print("*"*40)
        elif self.fighter1.return_strenght() == self.fighter2.return_strenght():
            print("It is a draw!")
        else:
            print("*"*40)
            print(self.fighter2.name, "won!")
            print("*"*40)