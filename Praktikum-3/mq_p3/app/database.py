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
        self.readData_mitarbeiter()
        self.readData_weiterbildung()
        self.readData_qualifikation()
        self.readData_zertifikat()
        self.readData_teilnahme()
        self.readData_teilnahmeIDs()


#-----------------------------------------------------------------------------------
# CREATE FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def create_mitarbeiter(self, data_m):
    #-------------------------------------------------------
        id_m = str(uuid.uuid4()) # UUID
        length = len(self.data_m)
        self.data_m[id_m] = data_m
        self.data_m[id_m]['id_m'] = str(id_m)
        length = len(self.data_m)
        self.saveData_mitarbeiter()
        return length-1

    #-------------------------------------------------------
    def create_weiterbildung(self, data_w, data_q, data_z):
    #-------------------------------------------------------
        id_w = str(uuid.uuid4()) # UUID

        # Qualifikation und Zertifikat auch erstellen
        id_q = self.create_qualifikation(data_q, id_w)
        id_z = self.create_zertifikat(data_z, id_w)

        length = len(self.data_w)
        self.data_w[id_w] = data_w
        self.data_w[id_w]['id_w'] = str(id_w)
        self.data_w[id_w]['id_q'] = str(id_q)
        self.data_w[id_w]['id_z'] = str(id_z)
        length = len(self.data_w)
        self.saveData_weiterbildung()

        return length-1

    #-------------------------------------------------------
    def create_qualifikation(self, data_q, id):
    #-------------------------------------------------------
        id_q = str(uuid.uuid4()) # UUID
        id_w = id
        self.data_q[id_q] = data_q
        self.data_q[id_q]['id_q'] = str(id_q)
        self.data_q[id_q]['id_w'] = str(id_w)
        self.saveData_qualifikation()
        return id_q

    #-------------------------------------------------------
    def create_zertifikat(self, data_z, id):
    #-------------------------------------------------------
        id_z = str(uuid.uuid4()) # UUID
        id_w = id
        self.data_z[id_z] = data_z
        self.data_z[id_z]['id_z'] = str(id_z)
        self.data_z[id_z]['id_w'] = str(id_w)
        self.saveData_zertifikat()
        return id_z

    #-------------------------------------------------------
    def create_teilnahme(self, data_t, id_w, id_m, data_new):
    #-------------------------------------------------------
        id_t = str(uuid.uuid4()) # UUID

        self.create_teilnahmeIDs(id_t)
        #if id_w not in data_t:
            #self.data_t[str(id_w)] = {} #Bei Mitarbeiter wird nur die Id in die Json eingetragen.
            #self.saveData_teilnahme()

        #self.data_t[str(id_w)][str(id_m)] = data_new
        self.data_t[str(id_t)] = data_new
        self.saveData_teilnahme()
        return str(id_t)

    #-------------------------------------------------------
    def create_teilnahmeIDs(self, id_t):
    #-------------------------------------------------------
        dataid = {"id_t": id_t}
        self.data_tIDs[str(id_t)] = dataid
        self.saveData_teilnahmeIDs()

#-----------------------------------------------------------------------------------
# READ FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def read_mitarbeiter(self, id_m = None):
    #-------------------------------------------------------
        data_m = None
        if id_m == None:
            data_m = self.data_m
        else:
            try:
                data_m = self.data_m[id_m]
            except:
                data_m = {}            
        return data_m

    #-------------------------------------------------------
    def read_weiterbildung(self, id_w = None):
    #-------------------------------------------------------
        data_w = None
        if id_w == None:
            data_w = self.data_w
        else:
            try:
                data_w = self.data_w[id_w]
            except:
                data_w = {}            
        return data_w

    #-------------------------------------------------------
    def read_qualifikation(self, id_q = None, data_w = None):
    #-------------------------------------------------------
        data_q = None
        if id_q == None:
            data_q = self.data_q
        else:
            try:
                data_q = self.data_q[data_w['id_q']]
            except:
                data_q = {}            
        return data_q

    #-------------------------------------------------------
    def read_zertifikat(self, id_z = None, data_w = None):
    #-------------------------------------------------------
        data_z = None
        if id_z == None:
            data_z = self.data_z
        else:
            try:
                data_z = self.data_z[data_w['id_z']]
            except:
                data_z = {}            
        return data_z

    #-------------------------------------------------------
    def read_teilnahme(self, id_t = None):
    #-------------------------------------------------------
        data_t = None
        if id_t == None:
            data_t = self.data_t
        else:
            try:
                data_t = self.data_t[id_t]
            except:
                data_t = {}            
        return data_t

    #-------------------------------------------------------
    def read_teilnahmeIDs(self, id_tID = None):
    #-------------------------------------------------------
        data_tIDs = None
        if id_tID == None:
            data_tIDs = self.data_tIDs
        else:
            try:
                data_tIDs = self.data_tIDs[id_tID]
            except:
                data_tIDs = {}            
        return data_tIDs


#-----------------------------------------------------------------------------------
# UPDATE FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def update_mitarbeiter(self, id_m, data_m):
    #-------------------------------------------------------
        if id_m in self.data_m:
            self.data_m[id_m] = data_m
            self.saveData_mitarbeiter()
        return

    #-------------------------------------------------------
    def update_weiterbildung(self, id_w, data_w, data_q, data_z):
    #-------------------------------------------------------
        data_tmp = self.read_weiterbildung(id_w)
        if id_w in self.data_w:
            id_q = self.update_qualifikation(data_tmp['id_q'], data_q)
            id_z = self.update_zertifikat(data_tmp['id_z'], data_z)

            self.data_w[id_w] = data_w
            self.data_w[id_w]['id_q'] = str(id_q)
            self.data_w[id_w]['id_z'] = str(id_z)
            self.saveData_weiterbildung()
        return

    #-------------------------------------------------------
    def update_qualifikation(self, id_q, data_q):
    #-------------------------------------------------------
        if id_q in self.data_q:
            self.data_q[id_q] = data_q
            self.data_q[id_q]['id_q'] = id_q
            self.saveData_qualifikation()
        return id_q

    #-------------------------------------------------------
    def update_zertifikat(self, id_z, data_z):
    #-------------------------------------------------------
        if id_z in self.data_z:
            self.data_z[id_z] = data_z
            self.data_z[id_z]['id_z'] = id_z
            self.saveData_zertifikat()
        return id_z

    #-------------------------------------------------------
    def update_teilnahme(self, data_t, data_tIDs, id_m, id_w, status):
    #-------------------------------------------------------
        for suche in data_tIDs: #iteriere durch die teilnahmeid json
            print ("Value : %s" %  suche)
            if id_m in data_t[suche]['id_m'] and id_w in data_t[suche]['id_w']:   #wenn id_w und id_m in teilnahme json vorhanden sind, dann ändere den Status
                self.data_t[suche]['status'] = status
                self.saveData_teilnahme()
                return str("Status wurde geändert!")
        return str("Status wurde nicht geändert!")


#-----------------------------------------------------------------------------------
# DELETE FUNKTIONEN
#-----------------------------------------------------------------------------------

    #-------------------------------------------------------
    def delete_mitarbeiter(self, id_m):
    #-------------------------------------------------------
        if self.data_m.pop(id_m) != None:
           self.saveData_mitarbeiter()
        return

    #-------------------------------------------------------
    def delete_weiterbildung(self, id_w):
    #-------------------------------------------------------
        id_q = self.data_w[id_w]['id_q']
        id_z = self.data_w[id_w]['id_z']
        if self.data_w.pop(id_w) != None:
            self.delete_qualifikation(id_q)
            self.delete_zertifikat(id_z)
            self.saveData_weiterbildung()
        return

    #-------------------------------------------------------
    def delete_qualifikation(self, id_q):
    #-------------------------------------------------------
        if self.data_q.pop(id_q) != None:
           self.saveData_qualifikation()
        return

    #-------------------------------------------------------
    def delete_zertifikat(self, id_z):
    #-------------------------------------------------------
        if self.data_z.pop(id_z) != None:
           self.saveData_zertifikat()
        return

    #-------------------------------------------------------
    def delete_teilnahme(self, id_w, id_m):
    #-------------------------------------------------------
        data_t = self.read_teilnahme()
        data_tIDs = self.read_teilnahmeIDs()

        for deletewert in data_tIDs: #iteriere durch die teilnahmeid json
            print ("Value : %s" %  deletewert)
            if id_w in data_t[deletewert]['id_w'] and id_m in data_t[deletewert]['id_m']:   #wenn id_w und id_m in teilnahme json vorhanden sind, dann lösche den Eintrag
                data_t.pop(deletewert, None)
                self.saveData_teilnahme()
                self.delete_teilnahmeIDs(deletewert)
                return str("Weiterbildung wurde storniert!")
        return str("Sie waren nicht angemeldet!")

    #-------------------------------------------------------
    def delete_teilnahmeIDs(self, id_t):
    #-------------------------------------------------------
        if self.data_tIDs.pop(id_t, None) != None:
           self.saveData_teilnahmeIDs()
        return

#-----------------------------------------------------------------------------------
# READ_DATA FUNKTIONEN
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
            #for loop_i in range(1,50):
                #self.data_t[loop_i] = {}
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
            #for loop_i in range(1,50):
                #self.data_t[loop_i] = {}
            self.saveData_teilnahmeIDs()
        else:
            with fp_o:
                self.data_tIDs = json.load(fp_o)
        return

#-----------------------------------------------------------------------------------
# SAVE_DATA FUNKTIONEN
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