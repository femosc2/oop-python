import time
import peewee as pw

#OOP in python next steps lesson 3 with aleksander

#Object-relational mapping ( ORM)

#ORms help you a lot in writing complex crud operations wihch ar a paint to write via manual sql.

    # Create a new object in a database
    # Update an object in a database
    # Delete an object from a database

#db = pw.SqliteDatabase("animals2.db")

#class ZooAnimal(pw.Model):
    #animal_name = pw.TextField() #Text = type
    #a_popular = pw.IntegerField() #integer = type
    #class Meta: #configuration class
     #   """
      #  Connect the databse ot them odesl via the nested class
      #  """
      #  database = db

#if __name__ == "__main__":
   # try:
        #ZooAnimal.create_table()
    #except pw.OperationalError:
       # print(" ZooAnimal table already exists!")

    #animal1 = ZooAnimal(animal_name="Felix", a_popular=4)
    #animal2 = ZooAnimal(animal_name="Victor", a_popular=3)
    #animal3 = ZooAnimal(animal_name="Adam", a_popular=2)

    #animal1.save()
    #animal2.save()
    #animal3.save()


db = pw.SqliteDatabase("taxi.db")

class Taxi(pw.Model):
    taxi_name = pw.TextField() #Text = type
    taxi_id = pw.CharField() #char = type
    taxi_travellers = pw.IntegerField() #int = type
    class Meta: #configuration class
        """
        Connect the databse ot the models via the nested class
        """
        database = db

if __name__ == "__main__":
    try:
        Taxi.create_table()
    except pw.OperationalError:
        print(" Taxi table already exists!")

    taxi1 = Taxi(taxi_name="Felix", taxi_id = "24c", taxi_travellers=4)
    taxi2 = Taxi(taxi_name="Victor", taxi_id ="2", taxi_travellers=2)
    taxi3 = Taxi(taxi_name="Adam", taxi_id="1337", taxi_travellers=8)

    taxi1.save()
    taxi2.save()
    taxi3.save()