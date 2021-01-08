# coding: utf-8
import cherrypy

from .database import Database_cl
from .view import View_cl


#----------------------------------------------------------
class App_mitarbeiter_cl(object): # MITARBEITER
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, mitarbeiter=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_m()
      else:
         # Anforderung eines Details
         retVal_s = self.getDetail_m(id)

      return retVal_s
   
   #-------------------------------------------------------
   def POST(self, id, name, vorname, akagrad, taetigkeit):
   #-------------------------------------------------------
      
      data_m = { 
      'id':id,
      'name':name,
      'vorname':vorname,
      'akagrad':akagrad,
      'taetigkeit':taetigkeit
      }    
      id = self.database.create_mitarbeiter(data_m)
      
      return str(id)
      
   #-------------------------------------------------------
   def PUT(self, id, name, vorname, akagrad, taetigkeit):
   #-------------------------------------------------------
      
      data_m = { 
      'id':id,
      'name':name,
      'vorname':vorname,
      'akagrad':akagrad,
      'taetigkeit':taetigkeit
      }    
      self.database.update_mitarbeiter(id, data_m)
      
      return id
   
   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      return self.database.delete_mitarbeiter(id)
      
   #-------------------------------------------------------
   def getList_m(self):
   #-------------------------------------------------------
      self.database.readData_mitarbeiter()
      data_m = self.database.read_mitarbeiter()

      return self.view_o.createList_m(data_m)
   
   #-------------------------------------------------------
   def getDetail_m(self, id_spl):
   #-------------------------------------------------------
      self.database.readData_mitarbeiter()
      data_m = self.database.read_mitarbeiter(id_spl)

      return self.view_o.createDetail_m(data_m)


#----------------------------------------------------------
class App_weiterbildung_cl(object): # WEITERBILDUNG
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, weiterbildung=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_w()
      else:
         # Anforderung eines Details
         retVal_s = self.getDetail_w(id)

      return retVal_s
   
   #-------------------------------------------------------
   def POST(self, id, bezeichnung_w, von_w, bis_w, beschreibung_w, maxteilnehmer_w, minteilnehmer_w, bezeichnung_q, beschreibung_q, bezeichnung_z, beschreibung_z, berechtigtzu_z):
   #-------------------------------------------------------
      
      data_w = { 
      'id':id,
      'bezeichnung_w':bezeichnung_w,
      'von_w':von_w,
      'bis_w':bis_w,
      'beschreibung_w':beschreibung_w,
      'maxteilnehmer_w':maxteilnehmer_w,
      'minteilnehmer_w':minteilnehmer_w
      }

      data_q = { 
      'id':id,
      'bezeichnung_q':bezeichnung_q,
      'beschreibung_q':beschreibung_q
      }

      data_z = { 
      'id':id,
      'bezeichnung_z':bezeichnung_z,
      'beschreibung_z':beschreibung_z,
      'berechtigtzu_z':berechtigtzu_z
      }

      id = self.database.create_weiterbildung(data_w, data_q, data_z)
      
      return str(id)
      
   #-------------------------------------------------------
   def PUT(self, id, bezeichnung_w, von_w, bis_w, beschreibung_w, maxteilnehmer_w, minteilnehmer_w, bezeichnung_q, beschreibung_q, bezeichnung_z, beschreibung_z, berechtigtzu_z):
   #-------------------------------------------------------
      
      data_w = { 
      'id':id,
      'bezeichnung_w':bezeichnung_w,
      'von_w':von_w,
      'bis_w':bis_w,
      'beschreibung_w':beschreibung_w,
      'maxteilnehmer_w':maxteilnehmer_w,
      'minteilnehmer_w':minteilnehmer_w
      }

      data_q = { 
      'id':id,
      'bezeichnung_q':bezeichnung_q,
      'beschreibung_q':beschreibung_q
      }

      data_z = { 
      'id':id,
      'bezeichnung_z':bezeichnung_z,
      'beschreibung_z':beschreibung_z,
      'berechtigtzu_z':berechtigtzu_z
      }

      self.database.update_weiterbildung(id, data_w)
      self.database.update_qualifikation(id, data_q)
      self.database.update_zertifikat(id, data_z)
      
      return id
   
   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.database.delete_weiterbildung(id)
      self.database.delete_qualifikation(id)
      self.database.delete_zertifikat(id)
   
   #-------------------------------------------------------
   def getList_w(self):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()
      data_w = self.database.read_weiterbildung()
      data_q = self.database.read_qualifikation()
      data_z = self.database.read_zertifikat()

      return self.view_o.createList_w(data_w, data_q, data_z)
   
   #-------------------------------------------------------
   def getDetail_w(self, id_spl):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()
      data_w = self.database.read_weiterbildung(id_spl)
      data_q = self.database.read_qualifikation(id_spl)
      data_z = self.database.read_zertifikat(id_spl)

      return self.view_o.createDetail_w(data_w, data_q, data_z)


#----------------------------------------------------------
class App_teilnahme_cl(object): # WEITERBILDUNG
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, weiterbildung=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_w()
      else:
         # Anforderung eines Details
         retVal_s = self.getDetail_w(id)

      return retVal_s
   
   #-------------------------------------------------------
   def POST(self, id, name, vorname, akagrad, taetigkeit, bezeichnung_w, von_w, bis_w, beschreibung_w, maxteilnehmer_w, minteilnehmer_w):
   #-------------------------------------------------------
      
      data_m = { 
      'id':id,
      'name':name,
      'vorname':vorname,
      'akagrad':akagrad,
      'taetigkeit':taetigkeit
      }  

      data_w = { 
      'id':id,
      'bezeichnung_w':bezeichnung_w,
      'von_w':von_w,
      'bis_w':bis_w,
      'beschreibung_w':beschreibung_w,
      'maxteilnehmer_w':maxteilnehmer_w,
      'minteilnehmer_w':minteilnehmer_w
      }

      data_t = [data_m, data_w]  # Keine Ahnung ob das so überhaupt geht?
      id = self.database.create_teilnahme(data_t)
      
      return str(id)
      
   #-------------------------------------------------------
   def PUT(self, id, name, vorname, akagrad, taetigkeit, bezeichnung_w, von_w, bis_w, beschreibung_w, maxteilnehmer_w, minteilnehmer_w):
   #-------------------------------------------------------
      
      data_m = { 
      'id':id,
      'name':name,
      'vorname':vorname,
      'akagrad':akagrad,
      'taetigkeit':taetigkeit
      }  

      data_w = { 
      'id':id,
      'bezeichnung_w':bezeichnung_w,
      'von_w':von_w,
      'bis_w':bis_w,
      'beschreibung_w':beschreibung_w,
      'maxteilnehmer_w':maxteilnehmer_w,
      'minteilnehmer_w':minteilnehmer_w
      }

      data_t = [data_m, data_w]  # Keine Ahnung ob das so überhaupt geht?
      self.database.update_teilnahme(id, data_t)
      
      return id
   
   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.database.delete_teilnahme(id)

   #-------------------------------------------------------
   def getList_w(self):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()
      data_w = self.database.read_weiterbildung()
      data_q = self.database.read_qualifikation()
      data_z = self.database.read_zertifikat()

      return self.view_o.createList_w(data_w, data_q, data_z)
   
   #-------------------------------------------------------
   def getDetail_w(self, id_spl):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()
      data_w = self.database.read_weiterbildung(id_spl)
      data_q = self.database.read_qualifikation(id_spl)
      data_z = self.database.read_zertifikat(id_spl)

      return self.view_o.createDetail_w(data_w, data_q, data_z)


# EOF