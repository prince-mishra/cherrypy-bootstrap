__author__ = 'prince'
import cherrypy

from Lib.Renderer import *

class Base:
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        print "\n\n\nBase"
        rc = {'status' : 0, 'msg' : 'some random msg', 'page' : 'base.html'}
        return render(rc)

