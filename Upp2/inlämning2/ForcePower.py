class ForcePower():
    """ Method for creating a new Force Power """
    def __init__(self, force_name):
        """ Creates a new force power """
        self.force_name = force_name
    def return_force_strenght(self):
        if self.force_name == "lightning":
            return 3
        elif self.force_name == "battle meditation":
            return 3
        elif self.force_name == "choke":
            return 2
        elif self.force_name == "heal":
            return 2
        elif self.force_name == "push":
            return 1
        elif self.force_name == "the high ground":
            return 999
