from ForceWieldingDuelist import ForceWieldingDuelist

class Sith(ForceWieldingDuelist):
    """ Blueprint for creating a Sith """
    def __init__(self, name, force_name, force_strenght, rank, rank_strenght):
        """ Creates a new Jedi by inherting the ForceWieldingDuelist """
        super().__init__(name, force_name, force_strenght, rank, rank_strenght)
    def __str__(self):
        """ Returns the information about a Sith """
        duelist_information = super().__str__()
        return "Sith {duelist_information}".format(duelist_information=duelist_information)