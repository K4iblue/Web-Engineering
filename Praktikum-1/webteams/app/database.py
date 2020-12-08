# coding: utf-8

import os
import os.path
import codecs
import json

from . import dataid

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.data_o = None
      self.maxId_o = dataid.DataId_cl()
      self.readData_p()

   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------
      id_s = self.maxId_o.create_px()
      self.data_o[str(id_s)] = data_opl
      self.saveData_p()
      return str(id_s)

   #-------------------------------------------------------
   def read_px(self, id_spl = None):
   #-------------------------------------------------------
      data_o = None
      if id_spl == None:
         data_o = self.data_o
      else:
         if id_spl in self.data_o:
               data_o = self.data_o[id_spl]
      return data_o

   #-------------------------------------------------------
   def update_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      status_b = False
      if id_spl in self.data_o:
         self.data_o[id_spl] = data_opl
         self.saveData_p()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_px(self, id_spl):
   #-------------------------------------------------------
      status_b = False
      if self.data_o.pop(id_spl, None) != None:
         self.saveData_p()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------
      return ['', '', '', '', '', '', '', '',]                 # Ergänzung: Zweites Team mitglied hinzufügen // Semesteranzahl hinzugfügen

   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join('data', 'webteams.json'), 'r', 'utf-8')
      except:
         self.data_o = {}
         self.saveData_p()
      else:
         with fp_o:
            self.data_o = json.load(fp_o)
      return

   #-------------------------------------------------------
   def saveData_p(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join('data', 'webteams.json'), 'w', 'utf-8') as fp_o:
         json.dump(self.data_o, fp_o, indent=3)

# EOF