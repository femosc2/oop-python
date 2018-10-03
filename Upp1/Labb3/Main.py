from Users import User
from Mweet import Message
import peewee as pw

def create_tables():
    ''' Our method where we will create the database tables'''
    try:
        User.create_table()
        Message.create_table()
    except pw.OperationalError:
        print(" Users or Messages table already exists!")


def create_user(**kwargs):
    ''' Our method where we will create the user objects'''
    try:
        new_user = User(**kwargs)
        new_user.save()
        print("*"*40)
        for key, value in kwargs.items():
            print("{0} = {1}".format(key,value))
        print("Added!")
        print("*"*40)
    except pw.IntegrityError:
        user = kwargs.pop('username')
        print(user, "is already in the database!")
        pass  


def create_messages(**kwargs):
    ''' Our method where we will create message objects '''
    #user_ref = User.get(User.username == User.username)

    try:
        msg = Message(**kwargs)
        msg.save()
    except:
        pass
    


def print_messages(uname):
         ''' Our method that will print out all the messages from a user '''
         user = User.get(username=uname)
         for msg in user.messages:
             print(msg.message)

def main():
    ''' out main method where we will call all other methods'''
    create_tables()
    create_user(username="Felix", country="Sweden",
                full_name="Felix Morau", password="1234",
                email="felixmorau@gmail.com")

    create_user(username="Jens", country="Sweden",
                full_name="Jensa K", password="1234",
                email="jensaK@gmail.com")

    create_user(username="Kesse", country="Sweden",
                full_name="Linse K", password="1234",
                email="kesse@gmail.com")
                
    create_messages(username=1, message="Loooool",
                likes=1337)
if __name__ == '__main__':
    main()