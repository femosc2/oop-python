from ForceWieldingDuelist import ForceWieldingDuelist

class Jedi(ForceWieldingDuelist):
    """ Blueprint for creating a jedi """
    def __init__(self, name, force_name, rank, lightsaber_color, hilt_type):
        """ Creates a new Jedi by inherting the ForceWieldingDuelist """
        super().__init__(name, force_name, rank, lightsaber_color, hilt_type)
    def __str__(self):
        """ Defines what is going to be printed from an Jedi Object """
        duelist_information = super().__str__()
        return "Jedi {duelist_information}".format(duelist_information=duelist_information)