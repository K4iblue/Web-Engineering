# coding: utf-8

import json

import os
import os.path
import codecs

import cherrypy

# Method-Dispatching!

# Übersicht Anforderungen / Methoden
# (beachte: / relativ zu /templates, siehe Konfiguration Server!)

"""

Anforderung       GET          PUT          POST          DELETE
----------------------------------------------------------------
/                 Alle         -            -             -
                  Templates
                  liefern

"""

#----------------------------------------------------------
class Template_cl(object):
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      pass

   #-------------------------------------------------------
   def GET(self):
   #-------------------------------------------------------
      retVal_o = {
         'templates': {}
      }

      files_a = os.listdir(os.path.join(cherrypy.Application.currentDir_s, 'templates'))
      for fileName_s in files_a:
         file_o = codecs.open(os.path.join(cherrypy.Application.currentDir_s, 'templates', fileName_s), 'rU', 'utf-8')
         content_s = file_o.read()
         file_o.close()
         retVal_o["templates"][fileName_s] = content_s

      return json.dumps(retVal_o)
      
# EOF