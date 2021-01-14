# coding: utf-8
import os
import os.path
import codecs
import json
import uuid

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
    
    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        self.data_m = None
        self.data_w = None
        self.data_q = None
        self.data_z = None
        self.data_t = None
        self.data_tIDs = None
        self.readData_mitarbeiter()         # Liest Daten aus der Mitarbeiter JSON und schreibt sie in "data_m"
        self.readData_weiterbildung()       # Liest Daten aus der Weiterbildungs JSON und schreibt sie in "data_w"
        self.readData_qualifikation()       # Liest Daten aus der Qualifikations JSON und schreibt sie in "data_q"
        self.readData_zertifikat()          # Liest Daten aus der Zertifikats JSON und schreibt sie in "data_z"
        self.readData_teilnahme()           # Liest Daten aus der Teilnahme JSON und schreibt sie in "data_t"
        self.readData_teilnahmeIDs()        # Liest Daten aus der TeilnameIDs JSON und schreibt sie in "data_tIDs"


#-----------------------------------------------------------------------------------
# CREATE FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def create_mitarbeiter(self, data_m):
    #-------------------------------------------------------
        id_m = str(uuid.uuid4())                        # UUID für Mitarbeiter erstellen 
        self.data_m[id_m] = data_m                      # Neuen Eintrag mit der UUID in "data_m" erstellen 
        self.data_m[id_m]['id_m'] = str(id_m)           # UUID als "id_m" in "data_m" einfügen
        self.saveData_mitarbeiter()                     # Neuen Mitarbeiter abspeichern
        return id_m                                     # UUID zurückgeben

    #-------------------------------------------------------
    def create_weiterbildung(self, data_w, data_q, data_z):
    #-------------------------------------------------------
        id_w = str(uuid.uuid4())                        # UUID für Weiterbildunge erstellen
        id_q = self.create_qualifikation(data_q, id_w)  # Qualifikation auch erstellen, mithilfe der "id_w"
        id_z = self.create_zertifikat(data_z, id_w)     # Zertifikat auch erstellen, mithilfe der "id_w"
        self.data_w[id_w] = data_w                      # Neuen Eintrag mit der UUID in "data_w" erstellen
        self.data_w[id_w]['id_w'] = str(id_w)           # UUID als "id_w" in "data_w" einfügen
        self.data_w[id_w]['id_q'] = str(id_q)           # UUID der Qualifikation als "id_q" in "data_w" einfügen
        self.data_w[id_w]['id_z'] = str(id_z)           # UUID des Zertifikats als "id_z" in "data_w" einfügen
        self.saveData_weiterbildung()                   # Neue Weiterbildung abspeichern
        return id_w                                     # UUID zurückgeben

    #-------------------------------------------------------
    def create_qualifikation(self, data_q, id):
    #-------------------------------------------------------
        id_q = str(uuid.uuid4())                        # UUID für Qualifikation erstellen
        id_w = id                                       # "id_w" wurde von "create_weiterbildung" übergeben
        self.data_q[id_q] = data_q                      # Neuen Eintrag mit der UUID in "data_q" erstellen
        self.data_q[id_q]['id_q'] = str(id_q)           # UUID als "id_q" in "data_q" einfügen
        self.data_q[id_q]['id_w'] = str(id_w)           # UUID der Weiterbildung als "id_w" in "data_q" einfügen
        self.saveData_qualifikation()                   # Neue Qualifikation abspeichern
        return id_q                                     # UUID zurückgeben

    #-------------------------------------------------------
    def create_zertifikat(self, data_z, id):
    #-------------------------------------------------------
        id_z = str(uuid.uuid4())                        # UUID für Zertifikat erstellen
        id_w = id                                       # "id_w" wurde von "create_weiterbildung" übergeben
        self.data_z[id_z] = data_z                      # Neuen Eintrag mit der UUID in "data_z" erstellen
        self.data_z[id_z]['id_z'] = str(id_z)           # UUID als "id_z" in "data_z" einfügen
        self.data_z[id_z]['id_w'] = str(id_w)           # UUID der Weiterbildung als "id_w" in "data_z" einfügen
        self.saveData_zertifikat()                      # Neues Zertifikat abspeichern
        return id_z                                     # UUID zurückgeben

    #-------------------------------------------------------
    def create_teilnahme(self, data_t, id_w, id_m, data_new):
    #-------------------------------------------------------
        id_t = str(uuid.uuid4())                        # UUID für Zertifikat erstellen
        self.create_teilnahmeIDs(id_t)                  # TeilnahmeIDs auch erstellen, mithilfe der "id_t"
        self.data_t[str(id_t)] = data_new               # Neuen Eintrag mit der UUID in "data_t" erstellen
        self.saveData_teilnahme()                       # Neue Teilnahme abspeichern
        return str(id_t)                                # UUID zurückgeben

    #-------------------------------------------------------
    def create_teilnahmeIDs(self, id_t):
    #-------------------------------------------------------
        dataid = {"id_t": id_t}                         # "id_t" wurde von "create_teilnahme" übergeben und wird in das dict "dataid" als "id_t" geschrieben
        self.data_tIDs[str(id_t)] = dataid              # Neuen Eintrag mit der "id_t" in "data_tIDs" erstellen
        self.saveData_teilnahmeIDs()                    # Neue TeilnahmeIDs abspeichern

#-----------------------------------------------------------------------------------
# READ FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def read_mitarbeiter(self, id_m = None):
    #-------------------------------------------------------
        data_m = None                                   # "data_m" wird "geleert"
        if id_m == None:                                # Wenn keine ID vorhanden ist
            data_m = self.data_m                        # Werden alle Mitarbeiter in "data_m" gelesen
        else:                                           # Ansonsten
            try:                                        
                data_m = self.data_m[id_m]              # Werden die Daten des Mitarbeiter mit der passenden "ID" in "data_m" gelesen
            except:                                     # Falls dies nicht möglich war
                data_m = {}                             # Bleibt "data_m" leer
        return data_m                                   # "data_m" zurück geben

    #-------------------------------------------------------
    def read_weiterbildung(self, id_w = None):
    #-------------------------------------------------------
        data_w = None                                   # "data_w" wird "geleert"
        if id_w == None:                                # Wenn keine ID vorhanden ist
            data_w = self.data_w                        # Werden alle Weiterbildungen in "data_w" gelesen
        else:                                           # Ansonsten
            try:
                data_w = self.data_w[id_w]              # Werden die Daten der Weiterbildung mit der passenden "ID" in "data_w" gelesen
            except:                                     # Falls dies nicht möglich war
                data_w = {}                             # Bleibt "data_w" leer
        return data_w                                   # "data_w" zurück geben

    #-------------------------------------------------------
    def read_qualifikation(self, id_q = None, data_w = None):
    #-------------------------------------------------------
        data_q = None                                   # "data_q" wird "geleert"
        if id_q == None:                                # Wenn keine ID vorhanden ist
            data_q = self.data_q                        # Werden alle Qualifikationen in "data_q" gelesen
        else:                                           # Ansonsten
            try:
                data_q = self.data_q[data_w['id_q']]    # Werden die Daten der Qualifikation mit der passenden "ID" in "data_q" gelesen
            except:                                     # Falls dies nicht möglich war
                data_q = {}                             # Bleibt "data_q" leer
        return data_q                                   # "data_q" zurück geben

    #-------------------------------------------------------
    def read_zertifikat(self, id_z = None, data_w = None):
    #-------------------------------------------------------
        data_z = None                                   # "data_z" wird "geleert"
        if id_z == None:                                # Wenn keine ID vorhanden ist
            data_z = self.data_z                        # Werden alle Zertifikate in "data_z" gelesen
        else:                                           # Ansonsten
            try:
                data_z = self.data_z[data_w['id_z']]    # Werden die Daten des Zertifikat mit der passenden "ID" in "data_z" gelesen
            except:                                     # Falls dies nicht möglich war
                data_z = {}                             # Bleibt "data_z" leer
        return data_z                                   # "data_z" zurück geben

    #-------------------------------------------------------
    def read_teilnahme(self, id_t = None):
    #-------------------------------------------------------
        data_t = None                                   # "data_t" wird "geleert"
        if id_t == None:                                # Wenn keine ID vorhanden ist
            data_t = self.data_t                        # Werden alle Teilnahmen in "data_t" gelesen
        else:                                           # Ansonsten
            try:
                data_t = self.data_t[id_t]              # Werden die Daten der Teilnahmen mit der passenden "ID" in "data_t" gelesen
            except:                                     # Falls dies nicht möglich war
                data_t = {}                             # Bleibt "data_t" leer
        return data_t                                   # "data_t" zurück geben

    #-------------------------------------------------------
    def read_teilnahmeIDs(self, id_tID = None):
    #-------------------------------------------------------
        data_tIDs = None                                # "data_tIDs" wird "geleert"
        if id_tID == None:                              # Wenn keine ID vorhanden ist
            data_tIDs = self.data_tIDs                  # Werden alle TeilnahmenIDs in "data_tIDs" gelesen
        else:                                           # Ansonsten
            try:
                data_tIDs = self.data_tIDs[id_tID]      # Werden die Daten der TeilnahmenIDs mit der passenden "ID" in "data_tIDs" gelesen
            except:                                     # Falls dies nicht möglich war
                data_tIDs = {}                          # Bleibt "data_tIDs" leer
        return data_tIDs                                # "data_tIDs" zurück geben


#-----------------------------------------------------------------------------------
# UPDATE FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def update_mitarbeiter(self, id_m, data_m):
    #-------------------------------------------------------
        if id_m in self.data_m:                         # Wenn "id_m" in "data_m" ist
            self.data_m[id_m] = data_m                  # dann werden die alten Mitarbeiter Daten mit den neuen aus "data_m" überschrieben
            self.saveData_mitarbeiter()                 # Speichere Mitarbeiter Daten
        return

    #-------------------------------------------------------
    def update_weiterbildung(self, id_w, data_w, data_q, data_z):
    #-------------------------------------------------------
        data_tmp = self.read_weiterbildung(id_w)                        # Die Weiterbildung mit übergebenne ID werden in "data_tmp" geladen
        if id_w in self.data_w:                                         # Wenn "id_w" in "data_w" ist
            id_q = self.update_qualifikation(data_tmp['id_q'], data_q)  # Dann update auch die dazugehörige Qualifikation
            id_z = self.update_zertifikat(data_tmp['id_z'], data_z)     # Dann update auch das dazugehörige Zertifikat

            self.data_w[id_w] = data_w                                  # Die alten Weiterbildungs Daten werden mit den neuen aus "data_w" überschrieben
            self.data_w[id_w]['id_q'] = str(id_q)                       # "id_q" wird in die neuen Daten von "data_w" geschrieben
            self.data_w[id_w]['id_z'] = str(id_z)                       # "id_z" wird in die neuen Daten von "data_w" geschrieben
            self.saveData_weiterbildung()                               # Speichere Weiterbildung Daten
        return

    #-------------------------------------------------------
    def update_qualifikation(self, id_q, data_q):
    #-------------------------------------------------------
        if id_q in self.data_q:                         # Wenn "id_q" in "data_q" ist
            self.data_q[id_q] = data_q                  # dann werden die alten Qualifikations Daten mit den neuen aus "data_q" überschrieben
            self.data_q[id_q]['id_q'] = id_q            # "id_q" wird in die neuen Daten von "data_q" geschrieben
            self.saveData_qualifikation()               # Speichere Qualifikations Daten
        return id_q                                     # "id_q" zurückgeben

    #-------------------------------------------------------
    def update_zertifikat(self, id_z, data_z):
    #-------------------------------------------------------
        if id_z in self.data_z:                         # Wenn "id_z" in "data_z" ist
            self.data_z[id_z] = data_z                  # dann werden die alten Zertifikats Daten mit den neuen aus "data_z" überschrieben
            self.data_z[id_z]['id_z'] = id_z            # "id_z" wird in die neuen Daten von "data_z" geschrieben
            self.saveData_zertifikat()                  # Speichere Zertifikats Daten
        return id_z                                     # "id_z" zurückgeben

    #-------------------------------------------------------
    def update_teilnahme(self, data_t, data_tIDs, id_m, id_w, status):
    #-------------------------------------------------------
        for suche in data_tIDs:                                                     # Iteriere durch alle Teilnahmen ind der TeilnahmeIDs json
            print ("Value : %s" %  suche)                                           #
            if id_m in data_t[suche]['id_m'] and id_w in data_t[suche]['id_w']:     # Wenn "id_w" und "id_m" in "data_t" vorhanden sind, dann ändere den Status
                self.data_t[suche]['status'] = status                               # Ändere Status in bei der jeweiligen Teilnahme zu dem übergebenen Status
                self.saveData_teilnahme()                                           # Speichere Teilnahme Daten
                return str("Status wurde geändert!")                                #
        return str("Status wurde nicht geändert!")                                  #


#-----------------------------------------------------------------------------------
# DELETE FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def delete_mitarbeiter(self, id_m):
    #-------------------------------------------------------
        if self.data_m.pop(id_m) != None:           # Entferne Mitarbeiter mit der übergebenen ID
           self.saveData_mitarbeiter()              # Speichere Mitarbeiter Daten
        return

    #-------------------------------------------------------
    def delete_weiterbildung(self, id_w):
    #-------------------------------------------------------
        id_q = self.data_w[id_w]['id_q']            # Lese "id_q" aus "data_w" mithilfe der "id_w" aus
        id_z = self.data_w[id_w]['id_z']            # Lese "id_z" aus "data_w" mithilfe der "id_w" aus
        if self.data_w.pop(id_w) != None:           # Wenn die übergeben "id_w" in "data_w" vorhanden ist
            self.delete_qualifikation(id_q)         # Lösche dazugehörige Qualifikation
            self.delete_zertifikat(id_z)            # Lösche dazugehöriges Zertifikat
            self.saveData_weiterbildung()           # Speichere Weiterbildungs Daten
        return

    #-------------------------------------------------------
    def delete_qualifikation(self, id_q):
    #-------------------------------------------------------
        if self.data_q.pop(id_q) != None:           # Entferne Qualifikation mit der übergebenen ID
           self.saveData_qualifikation()            # Speichere Qualifikation Daten
        return

    #-------------------------------------------------------
    def delete_zertifikat(self, id_z):
    #-------------------------------------------------------
        if self.data_z.pop(id_z) != None:           # Entferne Zertifikat mit der übergebenen ID
           self.saveData_zertifikat()               # Speichere Zertifikat Daten
        return

    #-------------------------------------------------------
    def delete_teilnahme(self, id_w, id_m):
    #-------------------------------------------------------
        data_t = self.read_teilnahme()              # Lese alle Teilnahme Daten aus und schreibe sie in "data_t" 
        data_tIDs = self.read_teilnahmeIDs()        # Lese alle TeilnahmeIDs Daten aus und schreibe sie in "data_tIDs" 

        for deletewert in data_tIDs:                                                        # Iteriere durch die teilnahmeid JSON
            print ("Value : %s" %  deletewert)                                              #
            if id_w in data_t[deletewert]['id_w'] and id_m in data_t[deletewert]['id_m']:   # Wenn "id_w" und "id_m" in "data_t" vorhanden sind, dann lösche den Eintrag
                data_t.pop(deletewert, None)                                                #
                self.saveData_teilnahme()                                                   # Speichere Teilnahme Daten
                self.delete_teilnahmeIDs(deletewert)                                        # Lösche TeilnahmeIDs
                return str("Weiterbildung wurde storniert!")                                #
        return str("Sie waren nicht angemeldet!")                                           #

    #-------------------------------------------------------
    def delete_teilnahmeIDs(self, id_t):
    #-------------------------------------------------------
        if self.data_tIDs.pop(id_t, None) != None:      # Entferne TeilnahmeIDs mit der übergebenen ID
           self.saveData_teilnahmeIDs()                 # Speichere TeilnahmeIDs Daten
        return

#-----------------------------------------------------------------------------------
# READ_DATA FUNKTIONEN (Komplett wie in P2)                 ### Hier werden die Sachen aus den jeweiligen JSON Dateien gelesen ###
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def readData_mitarbeiter(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'mitarbeiter.json'), 'r', 'utf-8')
        except:
            self.data_m = {}
        
        else:
            with fp_o:
                self.data_m = json.load(fp_o)
        return

    #-------------------------------------------------------
    def readData_weiterbildung(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'weiterbildung.json'), 'r', 'utf-8')
        except:
            self.data_w = {}
        
        else:
            with fp_o:
                self.data_w = json.load(fp_o)
        return

    #-------------------------------------------------------
    def readData_qualifikation(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'qualifikation.json'), 'r', 'utf-8')
        except:
            self.data_q = {}
        
        else:
            with fp_o:
                self.data_q = json.load(fp_o)
        return

    #-------------------------------------------------------
    def readData_zertifikat(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'zertifikat.json'), 'r', 'utf-8')
        except:
            self.data_z = {}
        
        else:
            with fp_o:
                self.data_z = json.load(fp_o)
        return

    #-------------------------------------------------------
    def readData_teilnahme(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'teilnahme.json'), 'r', 'utf-8')
        except:
            self.data_t = {}
            self.saveData_teilnahme()
        else:
            with fp_o:
                self.data_t = json.load(fp_o)
        return

    #-------------------------------------------------------
    def readData_teilnahmeIDs(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', 'teilnahmeIDs.json'), 'r', 'utf-8')
        except:
            self.data_tIDs = {}
            self.saveData_teilnahmeIDs()
        else:
            with fp_o:
                self.data_tIDs = json.load(fp_o)
        return

#-----------------------------------------------------------------------------------
# SAVE_DATA FUNKTIONEN (Komplett wie in P2)                 ### Hier werden die Sachen in den jeweiligen JSON Dateien gespeichert ###
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def saveData_weiterbildung(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'weiterbildung.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_w, fp_o, indent=3)

    #-------------------------------------------------------
    def saveData_mitarbeiter(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'mitarbeiter.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_m, fp_o, indent=3)

    #-------------------------------------------------------
    def saveData_qualifikation(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'qualifikation.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_q, fp_o, indent=3)

    #-------------------------------------------------------
    def saveData_zertifikat(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'zertifikat.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_z, fp_o, indent=3)

    #-------------------------------------------------------
    def saveData_teilnahme(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'teilnahme.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_t, fp_o, indent=3)

    #-------------------------------------------------------
    def saveData_teilnahmeIDs(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', 'teilnahmeIDs.json'), 'w', 'utf-8') as fp_o:
            json.dump(self.data_tIDs, fp_o, indent=3)

# EOF