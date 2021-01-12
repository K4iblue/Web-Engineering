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
   def createDetail_m(self, data_m, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_w = {**data_m, **data_w, **data_q, **data_z}

      retVal_o = {
         'data': data_m
      }
      return json.dumps(datas_w)

   #-------------------------------------------------------
   def createList_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------
      
      datas_w = [data_w, data_q, data_z]

      retVal_o = {
         'data': datas_w
      }
      return json.dumps(data_w)

   #-------------------------------------------------------
   def createDetail_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_w = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      retVal_o = {
         'data': datas_w
      }
      return json.dumps(datas_w)


   #-------------------------------------------------------
   def createDetail_t(self, data_m, data_w):
   #-------------------------------------------------------

      datas_t = {**data_m, **data_w}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      retVal_o = {
         'data': datas_t
      }

      return json.dumps(datas_t)
# EOF