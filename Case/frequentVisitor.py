from visitor import Visitor

from visit import Visit

from membership import Membership

class FrequentVisitor(Visitor):
    """ time """
    def __init__(self, name, id, timestamp, age):
        super().__init__(timestamp, age)
        self.name = name
        self.membershipID = Membership(id, 1)
    def returnTime(self, timestamp):
        """ lol """
        return timestamp
    def __str__(self):
        return "Name: {name}, Membership ID:  {membershipID}, Timestamp {timestamp}".format(name=self.name, timestamp=self.timestamp, membershipID=self.membershipID)