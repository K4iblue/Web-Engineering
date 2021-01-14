# coding: utf-8
from .database import Database_cl
from datetime import date
import json

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.database = Database_cl

#-----------------------------------------------------------------------------------
# STARTSEITE FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createStartseite(self, data_m, data_w, data_t):
   #-------------------------------------------------------
      # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      data_startseite = {"mitarbeiter": "0","teilnahmen": "0","geplant": "0","laufend": "0", "abgeschlossen": "0"} 

      # Anzahl Mitarbeiter     
      data_startseite.update(mitarbeiter = len(data_m))  # Mitarbeiter zählen und in die Liste eintragen

      # Anzahl Teilnahmen
      data_startseite.update(teilnahmen = len(data_t))   # Teilnahmen zählen und in die Liste eintragen

      # Anzahl Weiterbildungen (Geplant, Laufend, Abgeschlossen)
      anzahlWeiterbildungen = {"geplant": "0","laufend": "0", "abgeschlossen": "0"}    # Dict für Weiterbildungs Anzahl
      today = date.today()                                                             # Aktuelles Datum, damit wir die Weiterbildungen entsprechend sortieren können
      currentDate = today.strftime("%Y-%M-%D")                                         # Datum zum String umwandeln
      w_Geplant = 0                                                                    # Variable für Geplante Weiterbildungen
      w_Laufend = 0                                                                    # Variable für Laufende Weiterbildungen
      w_Abgeschlossen = 0                                                              # Variable für Abgeschlossene Weiterbildungen
      
      for item in data_w:                                                                    # Durch alle Weiterbildungen iterieren
         if (currentDate < data_w[item]['von_w']):                                           # Geplante Weitebildungen finden
            w_Geplant = w_Geplant + 1                                                        # Variabele inkrementieren
         if (currentDate > data_w[item]['von_w'] and currentDate < data_w[item]['bis_w']):   # Laufende Weitebildungen finden
            w_Laufend = w_Laufend + 1                                                        # Variabele inkrementieren
         if (currentDate > data_w[item]['bis_w']):                                           # Abgschlossende Weiterbildungen finden
	         w_Abgeschlossen = w_Abgeschlossen + 1                                            # Variabele inkrementieren
      
      anzahlWeiterbildungen.update(geplant = w_Geplant, laufend = w_Laufend, abgeschlossen = w_Abgeschlossen)  # Weiterbildungen zusammenführen
      data_startseite.update(geplant = w_Geplant, laufend = w_Laufend, abgeschlossen = w_Abgeschlossen)        # Anzahl Weiterbildungen in die Liste eintragen   

      return json.dumps(data_startseite)  # Wandelt die Daten die übergeben wurden in einen JSON String um

#-----------------------------------------------------------------------------------
# MITARBEITER FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_m(self, data_m):
   #-------------------------------------------------------
      return json.dumps(data_m) # Wandelt die Daten die übergeben wurden in einen JSON String um

   #-------------------------------------------------------
   def createDetail_m(self, data_m, data_w, data_q, data_z, data_t):
   #-------------------------------------------------------
      datas_m = {**data_m, **data_w, **data_q, **data_z, **data_t}   # Hier werden alle Daten zu einem Dictionary zusammengefügt
      return json.dumps(datas_m)                                     # Wandelt die Daten in einen JSON String um

   #-------------------------------------------------------
   def mitarbeiter_anzeigen(self, data_m, data_w, data_q, data_z, data_t, id_spl):
   #-------------------------------------------------------
      status_erfolg = "erfolgreich"                             # Status nach dem wir die Teilnahmen sortieren
      datas_m_anzeigen = []                              # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      datas_m_anzeigen.append(data_m)                    # Mitarbeiter in die Liste eintragen
      id_m = id_spl                                      # Mitarbeiter ID

      # Weiterbildungen, Qualifikation, Zertifikate herausfiltern
      for item in data_t:                                # Durch alle Teilnahmen iterieren
         if id_m == data_t[item]['id_m']:                # Wenn Mitarbeiter ID in Teilnahme gefunden wird
            id_w = data_t[item]['id_w']                  # Weiterbildungs ID aus der gefundenen Teilnahme auslesen
            data_w[id_w]['status'] =  data_t[item]['status']
            datas_m_anzeigen.append(data_w[id_w])        # Weiterbildung in die Liste eintragen

            if status_erfolg == data_t[item]['status']:         # Bei Erfolgreicher Teilnahme, Qualifikation und Zertifikate auch eintragen
               id_q = data_w[id_w]['id_q']               # Qualifikations ID aus der gefundenen Teilnahme auslesen
               id_z = data_w[id_w]['id_z']               # Zertifikats ID aus der gefundenen Teilnahme auslesen            
               datas_m_anzeigen.append(data_q[id_q])     # Qualifikation in die Liste eintragen
               datas_m_anzeigen.append(data_z[id_z])     # Zertifikat in die Liste eintragen

      return json.dumps(datas_m_anzeigen) # Wandelt die Daten in einen JSON String um

#-----------------------------------------------------------------------------------
# WEITERBILDUNG FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_w(self, data_w):
   #-------------------------------------------------------
      return json.dumps(data_w)  # Wandelt die Daten die übergeben wurden in einen JSON String um

   #-------------------------------------------------------
   def createDetail_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------
      datas_w = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt
      return json.dumps(datas_w)                # Wandelt die Daten in einen JSON String um

   #-------------------------------------------------------
   def weiterbildung_anzeigen(self, data_m, data_w, data_q, data_z, data_t, id_spl):
   #-------------------------------------------------------
      datas_w_anzeigen = []                  # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      datas_w_anzeigen.append(data_w)        # Weiterbildung in die Liste eintragen

      id_w = data_w['id_w']                  # "id_w" aus Weiterbildungsdaten auslesen 
      id_q = data_w['id_q']                  # "id_q" aus Weiterbildungsdaten auslesen
      id_z = data_w['id_z']                  # "id_z" aus Weiterbildungsdaten auslesen
      datas_w_anzeigen.append(data_q[id_q])  # Qualifikation in die Liste eintragen
      datas_w_anzeigen.append(data_z[id_z])  # Zertifikat in die Liste eintragen

      # Teilnehmer herausfiltern
      for item in data_t:  # Durch alle Teilnahmen iterieren
         if id_w == data_t[item]['id_w']:                # Wenn Weiterbildungs ID in Teilnahme gefunden wird
            id_m = data_t[item]['id_m']                  # Mitarbeiter ID auslesen aus der gefundenen Teilnahme
            datas_w_anzeigen.append(data_m[id_m])        # Mitarbeiter Daten in die Liste eintragen

      return json.dumps(datas_w_anzeigen)                # Wandelt die Daten in einen JSON String um

#-----------------------------------------------------------------------------------
# TEILNAHME FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createDetail_t(self, data_m, data_w, data_t, data_tIDs):
   #-------------------------------------------------------
      datas_t = {**data_m, **data_w, **data_t, **data_tIDs} # Hier werden alle Daten zu einem Dictionary zusammengefügt
      return json.dumps(datas_t)                            # Wandelt die Daten in einen JSON String um

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - Mitarbeiter
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_auswertung_mitarbeiter(self, data_m):
   #-------------------------------------------------------
      return json.dumps(data_m)  # Wandelt die Daten die übergeben wurden in einen JSON String um

   #-------------------------------------------------------
   def createDetail_auswertung_mitarbeiter(self, data_m, data_w, data_t, id_spl):
   #-------------------------------------------------------
      id_m = data_m[id_spl]['id_m']       # Mitarbeiter ID aus data_m auslesen
      datas_am = []                       # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      datas_am.append(data_m[id_spl])     # Mitarbeiterdaten in die Liste eintragen

      for item in data_t:                          # Durch alle Teilnahmen iterieren
         if id_m == data_t[item]['id_m']:          # Wenn Mitarbeiter ID in Teilnahme gefunden wird
            id_w = data_t[item]['id_w']            # Weiterbildungs ID aus der gefundenen Teilnahme auslesen
            datas_am.append(data_w[id_w])          # Weiterbildungsdaten in die Liste eintragen

      return json.dumps(datas_am)   # Wandelt die Daten in einen JSON String um

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - Weiterbildung 
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_auswertung_weiterbildung(self, data_w):
   #-------------------------------------------------------
      return json.dumps(data_w)  # Wandelt die Daten die übergeben wurden in einen JSON String um

   #-------------------------------------------------------
   def createDetail_auswertung_weiterbildung(self, data_m, data_w, data_t, id_spl):
   #-------------------------------------------------------
      status = "erfolgreich"        # Status nach dem wir die Mitarbeiter sortieren
      datas_aw = []                 # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      id_w = id_spl                 # Weiterbildungs ID auslesen         
      datas_aw.append(data_w)       # Weiterbildungsdaten in die Liste eintragen

      for item in data_t:                                                           # Durch alle Teilnahmen iterieren
         if status == data_t[item]['status'] and id_w == data_t[item]['id_w']:      # Kontrolle ob Status "Erfolgreich" ist und ob Zertifikat ID in data_t ist
            id_m = data_t[item]['id_m']                                             # Mitarbeiter ID aus der gefundenen Teilnahme auslesen         
            datas_aw.append(data_m[id_m])                                           # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_aw)                                                   # Wandelt die Daten in einen JSON String um

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN - ZERTIFIKAT 
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_auswertung_zertifikat(self, data_z):
   #-------------------------------------------------------
      return json.dumps(data_z)  # Wandelt die Daten die übergeben wurden in einen JSON String um

   #-------------------------------------------------------
   def createDetail_auswertung_zertifikat(self, data_m, data_z, data_t, id_spl):
   #-------------------------------------------------------
      status = "erfolgreich"           # Status nach dem wir die Mitarbeiter sortieren
      datas_az = []                    # Hier schreiben wir alle Daten rein, die wir dann im Template benutzen
      id_w = data_z[id_spl]['id_w']    # Weiterbildungs ID aus data_z auslesen

      for item in data_t:                                                           # Durch alle Teilnahmen iterieren
         if status == data_t[item]['status'] and id_w == data_t[item]['id_w']:      # Kontrolle ob Status "Erfolgreich" ist und ob Zertifikat ID in data_t ist
            id_m = data_t[item]['id_m']                                             # Mitarbeiter ID aus der gefundenen Teilnahme auslesen         
            datas_az.append(data_m[id_m])                                           # Mitarbeiterdaten anhand ID auslesen und zu einer Liste zusammenfügen

      return json.dumps(datas_az)                                                   # Wandelt die Daten in einen JSON String um

# EOF