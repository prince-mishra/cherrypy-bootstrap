__author__ = 'prince'
import os
import cherrypy
import Settings

import requests
from sqlobject import *
import sqlite3 as sqlite
import time

class Sample(SQLObject):
    name     = UnicodeCol(length = 1024, unique = True) # lets ensure unique links at db level

from Urls import Root

def runserver():

    cherrypy.config.update({
        'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
        'tools.decode.on': True,
        'tools.trailing_slash.on': True,
        'tools.staticdir.root': Settings.base_path,
        })

    connect_db()
    init_db()

    cherrypy.quickstart(Root(), '/', {
        '/media': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'media'
        }
    })

def connect_db(db_path = Settings.db_path):
    connection_string = 'sqlite:' + db_path
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection

def init_db():
    Sample.createTable(ifNotExists=True)

def shell():
    pass

if __name__=="__main__":
    runserver()

