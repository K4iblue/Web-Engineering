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
   def createList_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------
      
      datas_w = [data_w, data_q, data_z]

      return json.dumps(data_w)

   #-------------------------------------------------------
   def createDetail_w(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_w = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      return json.dumps(datas_w)

#-----------------------------------------------------------------------------------
# TEILNAHME FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createDetail_t(self, data_m, data_w, data_t):
   #-------------------------------------------------------

      datas_t = {**data_m, **data_w, **data_t}  # Hier werden alle Daten zu einem Dictionary zusammengefügt. !!!!!data_t verursacht, dass angemeldetete weiterbilungen nicht angezeigt werden in teilnahmemitarbeiteranzeige.tpl, weil jede ID nur einmal übergeben wird!!!!!

      return json.dumps(datas_t)

#-----------------------------------------------------------------------------------
# AUSWERTUNG FUNKTIONEN
#-----------------------------------------------------------------------------------

   #-------------------------------------------------------
   def createList_a(self, data_m, data_w):
   #-------------------------------------------------------
      
      datas_a = {**data_m, **data_w}

      return json.dumps(datas_a)

   #-------------------------------------------------------
   def createDetail_a(self, data_w, data_q, data_z):
   #-------------------------------------------------------

      datas_a = {**data_w, **data_q, **data_z}  # Hier werden alle Daten zu einem Dictionary zusammengefügt

      return json.dumps(datas_a)

# EOF