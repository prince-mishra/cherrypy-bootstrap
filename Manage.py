__author__ = 'prince'
import os
import cherrypy
import Settings
import time
from Urls import Root

from DBManager import bootstrap_db

def runserver():

    cherrypy.config.update({
        'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
        'tools.decode.on': True,
        'tools.trailing_slash.on': True,
        'tools.staticdir.root': Settings.base_path,
        })
    
    bootstrap_db()
    cherrypy.quickstart(Root(), '/', {
        '/media': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'media'
        }
    })



def shell():
    pass

if __name__=="__main__":
    runserver()

