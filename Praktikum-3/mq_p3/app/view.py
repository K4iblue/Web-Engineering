# coding: utf-8
from .database import Database_cl
import json

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl

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
   def createList_w(self, data_w):
   #-------------------------------------------------------

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
   def createDetail_t(self, data_m, data_w, data_t, data_tIDs):
   #-------------------------------------------------------

      datas_t = {**data_m, **data_w, **data_t, **data_tIDs}  # Hier werden alle Daten zu einem Dictionary zusammengefügt. !!!!!data_t verursacht, dass angemeldetete weiterbilungen nicht angezeigt werden in teilnahmemitarbeiteranzeige.tpl, weil jede ID nur einmal übergeben wird!!!!!

      return json.dumps(datas_t)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - Mitarbeiter
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_a(self, data_m, data_w):
   #-------------------------------------------------------
      
      datas_a = {**data_m, **data_w}

      return json.dumps(datas_a)

   #-------------------------------------------------------
   def createDetail_a(self, data_m, data_w, data_t, id_spl):
   #-------------------------------------------------------

      id_m = data_m[id_spl]['id_m']
      datas_am = []  # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      datas_am.append(data_m[id_spl])

      for item in data_t:  # Durch alle Teilnahmen iterieren
         if id_m == data_t[item]['id_m']:
            id_w = data_t[item]['id_w']
            datas_am.append(data_w[id_w])

      return json.dumps(datas_am)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - Weiterbildung 
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_auswertung_weiterbildung(self, data_w):
   #-------------------------------------------------------
      return json.dumps(data_w)

   #-------------------------------------------------------
   def createDetail_auswertung_weiterbildung(self, data_m, data_w, data_t, id_spl):
   #-------------------------------------------------------
      status = "erfolgreich"        # Status nach dem wir die Mitarbeiter sortieren
      datas_w = []                  # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      
      id_w = id_spl                 # Weiterbildungs ID auslesen         
      datas_w.append(data_w)        # Weiterbildungsdaten in die Liste eintragen

      for item in data_t:  # Durch alle Teilnahmen iterieren
         if status == data_t[item]['status'] and id_w == data_t[item]['id_w']:   # Kontrolle ob Status "Erfolgreich" ist und ob Zertifikat ID in data_t (ohne das zeigt er die Mitarbeiter bei jedem Zertifikat an, obwohl man nicht in Teilnahme steht)
            id_m = data_t[item]['id_m']   # Mitarbeiter ID auslesen         
            datas_w.append(data_m[id_m])  # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_w)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - ZERTIFIKAT 
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_z(self, data_z):
   #-------------------------------------------------------
      return json.dumps(data_z)

   #-------------------------------------------------------
   def createDetail_z(self, data_m, data_w, data_z, data_t, id_spl):
   #-------------------------------------------------------
      status = "erfolgreich"        # Status nach dem wir die Mitarbeiter sortieren
      datas_z = []                  # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      id_w = data_z[id_spl]['id_w']

      for item in data_t:  # Durch alle Teilnahmen iterieren
         if status == data_t[item]['status'] and id_w == data_t[item]['id_w']:   # Kontrolle ob Status "Erfolgreich" ist und ob Zertifikat ID in data_t (ohne das zeigt er die Mitarbeiter bei jedem Zertifikat an, obwohl man nicht in Teilnahme steht)
            id_m = data_t[item]['id_m']   # Mitarbeiter ID auslesen         
            datas_z.append(data_m[id_m])  # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_z)

# EOF