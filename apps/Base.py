__author__ = 'prince'
import cherrypy

from lib.Renderer import *

class Base:
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        print "\n\n\nBase"
        rc = {'status' : 0, 'msg' : 'some random msg'}
        return render(rc)

