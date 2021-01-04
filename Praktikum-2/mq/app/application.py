# coding: utf-8

import cherrypy
from collections import OrderedDict
from .view import View
from .database import Database
from . import dataid

#----------------------------------------------------------
class Application(object):
#----------------------------------------------------------

	#----------------------------------------------------------
	def __init__(self):
	#----------------------------------------------------------
		self.view = View()
		self.database = Database()
		self.id = dataid.DataId()

	@cherrypy.expose
	#----------------------------------------------------------
	def index(self):
	#----------------------------------------------------------
		return self.startseite()

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


	#----------------------------------------------------------
	# Funktionen um die Templates zu rendern
	#----------------------------------------------------------
	@cherrypy.expose
	def startseite(self):
		id_m = self.id.readMaxId_m()		# Hier lesen wir die IDs aus der jeweiligen JSON Datei aus
		id_w = self.id.readMaxId_w()		# und fügen diese zu einer Liste zusammen
		id_t = self.id.readMaxId_t()
		id_s = [id_m, id_w, id_t]
		data_w = self.database.read_weiterbildung()
		return self.view.startseite(id_s, data_w)

	@cherrypy.expose
	def pflegeMitarbeiter(self):
		data_m = self.database.read_mitarbeiter()
		return self.view.pflegeMitarbeiter(data_m)

	@cherrypy.expose
	def pflegeWeiterbildung(self):
		data_w = self.database.read_weiterbildung()
		data_q = self.database.read_qualifikation()
		data_z = self.database.read_zertifikate()
		return self.view.pflegeWeiterbildung(data_w, data_q, data_z)

	@cherrypy.expose
	def teilnahmeMitarbeiter(self):
		data_m = self.database.read_mitarbeiter()
		return self.view.teilnahmeMitarbeiter(data_m)

	@cherrypy.expose
	def teilnahmeWeiterbildung(self):
		data_w = self.database.read_weiterbildung()
		return self.view.teilnahmeWeiterbildung(data_w)

	@cherrypy.expose
	def auswertungMitarbeiter(self):
		data_m = self.database.read_mitarbeiter()
		sorted_list = sorted(data_m.items(), key=lambda x: x[1], reverse = False) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		return self.view.auswertungMitarbeiter(myOrdDic)

	@cherrypy.expose
	def auswertungWeiterbildung(self):
		data_w = self.database.read_weiterbildung()
		sorted_list = sorted(data_w.items(), key=lambda x: x[1], reverse = False) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		return self.view.auswertungWeiterbildung(myOrdDic)

	@cherrypy.expose
	def auswertungZertifikate(self):
		data_z = self.database.read_zertifikate()
		sorted_list = sorted(data_z.items(), key=lambda x: x[1], reverse = False) #Alphabetisch sortiert
		myOrdDic = OrderedDict(sorted_list)
		return self.view.auswertungZertifikate(myOrdDic)

	#----------------------------------------------------------
	# Add-Funktionen
	#----------------------------------------------------------

	@cherrypy.expose
	def addmitarbeiter(self):                                 
		return self.createForm_Mitarbeiter()

	@cherrypy.expose
	def addweiterbildung(self):                                 
		return self.createForm_Weiterbildung()

	#----------------------------------------------------------
	# CreateForm-Funktionen
	#----------------------------------------------------------

	def createForm_Mitarbeiter(self, id_m = None):
		if id_m != None:
			data_m = self.database.read_mitarbeiter(id_m)
		else:
			data_m = self.database.getDefault_m()
		return self.view.createForm_Mitarbeiter(id_m, data_m)

	def createForm_Weiterbildung(self, id_w = None):
		if id_w != None:
			data_w = self.database.read_weiterbildung(id_w)
		else:
			data_w = self.database.getDefault_w()

		if id_w != None:
			data_q = self.database.read_qualifikation(id_w)
		else:
			data_q = self.database.getDefault_q()

		if id_w != None:
			data_z = self.database.read_zertifikate(id_w)
		else:
			data_z = self.database.getDefault_z()

		return self.view.createForm_Weiterbildung(id_w, data_w, data_q, data_z)


	#----------------------------------------------------------
	# Save-Funktionen
	#----------------------------------------------------------

	@cherrypy.expose
	def savemitarbeiter(self, id_spam, namemitarbeiter, vornamemitarbeiter, akagrad, taetigkeit):
		id_m = id_spam
		data_m = [namemitarbeiter, vornamemitarbeiter, akagrad, taetigkeit]
		if id_m != "None":
			self.database.update_mitarbeiter(id_m, data_m)
		else:
			self.database.create_mitarbeiter(data_m)
		return self.pflegeMitarbeiter()

	@cherrypy.expose
	def saveweiterbildung(self, id_spaw, bezeichnung_w, von_w, bis_w, beschreibung_w, maxteilnehmer_w, minteilnehmer_w, bezeichnung_q, beschreibung_q, bezeichnung_z, beschreibung_z, berechtigtzu_z):
		id_w = id_spaw
		data_w = [bezeichnung_w, von_w, bis_w, beschreibung_w, maxteilnehmer_w, minteilnehmer_w]
		data_q = [bezeichnung_q, beschreibung_q]
		data_z = [bezeichnung_z, beschreibung_z, berechtigtzu_z]

		if id_w != "None":
			self.database.update_weiterbildung(id_w, data_w)
			self.database.update_qualifikation(id_w, data_q)
			self.database.update_zertifikate(id_w, data_z)
		else:
			self.database.create_weiterbildung(data_w)
			self.database.create_qualifikation(data_q)
			self.database.create_zertifikate(data_z)
		return self.pflegeWeiterbildung()

	#----------------------------------------------------------
	# Edit-Funktionen
	#----------------------------------------------------------

	@cherrypy.expose
	def editmitarbeiter(self, id_m):                        
		return self.createForm_Mitarbeiter(id_m)

	@cherrypy.expose
	def editweiterbildung(self, id_w):                        
		return self.createForm_Weiterbildung(id_w)

   
   	#----------------------------------------------------------
	# Delete-Funktionen
	#----------------------------------------------------------

	@cherrypy.expose
	def deletemitarbeiter(self, id):
		self.database.delete_Mitarbeiter(id)
		data_t = self.database.read_teilnahme()
		for key_t in data_t:
			if id in data_t[key_t]:
				self.database.delete_Teilnahme(id, key_t)
		raise cherrypy.HTTPRedirect('/pflegeMitarbeiter')

	@cherrypy.expose
	def deleteweiterbildung(self, id):
		self.database.delete_Weiterbildung(id)
		self.database.delete_Qualifikation(id)
		self.database.delete_Zertifikate(id)
		raise cherrypy.HTTPRedirect('/pflegeWeiterbildung')

	#----------------------------------------------------------
	# Anzeige-Funktionen
	#----------------------------------------------------------

	@cherrypy.expose
	def anzeigeweiterbildung(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_q = self.database.read_qualifikation()
		data_z = self.database.read_zertifikate()
		data_t = self.database.read_teilnahme()
		return self.view.anzeigeWeiterbildung(data_m, data_w, data_q, data_z, data_t, id)

	@cherrypy.expose
	def anzeigemitarbeiter(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_q = self.database.read_qualifikation()
		data_z = self.database.read_zertifikate()
		data_t = self.database.read_teilnahme()
		return self.view.anzeigeMitarbeiter(data_m, data_w, data_q, data_z, data_t, id)

	@cherrypy.expose
	def teilnahmeMitarbeiteranzeige(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_t = self.database.read_teilnahme()
		return self.view.teilnahmeMitarbeiteranzeige(data_m, data_w, data_t, id)

	@cherrypy.expose
	def teilnahmeWeiterbildunganzeige(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_t = self.database.read_teilnahme()
		return self.view.teilnahmeWeiterbildunganzeige(data_m, data_w, data_t, id)

	@cherrypy.expose
	def anzeigeauswertungmitarbeiter(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_t = self.database.read_teilnahme()
		return self.view.auswertungMitarbeiteranzeige(data_m, data_w, data_t, id)
	
	@cherrypy.expose
	def anzeigeauswertungweiterbildung(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_t = self.database.read_teilnahme()
		return self.view.auswertungWeiterbildunganzeige(data_m, data_w, data_t, id)

	@cherrypy.expose
	def anzeigeauswertungzertifikate(self, id):
		data_m = self.database.read_mitarbeiter()
		data_w = self.database.read_weiterbildung()
		data_t = self.database.read_teilnahme()
		return self.view.auswertungZertifikatanzeige(data_m, data_w, data_t, id)

	#----------------------------------------------------------
	# Anmeldung/Storno/Status-Funktionen
	#----------------------------------------------------------

	@cherrypy.expose
	def anmeldungWeiterbildung(self, key_s, key_w):	#key_s = MitarbeiterId, key_w = WeiterbildungsId
		status = "angemeldet"
		data_m = self.database.read_mitarbeiter()
		data_t = self.database.read_teilnahme()
		data_w = self.database.read_weiterbildung()
		data_new = data_m[key_s]
		if status not in data_new:	#entfernt doppelte Statuseinträge
			data_new.append(status)

		self.database.create_teilnahme(data_t, data_new, key_s, key_w)
		status = ""
		return self.view.teilnahmeMitarbeiteranzeige(data_m, data_w, data_t, key_s)

	@cherrypy.expose
	def stornierenWeiterbildung(self, key_s, key_t):	#key_s = MitarbeiterId, key_t = TeilnahmeId
		#status0 = "storniert"
		data_m = self.database.read_mitarbeiter()
		data_t = self.database.read_teilnahme()
		data_w = self.database.read_weiterbildung()
	
		self.database.delete_Teilnahme(key_s, key_t)
		#status0 = ""
		return self.view.teilnahmeMitarbeiteranzeige(data_m, data_w, data_t, key_s)

	@cherrypy.expose
	def abbruchWeiterbildung(self, key_w, key_t):	#key_s = WeiterbildungId, key_t = TeilnahmeId
		status1 = "abgebrochen"
		data_m = self.database.read_mitarbeiter()
		data_t = self.database.read_teilnahme()
		data_w = self.database.read_weiterbildung()
	
		self.database.change_Status(data_t, key_w, key_t, status1)
		status1 = ""
		return self.view.teilnahmeWeiterbildunganzeige(data_m, data_w, data_t, key_w)
		
	@cherrypy.expose
	def statuserfolg(self, key_w, key_t):	#key_w = WeiterbildungsId, key_t = TeilnahmeId
		status2 = "erfolgreich beendet"
		data_m = self.database.read_mitarbeiter()
		data_t = self.database.read_teilnahme()
		data_w = self.database.read_weiterbildung()

		self.database.change_Status(data_t, key_w, key_t, status2)
		status2 = ""
		return self.view.teilnahmeWeiterbildunganzeige(data_m, data_w, data_t, key_w)
		
	@cherrypy.expose
	def statusnichterfolg(self, key_w, key_t):	#key_t = WeiterbildungsId, key_t = TeilnahmeId
		status3 = "nicht erfolgreich beendet"
		data_m = self.database.read_mitarbeiter()
		data_t = self.database.read_teilnahme()
		data_w = self.database.read_weiterbildung()
		
		self.database.change_Status(data_t, key_w, key_t, status3)
		status3 = ""
		return self.view.teilnahmeWeiterbildunganzeige(data_m, data_w, data_t, key_w)

# EOF












