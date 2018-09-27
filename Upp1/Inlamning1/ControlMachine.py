from Ticket import Ticket
from Scale import Scale


class ControlMachine():
    """ Blueprint for the Control Machine at the airport """

    def __init__(self):
        """ Not used """
        pass

    def checkWeight(self, weightLuggage):
        """ Checks the weight of the luggage, returns True if it passes
            ,returns False if it fails
        """
        pass

    def checkTicket(self, ticket):
        """ Checks the validility of the ticket, if the ticket is invalid, refer to the manual checkout
            if the ticket is valid the users luggage gets weighed
            if the weight is invalid, refer to manual checkout
            else create and print the label for the luggage
        """

        if ticket == "Valid":
            if self.checkWeight(123) == True:
                self.createLabel()
                self.printLabel()
            else:
                self.referToManualCheckout()
        else:
            self.referToManualCheckout()
        
    def referToManualCheckout(self):
        """ Tells the user to go to the manual checkout """
        pass
    def createLabel(self):
        """ Creates the Label """
        pass
    def printLabel(self):
        """ prints the label """
        pass
