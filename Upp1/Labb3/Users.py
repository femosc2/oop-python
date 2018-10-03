import peewee as pw
from BaseClass import BaseClass

class User(BaseClass):
    username = pw.CharField(unique=True) #Char = type
    country= pw.CharField() #char = type
    full_name = pw.CharField() #char = type
    password = pw.CharField() #char = type
    email = pw.CharField() #char = type