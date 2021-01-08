## Dokumentation zum zweiten WEB-Praktikum
__Datum: 10.12.2020__

__Team:__

- Kai Klaps, Matthias Wiese

- Marvin Schlitter, Tomas Kublickas

## Allgemeine Beschreibung

### Aufgabe der Anwendung
Die Webanwendung Mitarbeiterqualifizierung (MQ) hat die Aufgabe Qualifikationen und Zertifikate zu verwalten. Zu dem können Weiterbildungen von Mitarbeiter gebucht oder stoniert werden. Außerdem besteht die Möglichkeit, eine Auswertung der Mitarbeiter oder Weiterbildungen zu erhalten.

### Übersicht der fachlichen Funktionen
* Verwaltung der Mitarbeiter
* Verwaltung der Weiterbildungen (inkl. Qualifikationen und Zertifikate)
* Mitarbeiter können an Weiterbildungen teilnehmen bzw. die Teilnahme stonieren
* Mitarbeiter und Weiterbildungen können ausgewertet werden

## Beschreibung der Komponenten des Servers

### server.py

Hierbei handelt es sich um das eigentliche, zu startende Program des Servers.

### application.py

#### Allgemeine Funktionen:
Funktion            Zweck                                              
------------------- ---------------------------------------------------
init(self)          Welche die Datenbanken, den Pfad und view_o anlegt 
index(self)         Führt die startseite(self) aus                   
default(...)        Meldet sich bei der Fehlermeldung 404              
startseite(self)  	Ruft die Hauptseite auf 

#### Funktionen für die Pflege der Mitarbeiter:
Funktion                             Zweck                                                               
------------------------------------ --------------------------------------------------------------------
pflegeMitarbeiter(self)	             Erzeugt eine Liste in der view_o
addmitarbeiter(self)				 Erzeugt ein leeres Formular zum Erfassen eines Datensatzes                                    
editmitarbeiter(...)				 Erzeugt ein Formular in der view_o                                  
savemitarbeiter(...)   				 Speichert die Daten der Mitarbeiter                                 
anzeigemitarbeiter(...)		         Zeigt eine Detailansicht                                            
deletemitarbeiter(...)               Entfernt den Eintrag des Mitarbeiters und zeigt die Liste erneut an 

#### Funktionen für die Pflege der Weiterbildungen:
Funktion                                Zweck                                                                
--------------------------------------- ---------------------------------------------------------------------
pflegeWeiterbildung(self)               Erzeugt eine Liste in der view_o
addweiterbildung(...)                   Erzeugt ein leeres Formular zum Erfassen eines Datensatzes               
editweiterbildung(...)   				Erzeugt ein Formular in der view_o                                   
saveweiterbildung()...)    				Speichert die Daten der Weiterbildungen, Qualifikation und Zertifikate                              
anzeigeweiterbildung(...)     			Zeigt eine Detailansicht                                             
deleteweiterbildung(...)                Entfernt den Eintrag der Weiterbildung und zeigt die Liste erneut an 

#### Funktionen für die Teilnahme (Mitarbeiter):
Funktion                                  Zweck                                                                                             
----------------------------------------- --------------------------------------------------------------------------------------------------
teilnahmeMitarbeiter(self)             	  Erzeugt eine Liste in der view_o                                                                  
teilnahmeMitarbeiteranzeige(...)  		  Erzeugt die Anzeige des Mitarbeiters und eine weitere Liste für die Weiterbildungen in der view_o 
anmeldungWeiterbildung(...)    			  Ermöglicht es an einer Weiterbildung teilzunehmen                                                 
stornierenWeiterbildung                   Storniert die Anmeldung zur Weiterbildung                                                         

#### Funktionen für die Teilnahme (Weiterbildung):
Funktion                                   Zweck                                                      
------------------------------------------ -----------------------------------------------------------
teilnahmeWeiterbildung(self)               Erzeugt zwei Liste in der view_o                           
teilnahmeWeiterbildunganzeige(...)         Zeigt in einer Tabelle die Teilnehmer der Weiterbildung an 
statuserfolg(...)                          Verändert den Status in der Tabelle Teilnahme
statusnichterfolg(...)                     Verändert den Status in der Tabelle Teilnahme              
abbruchWeiterbildung                       Storniert die Anmeldung zur Weiterbildung                  

#### Funktionen für die Auswertung:
Funktion                              Zweck                                                        
------------------------------------- --------------------------------------------------------------
auswertungMitarbeiter(self)           Erzeugt eine Liste in der view_o                             
anzeigeauswertungmitarbeiter(...)     Erzeugt eine Liste und Angaben zum Mitarbeiter in der view_o 
auswertungWeiterbildung(self)         Erzeugt eine Liste in der view_o                             
anzeigeauswertungweiterbildung(...)   Erzeugt eine Liste und Angaben zur Weiterbildung in der view_o
auswertungZertifikate(self)           Erzeugt eine Liste in der view_o                             
anzeigeauswertungzertifikate		  Erzeugt eine Liste und Angaben zu Zertifikaten in der view_o

### view.py

Hier werden die verschiedenen HTML Seiten mithilfe von Mako gerendert und an den Client gesendet.

### database.py

Die Datenbanken sind ausschließlich für die Verwaltung der jeweiligen Daten zuständig.

- Jeweilige Datenbank Klasse für:
	- Mitarbeiter
	- Qualifikationen
	- Teilnahme
	- Weiterbildung
	- Zertifikate

#### Die Datenbanken verfügen alle über die folgenden Funktionen:

Funktion                 Zweck                                                                                                  
------------------------ ----------------------------------
init(self)               Legt die Datensätze an und ließt Sie aus der JSON Datei aus
read_mitarbeiter()       Lädt die Daten data_m
read_weiterbildung()     Lädt die Daten data_w
read_qualifikation()     Lädt die Daten data_q                                         
read_zertifikate()       Lädt die Daten data_z
read_teilnahme()         Lädt die Daten data_t
readData_mitarbeiter()   Lädt die Daten aus der JSON Datei
readData_weiterbildung() Lädt die Daten aus der JSON Datei
readData_qualifikation() Lädt die Daten aus der JSON Datei                                         
readData_zertifikate()   Lädt die Daten aus der JSON Datei
readData_teilnahme()     Lädt die Daten aus der JSON Datei
saveData_mitarbeiter()	 Schreibt die Daten in die JSON Datei
saveData_weiterbildung() Schreibt die Daten in die JSON Datei
saveData_qualifikation() Schreibt die Daten in die JSON Datei
saveData_zertifikate()	 Schreibt die Daten in die JSON Datei
saveData_teilnahme()	 Schreibt die Daten in die JSON Datei                                                                                                     
getDefault_m()           Gibt eine Anzahl von default Werten zurück
getDefault_w()           Gibt eine Anzahl von default Werten zurück
getDefault_q()           Gibt eine Anzahl von default Werten zurück
getDefault_z()           Gibt eine Anzahl von default Werten zurück
getDefault_t()           Gibt eine Anzahl von default Werten zurück
update_mitarbeiter       Aktualisiert die Daten zwischen JSON und data_m
update_weiterbildung     Aktualisiert die Daten zwischen JSON und data_w
update_qualifikation     Aktualisiert die Daten zwischen JSON und data_q
update_zertifikate       Aktualisiert die Daten zwischen JSON und data_z
update_teilnahme         Aktualisiert die Daten zwischen JSON und data_t
create_mitarbeiter()     Liest die ID aus maxID von dataid.py aus und nimmt die nächsthöhere ID zum Eintragen der Daten
create_weiterbildung()   Liest die ID aus maxID von dataid.py aus und nimmt die nächsthöhere ID zum Eintragen der Daten
create_qualifikation()   Liest die ID aus maxID von dataid.py aus und nimmt die nächsthöhere ID zum Eintragen der Daten (gehört zu weiterbildung)
create_zertifikate()     Liest die ID aus maxID von dataid.py aus und nimmt die nächsthöhere ID zum Eintragen der Daten (gehört zu weiterbildung)
create_teilnahme()       Liest die ID aus maxID von dataid.py aus und nimmt die nächsthöhere ID zum Eintragen der Daten
delete_mitarbeiter()     Übergebene daten werden gelöscht
delete_weiterbildung()   Übergebene daten werden gelöscht
delete_qualifikation()   Übergebene daten werden gelöscht
delete_zertifikate()     Übergebene daten werden gelöscht
delete_teilnahme()       Übergebene daten werden gelöscht
change_Status()			 Ändert den Status von Mitarbeiter und Weiterbildung

### dataid.py

Hier werden die maxID´s von Mitarbeiter, Weiterbildungen und Teilnahmen abgespeichert.

### Datenablage
Die Daten werden in mehreren JSON Dateien abgelegt und aufgerufen.

* mitarbeiter.json
* weiterbildung.json
* teilnahme.json
* qualifikationen.json
* zertifikat.json
* maxidMitarbeiter.json
* maxidWeiterbildung.json
* maxidTeilnahmen.json

### Konfiguration
```python
// Static content config
static_config = {
		'/': {
			'tools.staticdir.root': current_dir,
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './content'
		}
	}
```

### Durchführung und Ergebnis der geforderten Prüfung
- Markup Validierung:
	* Alle Seiten werden angezeigt wie geplant
	* Beim validieren wurden ein paar Warnungen angezeigt
	* diese entstehen durch das mehrfache verwenden von der selben ID

- CSS Validierung:
	* style.css -> Fehlerfrei
