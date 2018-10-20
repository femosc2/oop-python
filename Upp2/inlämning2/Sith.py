from ForceWieldingDuelist import ForceWieldingDuelist

class Sith(ForceWieldingDuelist):
    """ Blueprint for creating a jedi """
    def __init__(self, name, force_name, rank, lightsaber_color, hilt_type):
        """ Creates a new Jedi by inherting the ForceWieldingDuelist """
        super().__init__(name, force_name, rank, lightsaber_color, hilt_type)
    def __str__(self):
        duelist_information = super().__str__()
        return "Sith {duelist_information}".format(duelist_information=duelist_information)