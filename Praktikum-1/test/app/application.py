# coding: utf-8

import cherrypy

#--------------------------------------
class Application_cl(object):
#--------------------------------------
   #----------------------------------
   def __init__(self):
   #--------------------------------------
      # constructor
      pass

   @cherrypy.expose
   #--------------------------------------
   def greeting(self):
   #--------------------------------------
      return "Cherrypy-Server, Version %s" % cherrypy.__version__

   @cherrypy.expose
   #--------------------------------------
   def default(self, *arglist, **kwargs):
   #--------------------------------------
      msg_s = "unbekannte Anforderung: " + \
              str(arglist) + \
              ''+\
              str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
# EOF