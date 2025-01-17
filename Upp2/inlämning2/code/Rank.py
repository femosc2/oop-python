class Rank():
    """ Blueprint for creating a new Rank """
    
    def __init__(self, rank_name, rank_strenght):
        """ Creates a new rank object """

        self.rank_name = rank_name
        self.rank_strenght = rank_strenght

    def get_rank_strenght(self):
        """ Returns the strenght of the rank """

        return self.rank_strenght

    def get_rank_name(self):
        """ Returns the name of the rank """

        return self.rank_name

    def __str__(self):
        """ Prints the name of the rank capitalized """

        return self.rank_name.capitalize()