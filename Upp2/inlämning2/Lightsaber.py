class Lightsaber():
    """ Blueprint for creating a lightsaber """
    def __init__(self, lightsaber_color, hilt_type):
        """ Creates a new lightsaber object """
        self.lightsaber_color = lightsaber_color
        self.hilt_type = hilt_type
    def __str__(self):
        return self.hilt_type + " " + self.lightsaber_color + " lightsaber"