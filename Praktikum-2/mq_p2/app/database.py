# coding: utf-8

import os
import os.path
import codecs
import json

from . import dataid

#----------------------------------------------------------
class Database(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.data_m = None
      self.data_w = None
      self.data_q = None
      self.data_z = None
      self.data_t = None
      self.maxId_o = dataid.DataId()
      self.readData_mitarbeiter()
      self.readData_weiterbildung()
      self.readData_qualifikation()
      self.readData_zertifikate()
      self.readData_teilnahme()

   #-------------------------------------------------------
   def create_mitarbeiter(self, data_m):
   #-------------------------------------------------------
      id_m = self.maxId_o.create_m()
      self.data_m[str(id_m)] = data_m
      self.saveData_mitarbeiter()
      return str(id_m)

   #-------------------------------------------------------
   def create_weiterbildung(self, data_w):
   #-------------------------------------------------------
      id_w = self.maxId_o.create_w()
      self.data_w[str(id_w)] = data_w
      self.saveData_weiterbildung()
      return str(id_w)

   #-------------------------------------------------------
   def create_qualifikation(self, data_q):
   #-------------------------------------------------------
      id_w = self.maxId_o.readMaxId_w()
      self.data_q[str(id_w)] = data_q
      self.saveData_qualifikation()
      return str(id_w)

   #-------------------------------------------------------
   def create_zertifikate(self, data_z):
   #-------------------------------------------------------
      id_w = self.maxId_o.readMaxId_w()
      self.data_z[str(id_w)] = data_z
      self.saveData_zertifikate()
      return str(id_w)

   #-------------------------------------------------------
   def create_teilnahme(self, data_t, data_new, key_s, key_w):
   #-------------------------------------------------------
      self.maxId_o.create_t()
      self.data_t[str(key_w)][str(key_s)] = data_new
      self.saveData_teilnahme()
      return str(key_w)

   #-------------------------------------------------------
   def change_Status(self, data_t, key_w, key_t, status):
   #-------------------------------------------------------
      self.data_t[key_w][key_t][4] = status
      self.saveData_teilnahme()
      return str(key_t)

   #-------------------------------------------------------
   def read_mitarbeiter(self, id_m = None):
   #-------------------------------------------------------
      data_m = None
      if id_m == None:
         data_m = self.data_m
      else:
         if id_m in self.data_m:
               data_m = self.data_m[id_m]
      return data_m

   #-------------------------------------------------------
   def read_weiterbildung(self, id_w = None):
   #-------------------------------------------------------
      data_w = None
      if id_w == None:
         data_w = self.data_w
      else:
         if id_w in self.data_w:
               data_w = self.data_w[id_w]
      return data_w

   #-------------------------------------------------------
   def read_qualifikation(self, id_w = None):
   #-------------------------------------------------------
      data_q = None
      if id_w == None:
         data_q = self.data_q
      else:
         if id_w in self.data_q:
               data_q = self.data_q[id_w]
      return data_q

   #-------------------------------------------------------
   def read_zertifikate(self, id_w = None):
   #-------------------------------------------------------
      data_z = None
      if id_w == None:
         data_z = self.data_z
      else:
         if id_w in self.data_z:
               data_z = self.data_z[id_w]
      return data_z

   #-------------------------------------------------------
   def read_teilnahme(self, id_w = None):
   #-------------------------------------------------------
      data_t = None
      if id_w == None:
         data_t = self.data_t
      else:
         if id_w in self.data_t:
               data_t = self.data_t[id_w]
      return data_t

   #-------------------------------------------------------
   def update_mitarbeiter(self, id_m, data_m):
   #-------------------------------------------------------
      status_b = False  # Operation erfolgreich?
      if id_m in self.data_m:
         self.data_m[id_m] = data_m
         self.saveData_mitarbeiter()
         status_b = True   # id_spl in self.data_o vorhanden? Wenn ja, dann status_b = true, sonst false.
      return status_b

   #-------------------------------------------------------
   def update_weiterbildung(self, id_w, data_w):
   #-------------------------------------------------------
      status_b = False  # Operation erfolgreich?
      if id_w in self.data_w:
         self.data_w[id_w] = data_w
         self.saveData_weiterbildung()
         status_b = True   # id_spl in self.data_o vorhanden? Wenn ja, dann status_b = true, sonst false.
      return status_b

   #-------------------------------------------------------
   def update_qualifikation(self, id_w, data_q):
   #-------------------------------------------------------
      status_b = False  # Operation erfolgreich?
      if id_w in self.data_q:
         self.data_q[id_w] = data_q
         self.saveData_qualifikation()
         status_b = True   # id_spl in self.data_o vorhanden? Wenn ja, dann status_b = true, sonst false.
      return status_b

   #-------------------------------------------------------
   def update_zertifikate(self, id_w, data_z):
   #-------------------------------------------------------
      status_b = False  # Operation erfolgreich?
      if id_w in self.data_z:
         self.data_z[id_w] = data_z
         self.saveData_zertifikate()
         status_b = True   # id_spl in self.data_o vorhanden? Wenn ja, dann status_b = true, sonst false.
      return status_b

   #-------------------------------------------------------
   def delete_Mitarbeiter(self, id_m):
   #-------------------------------------------------------
      status_b = False
      if self.data_m.pop(id_m, None) != None:
         self.saveData_mitarbeiter()
         id_m = self.maxId_o.delete_m()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_Weiterbildung(self, id_w):
   #-------------------------------------------------------
      status_b = False
      if self.data_w.pop(id_w, None) != None:
         self.saveData_weiterbildung()
         id_w = self.maxId_o.delete_w()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_Qualifikation(self, id_w):
   #-------------------------------------------------------
      status_b = False
      if self.data_q.pop(id_w, None) != None:
         self.saveData_qualifikation() #maxid wird in delete_Weiterbildung schon heruntergesetzt, sonst Minusbereich
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_Zertifikate(self, id_w):
   #-------------------------------------------------------
      status_b = False
      if self.data_z.pop(id_w, None) != None:
         self.saveData_zertifikate()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_Teilnahme(self, key_s, key_t):
   #-------------------------------------------------------
      status_b = False
      if self.data_t[key_t].pop(key_s, None) != None:
         self.saveData_teilnahme()
         self.maxId_o.delete_t()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def getDefault_m(self):
   #-------------------------------------------------------
      return ['', '', '', '']

   #-------------------------------------------------------
   def getDefault_w(self):
   #-------------------------------------------------------
      return ['', '', '', '', '', '']    

   #-------------------------------------------------------
   def getDefault_q(self):
   #-------------------------------------------------------
      return ['', '', '']

   #-------------------------------------------------------
   def getDefault_z(self):
   #-------------------------------------------------------
      return ['', '', '', '']

   #-------------------------------------------------------
   def getDefault_t(self):
   #-------------------------------------------------------
      return ['', '', '', '', '']


   #-------------------------------------------------------
   def readData_mitarbeiter(self):
   #-------------------------------------------------------
      try:
         fp_m = codecs.open(os.path.join('data', 'mitarbeiter.json'), 'r', 'utf-8')
      except:
         self.data_m = {}
         self.saveData_mitarbeiter()
      else:
         with fp_m:
            self.data_m = json.load(fp_m)
      return

   #-------------------------------------------------------
   def readData_weiterbildung(self):
   #-------------------------------------------------------
      try:
         fp_w = codecs.open(os.path.join('data', 'weiterbildung.json'), 'r', 'utf-8')
      except:
         self.data_w = {}
         self.saveData_weiterbildung()
      else:
         with fp_w:
            self.data_w = json.load(fp_w)
      return

   #-------------------------------------------------------
   def readData_qualifikation(self):
   #-------------------------------------------------------
      try:
         fp_q = codecs.open(os.path.join('data', 'qualifikation.json'), 'r', 'utf-8')
      except:
         self.data_q = {}
         self.saveData_qualifikation()
      else:
         with fp_q:
            self.data_q = json.load(fp_q)
      return

   #-------------------------------------------------------
   def readData_zertifikate(self):
   #-------------------------------------------------------
      try:
         fp_z = codecs.open(os.path.join('data', 'zertifikate.json'), 'r', 'utf-8')
      except:
         self.data_z = {}
         self.saveData_zertifikate()
      else:
         with fp_z:
            self.data_z = json.load(fp_z)
      return

   #-------------------------------------------------------
   def readData_teilnahme(self):
   #-------------------------------------------------------
      try:
         fp_t = codecs.open(os.path.join('data', 'teilnahme.json'), 'r', 'utf-8')
      except:
         self.data_t = {}
         for loop_i in range(1,50):
            self.data_t[str(loop_i)] = {}
         self.saveData_teilnahme()
      else:
         with fp_t:
            self.data_t = json.load(fp_t)
      return

   #-------------------------------------------------------
   def saveData_mitarbeiter(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'mitarbeiter.json'), 'w', 'utf-8') as fp_m:
         json.dump(self.data_m, fp_m, indent=3)

   #-------------------------------------------------------
   def saveData_weiterbildung(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'weiterbildung.json'), 'w', 'utf-8') as fp_w:
         json.dump(self.data_w, fp_w, indent=3)

   #-------------------------------------------------------
   def saveData_qualifikation(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'qualifikation.json'), 'w', 'utf-8') as fp_q:
         json.dump(self.data_q, fp_q, indent=3)

   #-------------------------------------------------------
   def saveData_zertifikate(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'zertifikate.json'), 'w', 'utf-8') as fp_z:
         json.dump(self.data_z, fp_z, indent=3)

   #-------------------------------------------------------
   def saveData_teilnahme(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'teilnahme.json'), 'w', 'utf-8') as fp_t:
         json.dump(self.data_t, fp_t, indent=3)

# EOF