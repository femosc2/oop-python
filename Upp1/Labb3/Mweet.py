import peewee as pw
from Users import User
from BaseClass import BaseClass


class Mweet(BaseClass):
    user = pw.ForeignKeyField(User, backref="messages")
    message = pw.TextField() #text=type
    likes = pw.IntegerField()
    #def incease_likes(self, likes):
        #self.likes = likes + 1
