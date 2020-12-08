# coding: utf-8

import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions                        # Ergänzung: History "Funktion" // Für Fehlerbehandlung

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.lookup_o = TemplateLookup('./templates')

   #-------------------------------------------------------
   def createList_px(self, data_opl, listform):                                              # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      if listform == "tabelle":                                                              # Hier wird ausgewählt welches template von
         template_o = self.lookup_o.get_template('list.tpl')                                 # Mako benutzt werden soll
         markup_s = template_o.render(data_o = data_opl, listform=listform)
         return markup_s
      elif listform == "liste":
         try:
            template_o = self.lookup_o.get_template("list2.tpl")
            markup_s = template_o.render(data_o=data_opl, listform=listform)
            return markup_s
         except:
            return exceptions.html_error_template().render()

   #-------------------------------------------------------
   def createForm_px(self, listform, id_spl, data_opl):                                      # Ergänzung: History "Funktion"
   #-------------------------------------------------------
      template_o = self.lookup_o.get_template('form.tpl')
      markup_s = template_o.render(data_o = data_opl, key_s = id_spl, listform=listform)
      return markup_s

# EOF