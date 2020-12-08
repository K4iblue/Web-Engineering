# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()

   @cherrypy.expose
   #-------------------------------------------------------
   def index(self, listform="tabelle"):                        # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      if listform == "listform=tabelle":
            listform = "tabelle"
      return self.createList_p(listform)

   @cherrypy.expose
   #-------------------------------------------------------
   def add(self, listform):                                    # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      return self.createForm_p(listform)

   @cherrypy.expose
   #-------------------------------------------------------
   def edit(self, id_spl, listform):                           # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      return self.createForm_p(listform, id_spl)

   @cherrypy.expose
   #-------------------------------------------------------
   # Ergänzung: Zweites Team mitglied hinzufügen // Semesteranzahl hinzugfügen // History "Funktion"
   def save(self, id_spa, name1_spa, vorname1_spa, matrnr1_spa, semesteranzahl1_spa, name2_spa, vorname2_spa, matrnr2_spa, semesteranzahl2_spa, listform):
   #-------------------------------------------------------
      id_s = id_spa
      # Ergänzung: Zweites Team mitglied hinzufügen // Semesteranzahl hinzugfügen
      data_a = [ name1_spa, vorname1_spa, matrnr1_spa, semesteranzahl1_spa, name2_spa, vorname2_spa, matrnr2_spa, semesteranzahl2_spa ]
      if id_s != "None":
         self.db_o.update_px(id_s, data_a)
      else:
         self.db_o.create_px(data_a)
      return self.createList_p(listform)

   @cherrypy.expose
   #-------------------------------------------------------
   def delete(self, id, listform):                             # Ergänzung: History "Funktion"
   #-------------------------------------------------------
   # Ergänzung: Löschen von Einträgen
      self.db_o.delete_px(id)
      raise cherrypy.HTTPRedirect("/?listform=" + listform)

   @cherrypy.expose
   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
      str(arguments) + \
      ' ' + \
      str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
   default.exposed= True

   #-------------------------------------------------------
   def createList_p(self, listform):                           # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      data_o = self.db_o.read_px()
      return self.view_o.createList_px(data_o, listform)

   #-------------------------------------------------------
   def createForm_p(self, listform, id_spl = None):            # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      if id_spl != None:
         data_o = self.db_o.read_px(id_spl)
      else:
         data_o = self.db_o.getDefault_px()
      return self.view_o.createForm_px(listform, id_spl, data_o)
# EOF