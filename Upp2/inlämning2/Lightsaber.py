class Lightsaber():
    """ Blueprint for creating a lightsaber """
    def __init__(self, lightsaber_color, hilt_type):
        """ Creates a new lightsaber object """
        self.lightsaber_color = lightsaber_color
        self.hilt_type = hilt_type
    def __str__(self):
        """ Defines how the print is going to look for the Lightsaber object """
        return self.hilt_type + " " + self.lightsaber_color + " lightsaber" 