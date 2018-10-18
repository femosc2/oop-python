class Rank():
    """ Blueprint for creating a new Rank """
    def __init__(self, rank_name):
        """ Creates a new rank object """
        self.rank_name = rank_name
    def return_rank_strenght(self):
        if self.rank_name == "master" or "lord":
            return 3
        elif self.rank_name == "knight" or "marauder":
            return 2
        elif self.rank_name == "padawan" or "apprentice":
            return 1
            
