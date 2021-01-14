# coding: utf-8
import cherrypy

from .database import Database_cl
from .view import View_cl
from collections import OrderedDict


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
      'id_m':id,
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
      'id_m':id,
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
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()
      self.database.readData_teilnahme()
      data_m = self.database.read_mitarbeiter(id_spl)
      data_w = self.database.read_weiterbildung()
      data_q = self.database.read_qualifikation()
      data_z = self.database.read_zertifikat()
      data_t = self.database.read_teilnahme()

      return self.view_o.createDetail_m(data_m, data_w, data_q, data_z, data_t)


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
      'id_w':id,
      'bezeichnung_w':bezeichnung_w,
      'von_w':von_w,
      'bis_w':bis_w,
      'beschreibung_w':beschreibung_w,
      'maxteilnehmer_w':maxteilnehmer_w,
      'minteilnehmer_w':minteilnehmer_w
      }

      data_q = { 
      'id_w':id,
      'bezeichnung_q':bezeichnung_q,
      'beschreibung_q':beschreibung_q
      }

      data_z = { 
      'id_w':id,
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
      'id_w':id,
      'bezeichnung_w':bezeichnung_w,
      'von_w':von_w,
      'bis_w':bis_w,
      'beschreibung_w':beschreibung_w,
      'maxteilnehmer_w':maxteilnehmer_w,
      'minteilnehmer_w':minteilnehmer_w
      }

      data_q = { 
      'id_w':id,
      'bezeichnung_q':bezeichnung_q,
      'beschreibung_q':beschreibung_q
      }

      data_z = { 
      'id_w':id,
      'bezeichnung_z':bezeichnung_z,
      'beschreibung_z':beschreibung_z,
      'berechtigtzu_z':berechtigtzu_z
      }

      self.database.update_weiterbildung(id, data_w, data_q, data_z)
      
      return id
   
   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.database.delete_weiterbildung(id)          # In Database werden Qualifikation und Zertifikat gelöscht.
   
   #-------------------------------------------------------
   def getList_w(self):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      data_w = self.database.read_weiterbildung()

      return self.view_o.createList_w(data_w)
   
   #-------------------------------------------------------
   def getDetail_w(self, id_spl):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()

      data_w = self.database.read_weiterbildung(id_spl)
      data_q = self.database.read_qualifikation(id_spl, data_w)
      data_z = self.database.read_zertifikat(id_spl, data_w)

      return self.view_o.createDetail_w(data_w, data_q, data_z)



#----------------------------------------------------------
class App_weiterbildung_anzeigen_cl(object): # WEITERBILDUNG ANZEIGEN
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, weiterbildungAnzeigen=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_s = self.get_weiterbildung_anzeigen(id)

      return retVal_s
   
   #-------------------------------------------------------
   def get_weiterbildung_anzeigen(self, id_spl):
   #-------------------------------------------------------
      # Daten auslesen und in die jeweilige "data_" packen
      self.database.readData_mitarbeiter()
      self.database.readData_weiterbildung()
      self.database.readData_qualifikation()
      self.database.readData_zertifikat()
      self.database.readData_teilnahme()
      data_m = self.database.read_mitarbeiter()
      data_w = self.database.read_weiterbildung(id_spl)
      data_q = self.database.read_qualifikation()
      data_z = self.database.read_zertifikat()
      data_t = self.database.read_teilnahme()

      return self.view_o.weiterbildung_anzeigen(data_m, data_w, data_q, data_z, data_t, id_spl)



#----------------------------------------------------------
class App_teilnahme_cl(object): # TEILNAHME
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, teilnahme=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_w()
      else:
         # Anforderung eines Details
         data_m = self.database.read_mitarbeiter()

         if id in data_m:
            retVal_s = self.getDetail_mt(id)
         else:
            retVal_s = self.getDetail_wt(id)

      return retVal_s
   
   #-------------------------------------------------------
   def POST(self, id_w, id_m):
   #-------------------------------------------------------
      status = "angemeldet"
      data_t = self.database.read_teilnahme()
      data_tIDs = self.database.read_teilnahmeIDs()

      for suche in data_tIDs: #iteriere durch die teilnahmeid json
         print ("Value : %s" %  suche)
         if id_w in data_t[suche]['id_w'] and id_m in data_t[suche]['id_m']:   #wenn id_w und id_m schon in teilnahme json vorhanden sind, dann beende Programm mit Meldung
            print ("ERROR")
            return str("Sie sind schon an dieser Weiterbildung angemeldet!")
      
      data_new = {
         'id_w':id_w,
         'id_m':id_m,
         'status':status
      }

      id = self.database.create_teilnahme(data_t, id_w, id_m, data_new)
      status = ""
      
      return str(id)
      
   #-------------------------------------------------------
   def PUT(self, id_m, id_w, status):
   #-------------------------------------------------------
      data_t = self.database.read_teilnahme()
      data_tIDs = self.database.read_teilnahmeIDs()

      self.database.update_teilnahme(data_t, data_tIDs, id_m, id_w, status)
      
      return id
   
   #-------------------------------------------------------
   def DELETE(self, id_w, id_m):
   #-------------------------------------------------------
      ausgabe = self.database.delete_teilnahme(id_w, id_m)

      return (ausgabe)
      
   #-------------------------------------------------------
   def getList_w(self):
   #-------------------------------------------------------
      self.database.readData_weiterbildung()
      data_w = self.database.read_weiterbildung()

      return self.view_o.createList_w(data_w)
   
   #-------------------------------------------------------
   def getDetail_mt(self, id_spl):
   #-------------------------------------------------------
      self.database.readData_mitarbeiter()
      self.database.readData_weiterbildung()
      self.database.readData_teilnahme()
      self.database.readData_teilnahmeIDs()
      data_m = self.database.read_mitarbeiter(id_spl)
      data_w = self.database.read_weiterbildung()
      data_t = self.database.read_teilnahme()
      data_tIDs = self.database.read_teilnahmeIDs()

      return self.view_o.createDetail_t(data_m, data_w, data_t, data_tIDs)

   #-------------------------------------------------------
   def getDetail_wt(self, id_spl):
   #-------------------------------------------------------
      self.database.readData_mitarbeiter()
      self.database.readData_weiterbildung()
      self.database.readData_teilnahme()
      self.database.readData_teilnahmeIDs()
      data_m = self.database.read_mitarbeiter()
      data_w = self.database.read_weiterbildung(id_spl)
      data_t = self.database.read_teilnahme()
      data_tIDs = self.database.read_teilnahmeIDs()

      return self.view_o.createDetail_t(data_m, data_w, data_t, data_tIDs)


#----------------------------------------------------------
class App_auswertung_mitarbeiter_cl(object): # AUSWERTUNG MITARBEITER
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, auswertungMitarbeiter=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_auswertung_mitarbeiter()
      else:
         # Anforderung eines Details
         retVal_s = self.getDetail_auswertung_mitarbeiter(id)

      return retVal_s

   #-------------------------------------------------------
   def getList_auswertung_mitarbeiter(self):
   #-------------------------------------------------------
      # Daten auslesen und in "data_m" packen
      self.database.readData_mitarbeiter()
      data_m = self.database.read_mitarbeiter()

      # Daten nach Namen sortieren und in ein geordnetes Dict packen
      sorted_data_m = sorted(data_m.items(), key=lambda x: x[1]['name'], reverse = False) #Alphabetisch sortiert
      ordered_dict_m = OrderedDict(sorted_data_m)

      return self.view_o.createList_auswertung_mitarbeiter(ordered_dict_m)
   
   #-------------------------------------------------------
   def getDetail_auswertung_mitarbeiter(self, id_spl):
   #-------------------------------------------------------
      # Daten auslesen und in die jeweilige "data_" packen
      self.database.readData_mitarbeiter()
      self.database.readData_weiterbildung()
      self.database.readData_teilnahme()
      data_m = self.database.read_mitarbeiter()
      data_w = self.database.read_weiterbildung()
      data_t = self.database.read_teilnahme()

      return self.view_o.createDetail_auswertung_mitarbeiter(data_m, data_w, data_t, id_spl)


#----------------------------------------------------------
class App_auswertung_weiterbildung_cl(object): # AUSWERTUNG WEITERBILDUNG
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, auswertungWeiterbildung=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_auswertung_weiterbildung()
      else:
         # Anforderung eines Details
         retVal_s = self.getDetail_auswertung_weiterbildung(id)

      return retVal_s

   #-------------------------------------------------------
   def getList_auswertung_weiterbildung(self):
   #-------------------------------------------------------
      # Daten auslesen und in "data_w" packen
      self.database.readData_weiterbildung()
      data_w = self.database.read_weiterbildung()

      # Daten nach Namen sortieren und in ein geordnetes Dict packen
      sorted_data_w = sorted(data_w.items(), key=lambda x: x[1]['bezeichnung_w'], reverse = False) #Alphabetisch sortiert
      ordered_dict_w = OrderedDict(sorted_data_w)

      return self.view_o.createList_auswertung_weiterbildung(ordered_dict_w)
   
   #-------------------------------------------------------
   def getDetail_auswertung_weiterbildung(self, id_spl):
   #-------------------------------------------------------
      # Daten auslesen und in die jeweilige "data_" packen
      self.database.readData_mitarbeiter()
      self.database.readData_weiterbildung()
      self.database.readData_teilnahme()
      data_m = self.database.read_mitarbeiter()
      data_w = self.database.read_weiterbildung(id_spl)
      data_t = self.database.read_teilnahme()

      return self.view_o.createDetail_auswertung_weiterbildung(data_m, data_w, data_t, id_spl)


#----------------------------------------------------------
class App_auswertung_zertifikat_cl(object): # AUSWERTUNG ZERTIFIKATE
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()
      self.view_o = View_cl()

   #-------------------------------------------------------
   def GET(self, id=None, auswertungZertifikat=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         # Anforderung der Liste
         retVal_s = self.getList_auswertung_zertifikat()
      else:
         # Anforderung eines Details
         retVal_s = self.getDetail_auswertung_zertifikat(id)

      return retVal_s

   #-------------------------------------------------------
   def getList_auswertung_zertifikat(self): # LISTE ALLER ZERTIFIKATE
   #-------------------------------------------------------
      # Daten auslesen und in "data_z" packen
      self.database.readData_zertifikat()
      data_z = self.database.read_zertifikat()

      # Daten nach Namen sortieren und in ein geordnetes Dict packen
      sorted_data_z = sorted(data_z.items(), key=lambda x: x[1]['bezeichnung_z'], reverse = False) #Alphabetisch sortiert
      ordered_dict_z = OrderedDict(sorted_data_z)

      return self.view_o.createList_auswertung_zertifikat(ordered_dict_z)
   
   #-------------------------------------------------------
   def getDetail_auswertung_zertifikat(self, id_spl):
   #-------------------------------------------------------
      # Daten auslesen und in die jeweilige "data_" packen
      self.database.readData_mitarbeiter()
      self.database.readData_weiterbildung()
      self.database.readData_zertifikat()
      self.database.readData_teilnahme()
      data_m = self.database.read_mitarbeiter()
      data_z = self.database.read_zertifikat()
      data_t = self.database.read_teilnahme()

      return self.view_o.createDetail_auswertung_zertifikat(data_m, data_z, data_t, id_spl)

# EOF