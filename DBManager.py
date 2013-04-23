
import requests
from sqlobject import *
import sqlite3 as sqlite
import time
import os

import Settings

class Sample(SQLObject):
    name     = UnicodeCol(length = 1024, unique = True)

def bootstrap_db():
	connect_db()
	init_db()

def connect_db(db_path = Settings.db_path):
    connection_string = 'sqlite:' + db_path
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection

def init_db():
    Sample.createTable(ifNotExists=True)