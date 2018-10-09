from visit import Visit

class Membership():
    """ Lol """
    def __init__(self, id, visit):
        self.id = id;
        self.visit = Visit.how_many()
    def getVisits(self):
        visits = []
        visits.append(Visit(1,2))
        for visit in visits:
            print(visit)