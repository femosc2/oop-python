class Visit():
    """ lol """
    numberOfVisits = 0
    @classmethod
    def how_many(cls):
        return cls.numberOfVisits
    def __init__(self, entry_time, exit_time):
        """ pass """
        self.entry_time = entry_time
        self.exit_time = exit_time
    def __str__(self):
        return "Entry: {entry}, Exit: {exit}".format(entry=self.entry_time, exit=self.exit_time )

    
#v1 = Visit(1, 2)
#print(v1)