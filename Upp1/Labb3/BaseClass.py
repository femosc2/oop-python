import peewee as pw
mautter_db = pw.SqliteDatabase("mautter.db")
db = mautter_db

class BaseClass(pw.Model):
    """ This si the base class form which all our other lcasses will inehrit,
     the benefit of having a common class is that we dont have to set the configuration"""
    db = mautter_db
    class Meta:
        """ Config class"""
        database = db
