# coding: utf-8

import json

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      pass

#-----------------------------------------------------------------------------------
# MITARBEITER FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_m(self, data_m):
   #-------------------------------------------------------
      
      retVal_o = {
         'data': data_m
      }
      return json.dumps(data_m)

   #-------------------------------------------------------
   def createDetail_m(self, data_m, data_w, data_q, data_z, data_t):
   #-------------------------------------------------------

      datas_w = {**data_m, **data_w, **data_q, **data_z, **data_t}

      retVal_o = {
         'data': datas_w
      }
      return json.dumps(datas_w)

#-----------------------------------------------------------------------------------
# WEITERBILDUNG FUNKTIONEN
#-----------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------
# TEILNAHME FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createDetail_t(self, data_m, data_w, data_t):
   #-------------------------------------------------------

      datas_t = {**data_m, **data_w}  # Hier werden alle Daten zu einem Dictionary zusammengefügt  !!!Wenn hier **data_t mit übergeben wird (und das brauchen wir), wird die Weiterbildung, zu der man sich angemeldet hat, nicht mehr angezeigt, sondern Mitarbeiterdaten werden anstelle dessen übergeben, siehe Netzwerkverkehr, prüfen.!!!

      retVal_o = {
         'data': datas_t
      }

      return json.dumps(datas_t)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_a(self, data_m, data_w, data_z):
   #-------------------------------------------------------
      
      datas_a = [data_m, data_w, data_z]

      retVal_o = {
         'data': datas_a
      }
      return json.dumps(datas_a)

   #-------------------------------------------------------
   def createDetail_a(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_w = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      retVal_o = {
         'data': datas_w
      }
      return json.dumps(datas_w)

# EOF