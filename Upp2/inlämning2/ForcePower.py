class ForcePower():
    """ Method for creating a new Force Power """
    def __init__(self, force_name, force_strenght):
        """ Creates a new force power """
        self.force_name = force_name
        self.force_strenght = force_strenght
    def return_force_strenght(self):
       return self.force_strenght