# coding: utf-8

import json

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      pass

   #-------------------------------------------------------
   def createList_m(self, data_m):
   #-------------------------------------------------------
      
      retVal_o = {
         'data': data_m
      }
      return json.dumps(data_m)

   #-------------------------------------------------------
   def createDetail_m(self, data_m):
   #-------------------------------------------------------

      retVal_o = {
         'data': data_m
      }
      return json.dumps(data_m)

   #-------------------------------------------------------
   def createList_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------
      
      datas_w = [data_w, data_q, data_z]

      retVal_o = {
         'data': datas_w
      }
      return json.dumps(data_w)  #wenn hier auch datas_w übergeben wird, funktioniert es nicht mehr (bearbeiten und anzeigen). Lösen, da Daten für Beziehungen gebraucht werden

   #-------------------------------------------------------
   def createDetail_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_w = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      retVal_o = {
         'data': datas_w
      }
      return json.dumps(datas_w)

# EOF