#!/usr/bin/python
import sys
import peewee
from models import *

''' Relates inputs to model names '''
models_dict = {'school': School, 'batch': Batch, 'student': Student}

''' Creates tables of all models from models.py '''
def create():
    my_models_db.create_tables([School, Batch, User, Student])

''' Prints all rows of specified table '''
def prints():
    if len(sys.argv) < 3:
        print ("Please specify a table to print")
    else:
        rows = models_dict[sys.argv[2]].select()
        for r in rows:
            print r

''' Inserts row in specified table '''
def insert():
    if len(sys.argv) < 3:
        print ("Please specify a table")
        return

    ''' If inserting row into School table '''
    if sys.argv[2] == "school":
        if len(sys.argv) < 4:
            print ("Please provide a name for the school")
            return
        entry = School.create(name=sys.argv[3])
        print ("New school: " + str(entry))

    ''' If inserting row into Batch table '''
    if sys.argv[2] == "batch":
        if len(sys.argv) < 5:
            print ("Please provide a school id and/or name")
            return
        entry = Batch.create(school_id=sys.argv[3], name=sys.argv[4])
        print ("New batch: " + str(entry))

    ''' If inserting row into Student table '''
    if sys.argv[2] == "student":
        if len(sys.argv) < 7:
            print ("Please provide all the attributes for a student")
            return
        entry = Student.create(batch_id=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name=sys.argv[6])
        print ("New student: " + str(entry))

'''If in your database you don't have any object with this id, your program should print Nothing to delete
otherwise, the object will be deleted and your program should print Delete: <object to delete>'''
def delete():
    if len(sys.argv) < 4:
        print ("Please specify a model and/or object id to delete")
    else:
        Model = models_dict[sys.argv[2]]
        row = Model.delete().where(Model.id == sys.argv[3])
        row.execute()

dict = { 'create': create, 'print': prints, 'insert': insert, 'delete': delete }

if len(sys.argv) < 2:
    print ("Please enter an action")
else:
    for key in dict:
        if key == sys.argv[1]:
            dict[key]()
            sys.exit()
    print ("Undefined action %s" % sys.argv[1])
