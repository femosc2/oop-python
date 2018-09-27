from Ticket import Ticket
from Scale import Scale


class ControlMachine():
    """ Blueprint for the Control Machine at the airport """

    def __init__():
        """ Not used """
        pass

    def checkWeight(weightLuggage):
        """ Checks the weight of the luggage, returns True if it passes, returns False if it fails """
        pass

    def checkTicket(ticket):
        """ Checks the validility of the ticket, if the ticket is invalid, refer to the manual checkout """

        if ticket == "Valid":
            checkWeight()
            if weight === True;
                createLabel()
                printLabel()
            else:
                referToManualCheckout()
        else:
            referToManualCheckout()
        
    def referToManualCheckout():
        """ Tells the user to go to the manual checkout """
        pass
    def createLabel():
        """ Creates the Label """
        pass
    def printLabel():
        """ prints the label """
