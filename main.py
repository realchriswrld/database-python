#install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "chris.db"))

#creating ou first table

class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
User.create_table(fail_silently= True)



#create student table

class Student(Model):
    name = CharField()
    age = CharField()
    verfication = CharField()
    stream = CharField()
    gender = CharField()


    class Meta:
        database = db
Student.create_table(fail_silently=True)