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
		self.path_s = "C:\\Git\\Web-Engineering\\Praktikum-2\\mq"								# Hier Path zur Server.py eintragen
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
		data1_o = self.db_mitarbeiter_o.read_px()
		data2_o = self.db_weiterbildung_o.read_px()
		data3_o = self.db_teilnahme_o.read_px()
		
		datas_o = [data1_o, data2_o, data3_o]
		return self.view_o.hauptseite_px(datas_o)


#..............................................................
#........................MITARBEITER...........................
#..............................................................
	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_p(self): # Mitarbeiter Liste aufrufen
	#------------------------------------------------------
		data_o = self.db_mitarbeiter_o.read_px()
		return self.view_o.pflegemitarbeiter_px(data_o)
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_bearbeiten_p(self, id_spl=None): # Mitarbeiter erfassen oder bearbeiten
	#------------------------------------------------------
		if id_spl != None:
			data_o = self.db_mitarbeiter_o.read_px(id_spl)
		else:
			data_o = self.db_mitarbeiter_o.getDefault4_px()
			
		return self.view_o.pflegemitarbeiter_formular_px(data_o, id_spl)
	

	@cherrypy.expose
	#------------------------------------------------------
	def pflegemitarbeiter_speichern_p(self, **data_opl): # Mitarbeiter abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = [ data_opl["name_s"], data_opl["vorname_s"], data_opl["titel_s"], data_opl["taetigkeit_s"] ]

		if id_s != "None":
			self.db_mitarbeiter_o.update_px(id_s, data_a)
		else:
			id_s = self.db_mitarbeiter_o.create_px(data_a)
			
		return self.pflegemitarbeiter_bearbeiten_p(id_s)


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
		data0_o = self.db_mitarbeiter_o.read_px(id_spl)
		data1_o = self.db_weiterbildung_o.read_px()
		data2_o = self.db_teilnahme_o.read_px()
		data3_o = self.db_qualifikation_o.read_px()
		data4_o = self.db_zertifikat_o.read_px()
		
		datas_o = [data0_o, data1_o, data2_o, data3_o, data4_o]
		return self.view_o.pflegemitarbeiter_anzeigen_px(datas_o, id_spl)
	

#..............................................................
#........................WEITERBILDUNG.........................
#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def pflegeweiterbildung_p(self): # Weiterbildungs Liste aufrufen
	#-------------------------------------------------------
		data_o = self.db_weiterbildung_o.read_px()
		return self.view_o.pflegeweiterbildung_px(data_o)


	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_bearbeiten_p(self, id_spl=None): # Weiterbildung(inkl. Qualifikation / Zertifikat) erfassen oder bearbeiten
	#------------------------------------------------------
		if id_spl != None:
			data1_o = self.db_weiterbildung_o.read_px(id_spl)
		else:
			data1_o = self.db_weiterbildung_o.getDefault6_px()

		if id_spl != None:
			data2_o = self.db_qualifikation_o.read_px(id_spl)
		else:
			data2_o = self.db_qualifikation_o.getDefault3_px()

		if id_spl != None:
			data3_o = self.db_zertifikat_o.read_px(id_spl)
		else:
			data3_o = self.db_zertifikat_o.getDefault4_px()		

		datas_o = [data1_o, data2_o, data3_o]
		return self.view_o.pflegeweiterbildung_formular_px(datas_o, id_spl)
	

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
		
		if id_s != "None":
			self.db_weiterbildung_o.update_px(id_s, data_a)
		else:
			id_s = self.db_weiterbildung_o.create_px(data_a)
			
		return self.pflegeweiterbildung_bearbeiten_p(id_s)


	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_q_speichern_p(self, **data_opl): # Qualifikation abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]
		data_a = [ data_opl["bezeichnung_s"], data_opl["beschreibung_text"] ]
		
		if id_s != "None":
			self.db_qualifikation_o.update_px(id_s, data_a)
		else:
			id_s = self.db_qualifikation_o.create_px(data_a)
			
		return self.pflegeweiterbildung_bearbeiten_p(id_s)


	@cherrypy.expose
	#------------------------------------------------------
	def pflegeweiterbildung_z_speichern_p(self, **data_opl): # Zertifikat abspeichern
	#------------------------------------------------------
		id_s = data_opl["id_s"]

		data_a = [ data_opl["bezeichnung_s"], data_opl["beschreibung_text"], data_opl["berechtigtzu_s"] ]
		
		if id_s != "None":
			self.db_zertifikat_o.update_px(id_s, data_a)
		else:
			id_s = self.db_zertifikat_o.create_px(data_a)
			
		return self.pflegeweiterbildung_bearbeiten_p(id_s)

	
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
		data0_o = self.db_mitarbeiter_o.read_px()
		data1_o = self.db_weiterbildung_o.read_px()
		data2_o = self.db_teilnahme_o.read_px()
		data3_o = self.db_qualifikation_o.read_px(id_spl)
		data4_o = self.db_zertifikat_o.read_px(id_spl)
		
		datas_o = [data0_o, data1_o, data2_o, data3_o, data4_o]
		return self.view_o.pflegeweiterbildung_anzeigen_px(datas_o, id_spl)


#..............................................................
#....................SICHTWEISE.MITARBEITER....................
#..............................................................
	@cherrypy.expose
	#------------------------------------------------------
	def sichtweisemitarbeiter_p(self): # Sichtweise Mitarbeiter: Mitarbeiter Liste aufrufen
	#------------------------------------------------------
		data_o = self.db_mitarbeiter_o.read_px()
		return self.view_o.sichtweisemitarbeiter_px(data_o)


	@cherrypy.expose
	#------------------------------------------------------
	def sichtweisemitarbeiter_information_p(self, id_spl): # Sichtweise Mitarbeiter: Mitarbeiter Detailansicht aufrufen
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()
		data2_o = self.db_weiterbildung_o.read_px()
		data3_o = self.db_teilnahme_o.read_px()
		datas_o= [data1_o, data2_o, data3_o]
		
		return self.view_o.sichtweisemitarbeiter_information_px(datas_o, id_spl)
	

	@cherrypy.expose
	#------------------------------------------------------
	def sichtweisemitarbeiter_eintragen_p(self, idW_spl, idM_spl): # Sichtweise Mitarbeiter: Mitarbeiter in eine Weiterbildung eintragen
	#------------------------------------------------------
		#data_o = self.db_teilnahme_o.read_px()
		#id_s = None
		
		data_a = [idW_spl, idM_spl, "angemeldet"]
		self.db_teilnahme_o.create_px(data_a)
					
		return self.sichtweisemitarbeiter_information_p(idM_spl)
	

	@cherrypy.expose
	#-------------------------------------------------------
	def deleteteilnahme_p(self, id, idM_spl=None): # Sichtweise Mitarbeiter: Mitarbeiter aus einer Weiterbildung löschen
	#-------------------------------------------------------
		self.db_teilnahme_o.delete_px(id)
		return self.sichtweisemitarbeiter_information_p(idM_spl)	


#..............................................................
#....................SICHTWEISE.WEITERBILDUNGEN................
#..............................................................
	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_p(self): # Sichtweise Weiterbildung: Weiterbildungs Liste aufrufen
	#------------------------------------------------------
		data_o = self.db_weiterbildung_o.read_px()
		return self.view_o.sichtweiseweiterbildungen_px(data_o)
	
	
	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_p(self, id_spl): # Sichtweise Weiterbildung: Detailansicht für eine zukünftige Weiterbildung aufrufen
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()		
		data2_o = self.db_weiterbildung_o.read_px()
		data3_o = self.db_teilnahme_o.read_px()

		datas_o= [data1_o, data2_o, data3_o]		
		return self.view_o.sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_px(datas_o, id_spl)


	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_p(self, id_spl): # Sichtweise Weiterbildung: Detailansicht für eine aktuelle Weiterbildung aufrufen
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()		
		data2_o = self.db_weiterbildung_o.read_px()		
		data3_o = self.db_teilnahme_o.read_px()

		datas_o= [data1_o, data2_o, data3_o]
		return self.view_o.sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_px(datas_o, id_spl)


	@cherrypy.expose
	#------------------------------------------------------
	def sichtweiseweiterbildungen_Status_p(self, idW_spl, id_s, Status=None): # Sichtweise Weiterbildung: Status der Teilnahme ändern (Erfolgreich / nicht Erfolgreich)
	#------------------------------------------------------
		data1_o = self.db_mitarbeiter_o.read_px()
		data2_o = self.db_weiterbildung_o.read_px()
		data3_o = self.db_teilnahme_o.read_px()
		datas_o= [data1_o, data2_o, data3_o]

		idM_spl = data3_o[id_s][1]
		
		self.db_teilnahme_o.update_px(id_s, [idW_spl, idM_spl, Status])		
		return self.view_o.sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_px(datas_o, idW_spl)


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
		data_o = self.db_mitarbeiter_o.read_px() #Mitarbeiter
		sorted_list = sorted(data_o.items(), key=lambda x: x[1]) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		return self.view_o.auswertungmitarbeiter_px(myOrdDic)


	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_mitarbeiter_Info_p(self, id_spl):
	#-------------------------------------------------------
		data0_o = self.db_mitarbeiter_o.read_px() #Mitarbeiter
		sorted_list = sorted(data0_o.items(), key=lambda x: x[1]) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		data1_o = self.db_weiterbildung_o.read_px()		
		data2_o = self.db_teilnahme_o.read_px()		
		datas_o = [myOrdDic, data1_o, data2_o]
		
		return self.view_o.auswertungmitarbeiterInfo_px(datas_o, id_spl)


	#..............................................................
	#..................AUSWERTUNGEN.WEITERBILDUNGEN................
	#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_weiterbildungen_p(self):
	#-------------------------------------------------------
		data_o = self.db_weiterbildung_o.read_px()		
		
		sorted_list = sorted(data_o.items(), key=lambda x: x[1]) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		return self.view_o.auswertungweiterbildungen_px(myOrdDic)


	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_weiterbildung_Info_p(self, id_spl):
	#-------------------------------------------------------
		data0_o = self.db_mitarbeiter_o.read_px() #Mitarbeiter
		sorted_list = sorted(data0_o.items(), key=lambda x: x[1]) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		data1_o = self.db_weiterbildung_o.read_px()		
		data2_o = self.db_teilnahme_o.read_px()		
		datas_o = [myOrdDic, data1_o, data2_o]
		
		return self.view_o.auswertungweiterbildungInfo_px(datas_o, id_spl)


	#..............................................................
	#..................AUSWERTUNGEN.ZERTIFIKATE....................
	#..............................................................
	@cherrypy.expose
	#-------------------------------------------------------
	def auswertung_zertifikat_p(self):
	#-------------------------------------------------------
		data_o = self.db_zertifikat_o.read_px()		
		
		sorted_list = sorted(data_o.items(), key=lambda x: x[1]) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		
		return self.view_o.auswertungzertifikat_px(myOrdDic)

# EOF