# coding: utf-8
from .database import Database_cl
import json

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl()

#-----------------------------------------------------------------------------------
# MITARBEITER FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_m(self, data_m):
   #-------------------------------------------------------
      
      return json.dumps(data_m)

   #-------------------------------------------------------
   def createDetail_m(self, data_m, data_w, data_q, data_z, data_t):
   #-------------------------------------------------------

      datas_m = {**data_m, **data_w, **data_q, **data_z, **data_t}

      return json.dumps(datas_m)

#-----------------------------------------------------------------------------------
# WEITERBILDUNG FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------
      
      datas_w = [data_w, data_q, data_z]

      return json.dumps(data_w)

   #-------------------------------------------------------
   def createDetail_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_w = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      return json.dumps(datas_w)

#-----------------------------------------------------------------------------------
# TEILNAHME FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createDetail_t(self, data_m, data_w, data_t):
   #-------------------------------------------------------

      datas_t = {**data_m, **data_w, **data_t}  # Hier werden alle Daten zu einem Dictionary zusammengefügt. !!!!!data_t verursacht, dass angemeldetete weiterbilungen nicht angezeigt werden in teilnahmemitarbeiteranzeige.tpl, weil jede ID nur einmal übergeben wird!!!!!

      return json.dumps(datas_t)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_a(self, data_m, data_w):
   #-------------------------------------------------------
      
      datas_a = {**data_m, **data_w}

      return json.dumps(datas_a)

   #-------------------------------------------------------
   def createDetail_a(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_a = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      return json.dumps(datas_a)

#-----------------------------------------------------------------------------------
# AUSWERTUNG ZERTIFIKAT FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_z(self, data_z):
   #-------------------------------------------------------
      return json.dumps(data_z)

   #-------------------------------------------------------
   def createDetail_z(self, data_m, data_z, data_t):
   #-------------------------------------------------------
      status = "erfolgreich"        # Status nach dem wir die Mitarbeiter sortieren, sollte wenn Teilnahme Weiterbildung fertig ist "Erfolgreich" sein
      datas_z = []                  # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen

      for item in data_t:                                         # Durch alle Teilnahmen iterieren
         if status in data_t[item]['status']:                     # Kontrolle ob Status "Erfolgreich" ist
            id_m = data_t[item]['id_m']                           # Mitarbeiter ID auslesen
            datas_z.append(self.database.read_mitarbeiter(id_m))  # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_z)

# EOF