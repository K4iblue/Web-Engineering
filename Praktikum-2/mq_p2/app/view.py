# coding: utf-8

import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from datetime import date

#----------------------------------------------------------
class View(object):
#----------------------------------------------------------

	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.lookup = TemplateLookup('./templates')

	#-------------------------------------------------------
	def startseite(self, id_s, data_w):
	#-------------------------------------------------------
		datum = date.today()
		template = self.lookup.get_template('startseite.tpl')
		markup = template.render(id_s = id_s, data_w = data_w, datum = datum)
		return markup

	#-------------------------------------------------------
	def pflegeMitarbeiter(self, data_m):
	#-------------------------------------------------------
		template = self.lookup.get_template('pflegeMitarbeiter.tpl')
		markup = template.render(data_m = data_m)
		return markup

	#-------------------------------------------------------
	def anzeigeMitarbeiter(self, data_m, data_w, data_q, data_z, data_t, id):
	#-------------------------------------------------------
		template = self.lookup.get_template('anzeigeMitarbeiter.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_q = data_q, data_z = data_z, data_t = data_t, key_s = id)
		return markup

	#-------------------------------------------------------
	def anzeigeWeiterbildung(self, data_m, data_w, data_q, data_z, data_t, id):
	#-------------------------------------------------------
		template = self.lookup.get_template('anzeigeWeiterbildung.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_q = data_q, data_z = data_z, data_t = data_t, key_s = id)
		return markup

	#-------------------------------------------------------
	def pflegeWeiterbildung(self, data_w, data_q, data_z):
	#-------------------------------------------------------
		template = self.lookup.get_template('pflegeWeiterbildung.tpl')
		markup = template.render(data_w = data_w, data_q = data_q, data_z = data_z)
		return markup

	#-------------------------------------------------------
	def teilnahmeMitarbeiter(self, data_m):
	#-------------------------------------------------------
		template = self.lookup.get_template('teilnahmeMitarbeiter.tpl')
		markup = template.render(data_m = data_m)
		return markup

	#-------------------------------------------------------
	def teilnahmeMitarbeiteranzeige(self, data_m, data_w, data_t, id):
	#-------------------------------------------------------
		datum = date.today()
		template = self.lookup.get_template('teilnahmeMitarbeiteranzeige.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_t = data_t, key_s = id, datum = datum)
		return markup

	#-------------------------------------------------------
	def teilnahmeWeiterbildunganzeige(self, data_m, data_w, data_t, id):
	#-------------------------------------------------------
		datum = date.today()
		template = self.lookup.get_template('teilnahmeWeiterbildunganzeige.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_t = data_t, key_w = id, datum = datum)
		return markup

	#-------------------------------------------------------
	def teilnahmeWeiterbildung(self, data_w):
	#-------------------------------------------------------
		datum = date.today()
		template = self.lookup.get_template('teilnahmeWeiterbildung.tpl')
		markup = template.render(data_w = data_w, datum = datum)
		return markup

	#-------------------------------------------------------
	def auswertungMitarbeiter(self, data_m):
	#-------------------------------------------------------
		template = self.lookup.get_template('auswertungMitarbeiter.tpl')
		markup = template.render(data_m = data_m)
		return markup

	#-------------------------------------------------------
	def auswertungWeiterbildung(self, data_w):
	#-------------------------------------------------------
		template = self.lookup.get_template('auswertungWeiterbildung.tpl')
		markup = template.render(data_w = data_w)
		return markup

	#-------------------------------------------------------
	def auswertungWeiterbildunganzeige(self, data_m, data_w, data_t, id):
	#-------------------------------------------------------
		template = self.lookup.get_template('auswertungWeiterbildunganzeige.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_t = data_t, key_w = id)
		return markup

	#-------------------------------------------------------
	def auswertungMitarbeiteranzeige(self, data_m, data_w, data_t, id):
	#-------------------------------------------------------
		template = self.lookup.get_template('auswertungMitarbeiteranzeige.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_t = data_t, key_s = id)
		return markup
	
	#-------------------------------------------------------
	def auswertungZertifikatanzeige(self, data_m, data_w, data_t, id):
	#-------------------------------------------------------
		template = self.lookup.get_template('auswertungZertifikatanzeige.tpl')
		markup = template.render(data_m = data_m, data_w = data_w, data_t = data_t, key_z = id)
		return markup	

	#-------------------------------------------------------
	def auswertungZertifikate(self, data_z):
	#-------------------------------------------------------
		template = self.lookup.get_template('auswertungZertifikate.tpl')
		markup = template.render(data_z = data_z)
		return markup

	#-------------------------------------------------------
	def createForm_Mitarbeiter(self, id_m, data_m):
   	#-------------------------------------------------------
		template = self.lookup.get_template('formMitarbeiter.tpl')
		markup_s = template.render(data_m = data_m, key_s = id_m)
		return markup_s

	#-------------------------------------------------------
	def createForm_Weiterbildung(self, id_w, data_w, data_q, data_z):
   	#-------------------------------------------------------
		template_w = self.lookup.get_template('formWeiterbildung.tpl')
		markup_s = template_w.render(data_w = data_w, data_q = data_q, data_z = data_z, key_s = id_w)
		return markup_s

