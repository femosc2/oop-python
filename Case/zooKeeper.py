from person import Person

class ZooKeeper(Person):
    """ time """
    def __init__(self, age, emp_id, name):
        super().__init__(self, age)
        self.emp_id = emp_id
        self.name = name
    def maintain(self):
        """ maintains the zoo """
        pass
