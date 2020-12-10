# coding: utf-8
import cherrypy
import array
from collections import OrderedDict
from .db_mitarbeiter import DB_mitarbeiter_cl
from .db_weiterbildung import DB_weiterbildung_cl
from .db_teilnahme import DB_teilnahme_cl
from .db_qualifikation import DB_qualifikation_cl
from .db_zertifikat import DB_zertifikat_cl
from .view import View_cl
import os.path

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		# spezielle Initialisierung können hier eingetragen werden
		self.db_mitarbeiter_o = DB_mitarbeiter_cl()
		self.db_weiterbildung_o = DB_weiterbildung_cl()
		self.db_teilnahme_o = DB_teilnahme_cl()
		self.db_qualifikation_o = DB_qualifikation_cl()
		self.db_zertifikat_o = DB_zertifikat_cl()
		self.path_s = "E:\\Git\\Web-Engineering\\Praktikum-2\\mq"								# Hier Path zur Server.py eintragen
		self.view_o = View_cl(self.path_s)
	
	@cherrypy.expose
	#--------------------------------------------------------
	def index(self):
	#--------------------------------------------------------
		return self.hauptseite_p()
	
	@cherrypy.expose
	#-------------------------------------------------------
	def default(self, *arguments, **kwargs):
	#-------------------------------------------------------
		msg_s = "unbekannte Anforderung: " + \
			str(arguments) + \
			' ' + \
			str(kwargs)
		raise cherrypy.HTTPError(404, msg_s)
	default.exposed= True
		
	@cherrypy.expose
	#------------------------------------------------------
	def hauptseite_p(self):
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()				# Mitarbeiter Daten lesen
		data2_o = self.db_weiterbildung_o.read_px()				# Weiterbildungs Daten lesen
		data3_o = self.db_teilnahme_o.read_px()					# Teilnahme Daten lesen
		
		datas_o = [data1_o, data2_o, data3_o]					# Daten zusammenfügen
		return self.view_o.hauptseite_px(datas_o)				# An view.py übergeben


#..............................................................
#........................MITARBEITER...........................
#..............................................................
	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_p(self): # Mitarbeiter Liste aufrufen
	#------------------------------------------------------
		data_o = self.db_mitarbeiter_o.read_px()				# Mitarbeiter Daten lesen
		return self.view_o.pflegemitarbeiter_px(data_o)			# An view.py übergeben
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_bearbeiten_p(self, id_spl=None): # Mitarbeiter erfassen oder bearbeiten
	#------------------------------------------------------
		if id_spl != None:													# Wenn eine ID übergeben wurde
			data_o = self.db_mitarbeiter_o.read_px(id_spl)					# Mitarbeiter Daten lesen
		else:																# Ansonsten
			data_o = self.db_mitarbeiter_o.getDefault4_px()					# Leeres Formular lades
			
		return self.view_o.pflegemitarbeiter_formular_px(data_o, id_spl)	# An view.py übergeben
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_speichern_p(self, **data_opl): # Mitarbeiter abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = [ data_opl["name_s"], data_opl["vorname_s"], data_opl["titel_s"], data_opl["taetigkeit_s"] ]

		if id_s != "None":												# Wenn eine ID übergeben wurde
			self.db_mitarbeiter_o.update_px(id_s, data_a)				# Mitarbeiter Daten updaten
		else:															# Ansonsten
			id_s = self.db_mitarbeiter_o.create_px(data_a)				# Neuen Mitarbeiter erstellen mit den übergebenen Daten

		return self.pflegemitarbeiter_bearbeiten_p(id_s)				# Formular neu laden


	@cherrypy.expose
	#-------------------------------------------------------
	def deletemitarbeiter_p(self, id): # Mitarbeiter löschen
	#-------------------------------------------------------
		self.db_mitarbeiter_o.deletemitarbeiter_px(id)
		return self.pflegemitarbeiter_p()
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_anzeigen_p(self, id_spl):	# Mitarbeiter Detailansicht aufrufen
	#------------------------------------------------------
		data0_o = self.db_mitarbeiter_o.read_px(id_spl)							# Mitarbeiter Daten Laden
		data1_o = self.db_weiterbildung_o.read_px()								# Weiterbildungs Daten Laden
		data2_o = self.db_teilnahme_o.read_px()									# Teilnahme Daten Laden
		data3_o = self.db_qualifikation_o.read_px()								# Qualifikation Daten Laden
		data4_o = self.db_zertifikat_o.read_px()								# Zertifikat Daten Laden

		datas_o = [data0_o, data1_o, data2_o, data3_o, data4_o]					# Alle Daten zusammenfügen
		return self.view_o.pflegemitarbeiter_anzeigen_px(datas_o, id_spl)		# An view.py übergeben
	

#..............................................................
#........................WEITERBILDUNG.........................
#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def pflegeweiterbildung_p(self): # Weiterbildungs Liste aufrufen
	#-------------------------------------------------------
		data_o = self.db_weiterbildung_o.read_px()								# Weiterbildungs Daten Laden
		return self.view_o.pflegeweiterbildung_px(data_o)						# An view.py übergeben


	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_bearbeiten_p(self, id_spl=None): # Weiterbildung(inkl. Qualifikation / Zertifikat) erfassen oder bearbeiten
	#------------------------------------------------------
		if id_spl != None:														# Wenn eine ID übergeben wurde
			data1_o = self.db_weiterbildung_o.read_px(id_spl)					# Weiterbildungs Daten Laden
		else:																	# Ansonsten
			data1_o = self.db_weiterbildung_o.getDefault6_px()					# Leeres Weiterbildungs Formular laden

		if id_spl != None:														# Wenn eine ID übergeben wurde
			data2_o = self.db_qualifikation_o.read_px(id_spl)					# Qualifikation Daten Laden
		else:																	# Ansonsten
			data2_o = self.db_qualifikation_o.getDefault3_px()					# Leeres Qualifikation Formular laden

		if id_spl != None:														# Wenn eine ID übergeben wurde
			data3_o = self.db_zertifikat_o.read_px(id_spl)						# Zertifikat Daten Laden
		else:																	# Ansonsten
			data3_o = self.db_zertifikat_o.getDefault4_px()						# Leeres Zertifikat Formular laden

		datas_o = [data1_o, data2_o, data3_o]									# Alle Daten zusammenfügen
		return self.view_o.pflegeweiterbildung_formular_px(datas_o, id_spl)		# An view.py übergeben
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_speichern_p(self, **data_opl): # Weiterbildung abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]

		data_a = [ data_opl["bezeichnung_s"]
		, data_opl["von_date"]
		, data_opl["bis_date"]
		, data_opl["beschreibung_text"]
		, data_opl["max_teilnehmeranzahl_int"]
		, data_opl["min_teilnehmeranzahl_int"] ]
		
		if id_s != "None":														# Wenn eine ID übergeben wurde
			self.db_weiterbildung_o.update_px(id_s, data_a)						# Weiterbildungs Daten updaten
		else:																	# Ansonsten
			id_s = self.db_weiterbildung_o.create_px(data_a)					# Neue Weiterbildung erstellen
			
		return self.pflegeweiterbildung_bearbeiten_p(id_s)						# Formular neuladen


	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_q_speichern_p(self, **data_opl): # Qualifikation abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = [ data_opl["bezeichnung_s"], data_opl["beschreibung_text"] ]
		
		if id_s != "None":														# Wenn eine ID übergeben wurde
			self.db_qualifikation_o.update_px(id_s, data_a)						# Qualifikations Daten updaten
		else:																	# Ansonsten
			id_s = self.db_qualifikation_o.create_px(data_a)					# Neue Qualifikation erstellen
			
		return self.pflegeweiterbildung_bearbeiten_p(id_s)						# Formular neuladen


	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_z_speichern_p(self, **data_opl): # Zertifikat abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]

		data_a = [ data_opl["bezeichnung_s"], data_opl["beschreibung_text"], data_opl["berechtigtzu_s"] ]
		
		if id_s != "None":														# Wenn eine ID übergeben wurde
			self.db_zertifikat_o.update_px(id_s, data_a)						# Zertifikat Daten updaten
		else:																	# Ansonsten
			id_s = self.db_zertifikat_o.create_px(data_a)						# Neues Zertifikat erstellen
			
		return self.pflegeweiterbildung_bearbeiten_p(id_s)						# Formular neuladen

	
	@cherrypy.expose
	#-------------------------------------------------------
	def deleteweiterbildung_p(self, id): # Weiterbildung löschen
	#-------------------------------------------------------
		self.db_weiterbildung_o.delete_px(id)
		return self.pflegeweiterbildung_p()
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_anzeigen_p(self, id_spl): # Weiterbildung Detailansicht aufrufen
	#------------------------------------------------------
		data0_o = self.db_mitarbeiter_o.read_px()									# Mitarbeiter Daten Laden
		data1_o = self.db_weiterbildung_o.read_px()									# Weiterbildungs Daten Laden
		data2_o = self.db_teilnahme_o.read_px()										# Teilnahme Daten Laden
		data3_o = self.db_qualifikation_o.read_px(id_spl)							# Qualifikations Daten Laden
		data4_o = self.db_zertifikat_o.read_px(id_spl)								# Zertifikat Daten Laden
		
		datas_o = [data0_o, data1_o, data2_o, data3_o, data4_o]						# Alle Daten zusammenfügen
		return self.view_o.pflegeweiterbildung_anzeigen_px(datas_o, id_spl)			# An view.py übergeben


#..............................................................
#....................SICHTWEISE.MITARBEITER....................
#..............................................................
	@cherrypy.expose
	#------------------------------------------------------
	def sichtweisemitarbeiter_p(self): # Sichtweise Mitarbeiter: Mitarbeiter Liste aufrufen
	#------------------------------------------------------
		data_o = self.db_mitarbeiter_o.read_px()									# Mitarbeiter Daten Laden
		return self.view_o.sichtweisemitarbeiter_px(data_o)							# An view.py übergeben


	@cherrypy.expose
	#------------------------------------------------------
	def sichtweisemitarbeiter_information_p(self, id_spl): # Sichtweise Mitarbeiter: Mitarbeiter Detailansicht aufrufen
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()									# Mitarbeiter Daten Laden
		data2_o = self.db_weiterbildung_o.read_px()									# Weiterbildungs Daten Laden
		data3_o = self.db_teilnahme_o.read_px()										# Teilnahme Daten Laden
		datas_o= [data1_o, data2_o, data3_o]										# Alle Daten zusammenfügen
		
		return self.view_o.sichtweisemitarbeiter_information_px(datas_o, id_spl)	# An view.py übergeben
	

	@cherrypy.expose
	#------------------------------------------------------
	def sichtweisemitarbeiter_eintragen_p(self, idW_spl, idM_spl): # Sichtweise Mitarbeiter: Mitarbeiter in eine Weiterbildung eintragen
	#------------------------------------------------------
		data_a = [idW_spl, idM_spl, "angemeldet"]									# Teilnahme eintragen
		self.db_teilnahme_o.create_px(data_a)										# Neue Teilnahme erstellen
					
		return self.sichtweisemitarbeiter_information_p(idM_spl)					# Seite neuladen
	

	@cherrypy.expose
	#-------------------------------------------------------
	def deleteteilnahme_p(self, id, idM_spl=None): # Sichtweise Mitarbeiter: Mitarbeiter aus einer Weiterbildung löschen
	#-------------------------------------------------------
		self.db_teilnahme_o.delete_px(id)											# Teilnahme entfernen
		return self.sichtweisemitarbeiter_information_p(idM_spl)					# Seite neuladen


#..............................................................
#....................SICHTWEISE.WEITERBILDUNGEN................
#..............................................................
	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_p(self): # Sichtweise Weiterbildung: Weiterbildungs Liste aufrufen
	#------------------------------------------------------
		data_o = self.db_weiterbildung_o.read_px()									# Weiterbildungs Daten Laden
		return self.view_o.sichtweiseweiterbildungen_px(data_o)						# An view.py übergeben
	
	
	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_p(self, id_spl): # Sichtweise Weiterbildung: Detailansicht für eine zukünftige Weiterbildung aufrufen
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()														# Mitarbeiter Daten Laden
		data2_o = self.db_weiterbildung_o.read_px()														# Weiterbildungs Daten Laden
		data3_o = self.db_teilnahme_o.read_px()															# Teilnahme Daten Laden

		datas_o= [data1_o, data2_o, data3_o]															# Alle Daten zusammenfügen
		return self.view_o.sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_px(datas_o, id_spl) 	# An view.py übergeben


	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_p(self, id_spl): # Sichtweise Weiterbildung: Detailansicht für eine aktuelle Weiterbildung aufrufen
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()														# Mitarbeiter Daten Laden
		data2_o = self.db_weiterbildung_o.read_px()														# Weiterbildungs Daten Laden
		data3_o = self.db_teilnahme_o.read_px()															# Teilnahme Daten Laden

		datas_o= [data1_o, data2_o, data3_o]															# Alle Daten zusammenfügen
		return self.view_o.sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_px(datas_o, id_spl)		# An view.py übergeben


	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_Status_p(self, idW_spl, id_s, Status=None): # Sichtweise Weiterbildung: Status der Teilnahme ändern (Erfolgreich / nicht Erfolgreich)
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()														# Mitarbeiter Daten Laden
		data2_o = self.db_weiterbildung_o.read_px()														# Weiterbildungs Daten Laden
		data3_o = self.db_teilnahme_o.read_px()															# Teilnahme Daten Laden
		datas_o= [data1_o, data2_o, data3_o]															# Alle Daten zusammenfügen

		idM_spl = data3_o[id_s][1]																		# Mitarbeiter aus Teilnahme auslesen
		
		self.db_teilnahme_o.update_px(id_s, [idW_spl, idM_spl, Status])									# Teilnahme updaten (Erfolgreich / nicht Erfolgreich)
		return self.view_o.sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_px(datas_o, idW_spl)		# An view.py übergeben


	@cherrypy.expose
	#-------------------------------------------------------
	def deleteteilnahme2_p(self, id, idW_spl=None): # Sichtweise Weiterbildung: Mitarbeiter aus einer laufenden Weiterbildung löschen
	#-------------------------------------------------------
		self.db_teilnahme_o.delete_px(id)		
		return self.sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_p(idW_spl)


	#..............................................................
	#..................AUSWERTUNGEN.MITARBEITER....................
	#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_mitarbeiter_p(self):
	#-------------------------------------------------------
		data_o = self.db_mitarbeiter_o.read_px()					# Mitarbeiter Daten Laden
		sorted_list = sorted(data_o.items(), key=lambda x: x[1])	# Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		return self.view_o.auswertungmitarbeiter_px(myOrdDic)		# An view.py übergeben


	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_mitarbeiter_Info_p(self, id_spl):
	#-------------------------------------------------------
		data0_o = self.db_mitarbeiter_o.read_px() 							# Mitarbeiter Daten Laden
		sorted_list = sorted(data0_o.items(), key=lambda x: x[1]) 			# Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		data1_o = self.db_weiterbildung_o.read_px()							# Weiterbildungs Daten Laden
		data2_o = self.db_teilnahme_o.read_px()								# Teilnahme Daten Laden
		datas_o = [myOrdDic, data1_o, data2_o]								# Alle Daten zusammenfügen
		
		return self.view_o.auswertungmitarbeiterInfo_px(datas_o, id_spl)	# An view.py übergeben


	#..............................................................
	#..................AUSWERTUNGEN.WEITERBILDUNGEN................
	#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_weiterbildungen_p(self):
	#-------------------------------------------------------
		data_o = self.db_weiterbildung_o.read_px()					# Weiterbildungs Daten Laden
		sorted_list = sorted(data_o.items(), key=lambda x: x[1])	# Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		return self.view_o.auswertungweiterbildungen_px(myOrdDic)	# An view.py übergeben


	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_weiterbildung_Info_p(self, id_spl):
	#-------------------------------------------------------
		data0_o = self.db_mitarbeiter_o.read_px() 							# Mitarbeiter Daten Laden
		sorted_list = sorted(data0_o.items(), key=lambda x: x[1])			# Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)

		data1_o = self.db_weiterbildung_o.read_px()							# Weiterbildungs Daten Laden
		data2_o = self.db_teilnahme_o.read_px()								# Teilnahme Daten Laden
		datas_o = [myOrdDic, data1_o, data2_o]								# Alle Daten zusammenfügen
		
		return self.view_o.auswertungweiterbildungInfo_px(datas_o, id_spl)	# An view.py übergeben


	#..............................................................
	#..................AUSWERTUNGEN.ZERTIFIKATE....................
	#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_zertifikat_p(self):
	#-------------------------------------------------------
		data_o = self.db_zertifikat_o.read_px()		
		
		sorted_list = sorted(data_o.items(), key=lambda x: x[1]) 	#Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		return self.view_o.auswertungzertifikat_px(myOrdDic) 		# An view.py übergeben

# EOF