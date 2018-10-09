from visitor import Visitor

class OneTimeVisitor(Visitor):
    """ time """
    def __init__(self, timestamp, age):
        super().__init__(timestamp, age)
        self.timestamp = timestamp
    def __str__(self):
        return "Timestamp : {timestamp}".format(timestamp=self.timestamp)
