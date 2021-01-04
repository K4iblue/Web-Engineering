# coding: utf-8

import os
import os.path
import codecs
import json

#----------------------------------------------------------
class DataId(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.maxId_i_w = 0
      self.maxId_i_m = 0
      self.maxId_i_t = 0
      self.readMaxId_w()
      self.readMaxId_m()
      self.readMaxId_t()

   #-------------------------------------------------------
   def create_w(self):
   #-------------------------------------------------------
      self.maxId_i_w += 1
      self.saveMaxId_w()
      return str(self.maxId_i_w)

   #-------------------------------------------------------
   def create_t(self):
   #-------------------------------------------------------
      self.maxId_i_t += 1
      self.saveMaxId_t()
      return str(self.maxId_i_t)

   #-------------------------------------------------------
   def delete_t(self):
   #-------------------------------------------------------
      self.maxId_i_t -= 1
      self.saveMaxId_t()
      return str(self.maxId_i_t)

   #-------------------------------------------------------
   def readMaxId_w(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join('data', 'maxidWeiterbildung.json'), 'r', 'utf-8')
      except:
         self.maxId_i_w = 0
         self.saveMaxId_w()
      else:
         with fp_o:
            self.maxId_i_w = json.load(fp_o)
      return str(self.maxId_i_w)

   #-------------------------------------------------------
   def readMaxId_t(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join('data', 'maxidTeilnahmen.json'), 'r', 'utf-8')
      except:
         self.maxId_i_t = 0
         self.saveMaxId_t()
      else:
         with fp_o:
            self.maxId_i_t = json.load(fp_o)
      return str(self.maxId_i_t)

   #-------------------------------------------------------
   def saveMaxId_w(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'maxidWeiterbildung.json'), 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i_w, fp_o)

   #-------------------------------------------------------
   def saveMaxId_t(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'maxidTeilnahmen.json'), 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i_t, fp_o)

   #-------------------------------------------------------
   def delete_w(self):
   #-------------------------------------------------------
      self.maxId_i_w -= 1
      self.saveMaxId_w()
      return str(self.maxId_i_w)
   
   #-------------------------------------------------------
   def create_m(self):
   #-------------------------------------------------------
      self.maxId_i_m += 1
      self.saveMaxId_m()
      return str(self.maxId_i_m)

   #-------------------------------------------------------
   def readMaxId_m(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join('data', 'maxidMitarbeiter.json'), 'r', 'utf-8')
      except:
         self.maxId_i_m = 0
         self.saveMaxId_m()
      else:
         with fp_o:
            self.maxId_i_m = json.load(fp_o)
      return str(self.maxId_i_m)

   #-------------------------------------------------------
   def saveMaxId_m(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'maxidMitarbeiter.json'), 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i_m, fp_o)

   #-------------------------------------------------------
   def delete_m(self):
   #-------------------------------------------------------
      self.maxId_i_m -= 1
      self.saveMaxId_m()
      return str(self.maxId_i_m)
# EOF