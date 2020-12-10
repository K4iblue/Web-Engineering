# coding: utf-8
import os.path
from mako.template import Template
from mako.lookup import TemplateLookup
import string
from datetime import date

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------
	#-------------------------------------------------------
	def __init__(self, path_spl):
	#-------------------------------------------------------
		# Pfad hier zur Vereinfachung fest vorgeben
		self.path_s = os.path.join(path_spl, "template")
		self.lookup_o = TemplateLookup(directories=self.path_s)
	
		#-------------------------------------------------------
	def create_p(self, template_spl, data_opl, id_spl=None):
	#-------------------------------------------------------
		template_o = self.lookup_o.get_template(template_spl)
		# mit der Methode render wird das zuvor 'übersetzte' Template ausgeführt
		# data_o sind die im Template angegebenen Daten
		# data_opl die übergebenen Daten
		markup_s = template_o.render(data_o = data_opl, id_str = id_spl)
		return markup_s
		
	#-------------------------------------------------------
	def createList_px(self, datas_opl):
	#-------------------------------------------------------
		return self.create_p('startseite.tpl', datas_opl)


	#-------------------------------------------------------
	def hauptseite_px(self, data_opl):
	#-------------------------------------------------------
		datum = date.today()
		markup_html = ""
		markup_html = self.create_p('startseite.tpl', [data_opl, datum])
		return markup_html
	

	#-------------------------------------------------------
	def pflegemitarbeiter_px(self, data_opl):
	#-------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('PflegeMitarbeiter//ListeMitarbeiter.tpl', data_opl)		
		return markup_s
	

	#-------------------------------------------------------
	def pflegemitarbeiter_formular_px(self, data_opl, id_spl):
	#-------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('PflegeMitarbeiter//FormularMitarbeiter.tpl', data_opl, id_spl)
		return markup_s
	

	# HTML Dateien werden aus mehreren Templates zusammengefügt
	# Wir benutzten mehrere templates, damit wir unterschiedliche Daten
	# An unterschiedliche "teile" der HTML Datei übergeben können
	#-------------------------------------------------------
	def pflegemitarbeiter_anzeigen_px(self, datas_opl, id_spl):
	#-------------------------------------------------------
		markup_s = ''
		markup_s += self.create_p('PflegeMitarbeiter//Anzeige0.tpl', datas_opl[0], id_spl)
		markup_s += self.create_p('PflegeMitarbeiter//Anzeige1.tpl', datas_opl, id_spl)
		
		return markup_s
	

	#--------------------------------------------------------
	def pflegeweiterbildung_px(self, data_opl):
	#--------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('PflegeWeiterbildung//ListeWeiterbildung.tpl', data_opl)
		return markup_s


	# HTML Dateien werden aus mehreren Templates zusammengefügt
	# Wir benutzten mehrere templates, damit wir unterschiedliche Daten
	# An unterschiedliche "teile" der HTML Datei übergeben können
	#-------------------------------------------------------
	def pflegeweiterbildung_formular_px(self, data_opl, id_spl):
	#-------------------------------------------------------
		markup_s = ''
		markup_s += self.create_p('PflegeWeiterbildung//FormularWeiterbildung1.tpl', data_opl[0], id_spl)
		markup_s += self.create_p('PflegeWeiterbildung//FormularWeiterbildung2.tpl', data_opl[1], id_spl)
		markup_s += self.create_p('PflegeWeiterbildung//FormularWeiterbildung3.tpl', data_opl[2], id_spl)
		return markup_s	
	

	#-------------------------------------------------------	
	def pflegeweiterbildung_anzeigen_px(self, datas_opl, id_spl):
	#-------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('PflegeWeiterbildung//AnzeigeWeiterbildung.tpl', datas_opl, id_spl)	
		return markup_s


	#-------------------------------------------------------
	def sichtweisemitarbeiter_px(self, data_opl):
	#-------------------------------------------------------
		markup_s = ''	
		markup_s = self.create_p('SichtweiseMitarbeiter//SichtweiseMitarbeiter.tpl', data_opl)
		return markup_s


	# HTML Dateien werden aus mehreren Templates zusammengefügt
	# Wir benutzten mehrere templates, damit wir unterschiedliche Daten
	# An unterschiedliche "teile" der HTML Datei übergeben können
	#-------------------------------------------------------
	def sichtweisemitarbeiter_information_px(self, datas_opl, id_spl):
	#-------------------------------------------------------
		datum = date.today()
		markup_s = ''
		markup_s += self.create_p('SichtweiseMitarbeiter//InformationMitarbeiter1.tpl', datas_opl[0][id_spl], id_spl)
		markup_s += self.create_p('SichtweiseMitarbeiter//InformationMitarbeiter2.tpl', [datas_opl, datum], id_spl)
		markup_s += self.create_p('SichtweiseMitarbeiter//InformationMitarbeiter3.tpl', datas_opl, id_spl)
		return markup_s
	

	#-------------------------------------------------------	
	def sichtweiseweiterbildungen_px(self, data_opl):
	#-------------------------------------------------------
		datum = date.today()
		markup_s = ''		
		markup_s = self.create_p('SichtweiseWeiterbildungen//SichtweiseWeiterbildung.tpl', [data_opl, datum])
		return markup_s


	#-------------------------------------------------------	
	def sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_px(self, datas_opl, id_spl):
	#-------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('SichtweiseWeiterbildungen//SichtweiseWeiterbildung_Info.tpl', datas_opl, id_spl)
		return markup_s	


	# HTML Dateien werden aus mehreren Templates zusammengefügt
	# Wir benutzten mehrere templates, damit wir unterschiedliche Daten
	# An unterschiedliche "teile" der HTML Datei übergeben können
	#-------------------------------------------------------	
	def sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_px(self, datas_opl, id_spl):
	#-------------------------------------------------------
		datum = date.today()
		markup_s = ''
		markup_s += self.create_p('SichtweiseWeiterbildungen//SichtweiseWeiterbildung_Aktuell1.tpl', datas_opl, id_spl)
		markup_s += self.create_p('SichtweiseWeiterbildungen//SichtweiseWeiterbildung_Aktuell2.tpl', [datas_opl, datum], id_spl)
		return markup_s		


	#--------------------------------------------------------
	def auswertungmitarbeiter_px(self, data_opl):
	#--------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('Auswertung//AuswertungMitarbeiter.tpl', data_opl)
		return markup_s
	

	# HTML Dateien werden aus mehreren Templates zusammengefügt
	# Wir benutzten mehrere templates, damit wir unterschiedliche Daten
	# An unterschiedliche "teile" der HTML Datei übergeben können
	#--------------------------------------------------------
	def auswertungmitarbeiterInfo_px(self, data_opl, id_str):
	#--------------------------------------------------------
		markup_s = ''
		markup_s += self.create_p('Auswertung//AuswertungMitarbeiterInfo1.tpl', data_opl[0][id_str])
		markup_s += self.create_p('Auswertung//AuswertungMitarbeiterInfo2.tpl', data_opl, id_str)
		return markup_s
	

	#--------------------------------------------------------
	def auswertungweiterbildungen_px(self, data_opl):
	#--------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('Auswertung//AuswertungWeiterbildung.tpl', data_opl)
		return markup_s
	

	# HTML Dateien werden aus mehreren Templates zusammengefügt
	# Wir benutzten mehrere templates, damit wir unterschiedliche Daten
	# An unterschiedliche "teile" der HTML Datei übergeben können
	#--------------------------------------------------------
	def auswertungweiterbildungInfo_px(self, datas_opl, id_spl):
	#--------------------------------------------------------
		markup_s = ''
		markup_s += self.create_p('Auswertung//AuswertungWeiterbildungInfo1.tpl', datas_opl[1], id_spl)
		markup_s += self.create_p('Auswertung//AuswertungWeiterbildungInfo2.tpl', datas_opl, id_spl)
		return markup_s
	

	#--------------------------------------------------------
	def auswertungzertifikat_px(self, data_opl):
	#--------------------------------------------------------
		markup_s = ''
		markup_s = self.create_p('Auswertung//AuswertungZertifikat.tpl', data_opl)
		return markup_s


# EOF