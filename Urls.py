__author__ = 'prince'
import cherrypy
from apps import Base

class Root(object):
    def __init__(self):
        self.base = Base.Base()
    @cherrypy.expose
    def index(self):
        return "index at root"
