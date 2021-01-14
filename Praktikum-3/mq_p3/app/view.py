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

   #-------------------------------------------------------
   def weiterbildung_anzeigen(self, data_m, data_w, data_q, data_z, data_t, id_spl):
   #-------------------------------------------------------
      datas_w_anzeigen = []            # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      datas_w_anzeigen.append(data_w)  # Weiterbildung in die Liste eintragen

      id_w = data_w ['id_w']           # "id_w" aus Weiterbildungsdaten auslesen 
      id_q = data_w['id_q']            # "id_q" aus Weiterbildungsdaten auslesen
      id_z = data_w['id_z']            # "id_z" aus Weiterbildungsdaten auslesen
      datas_w_anzeigen.append(data_q[id_q])  # Qualifikation in die Liste eintragen
      datas_w_anzeigen.append(data_z[id_z])  # Zertifikat in die Liste eintragen

      # Teilnehmer herausfiltern
      for item in data_t:  # Durch alle Teilnahmen iterieren
         if id_w == data_t[item]['id_w']:             # Wenn Weiterbildungs ID in Teilnahme gefunden wird
            id_m = data_t[item]['id_m']               # Mitarbeiter ID auslesen aus der gefundenen Teilnahme
            datas_w_anzeigen.append(data_m[id_m])     # Mitarbeiter Daten in die Liste eintragen

      return json.dumps(datas_w_anzeigen)

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
   def createList_auswertung_mitarbeiter(self, data_m):
   #-------------------------------------------------------
      return json.dumps(data_m)

   #-------------------------------------------------------
   def createDetail_auswertung_mitarbeiter(self, data_m, data_w, data_t, id_spl):
   #-------------------------------------------------------
      id_m = data_m[id_spl]['id_m']       # Mitarbeiter ID aus data_m auslesen
      datas_am = []                       # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      datas_am.append(data_m[id_spl])     # Mitarbeiterdaten in die Liste eintragen

      for item in data_t:  # Durch alle Teilnahmen iterieren
         if id_m == data_t[item]['id_m']:    # Wenn Mitarbeiter ID in Teilnahme gefunden wird
            id_w = data_t[item]['id_w']      # Weiterbildungs ID auslesen aus der gefundenen Teilnahme
            datas_am.append(data_w[id_w])    # Weiterbildungsdaten in die Liste eintragen

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
      datas_aw = []                 # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      id_w = id_spl                 # Weiterbildungs ID auslesen         
      datas_aw.append(data_w)       # Weiterbildungsdaten in die Liste eintragen

      for item in data_t:  # Durch alle Teilnahmen iterieren
         if status == data_t[item]['status'] and id_w == data_t[item]['id_w']:   # Kontrolle ob Status "Erfolgreich" ist und ob Zertifikat ID in data_t ist
            id_m = data_t[item]['id_m']                                          # Mitarbeiter ID auslesen         
            datas_aw.append(data_m[id_m])                                        # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_aw)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - ZERTIFIKAT 
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_auswertung_zertifikat(self, data_z):
   #-------------------------------------------------------
      return json.dumps(data_z)

   #-------------------------------------------------------
   def createDetail_auswertung_zertifikat(self, data_m, data_z, data_t, id_spl):
   #-------------------------------------------------------
      status = "erfolgreich"           # Status nach dem wir die Mitarbeiter sortieren
      datas_az = []                    # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      id_w = data_z[id_spl]['id_w']    # Weiterbildungs ID aus data_z auslesen

      for item in data_t:  # Durch alle Teilnahmen iterieren
         if status == data_t[item]['status'] and id_w == data_t[item]['id_w']:   # Kontrolle ob Status "Erfolgreich" ist und ob Zertifikat ID in data_t ist
            id_m = data_t[item]['id_m']                                          # Mitarbeiter ID auslesen         
            datas_az.append(data_m[id_m])                                        # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_az)

# EOF