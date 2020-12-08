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
index(self)         Führt die hauptseite_p(self) aus                   
default(...)        Meldet sich bei der Fehlermeldung 404              
hauptseite_p(self)  Ruft die Hauptseite auf 

#### Funktionen für die Pflege der Mitarbeiter:
Funktion                             Zweck                                                               
------------------------------------ --------------------------------------------------------------------
pflegemitarbeiter_p(self)            Erzeugt eine Liste in der view_o                                    
pflegemitarbeiter_bearbeiten_p(...)  Erzeugt ein Formular in der view_o                                  
pflegemitarbeiter_speichern_p(...)   Speichert die Daten der Mitarbeiter                                 
pflegemitarbeiter_anzeigen_p         Zeigt eine Detailansicht                                            
deletemitarbeiter(...)               Entfernt den Eintrag des Mitarbeiters und zeigt die Liste erneut an 

#### Funktionen für die Pflege der Weiterbildungen:
Funktion                                Zweck                                                                
--------------------------------------- ---------------------------------------------------------------------
pflegeweiterbildung_p(self)             Erzeugt eine Liste in der view_o                                     
pflegeweiterbildung_bearbeiten_p(...)   Erzeugt ein Formular in der view_o                                   
pflegeweiterbildung_speichern_p(...)    Speichert die Daten der Weiterbildungen                              
pflegeweiterbildung_anzeigen_p(...)     Zeigt eine Detailansicht                                             
deleteweiterbildung(...)                Entfernt den Eintrag der Weiterbildung und zeigt die Liste erneut an 
pflegeweiterbildung_q_speichern_p(...)  Speichert die Daten der Qualifikationen                              
pflegeweiterbildung_z_speichern_p(...)  Speichert die Daten der Zertifikate                                  

#### Funktionen für die Teilnahme (Mitarbeiter):
Funktion                                  Zweck                                                                                             
----------------------------------------- --------------------------------------------------------------------------------------------------
sichtweisemitarbeiter_p(self)             Erzeugt eine Liste in der view_o                                                                  
sichtweisemitarbeiter_information_p(...)  Erzeugt die Anzeige des Mitarbeiters und eine weitere Liste für die Weiterbildungen in der view_o 
sichtweisemitarbeiter_eintragen_p(...)    Ermöglicht es an einer Weiterbildung teilzunehmen                                                 
deleteteilnahme_p(...)                    Storniert die Anmeldung zur Weiterbildung                                                         

#### Funktionen für die Teilnahme (Weiterbildung):
Funktion                                                      Zweck                                                      
------------------------------------------------------------- -----------------------------------------------------------
sichtweiseweiterbildungen_p(self)                             Erzeugt zwei Liste in der view_o                           
sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_p(...)  Zeigt in einer Tabelle die Teilnehmer der Weiterbildung an 
sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_p(...)     Zeigt in einer Tabelle die Teilnehmer der Weiterbildung an 
sichtweiseweiterbildungen_Status_p(...)                       Verändert den Status in der Tabelle Teilnahme              
deleteteilnahme2_p(...)                                       Storniert die Anmeldung zur Weiterbildung                  

#### Funktionen für die Auswertung:
Funktion                              Zweck                                                        
------------------------------------- --------------------------------------------------------------
auswertung_mitarbeiter_p(self)        Erzeugt eine Liste in der view_o                             
auswertung_mitarbeiter_Info_p(...)    Erzeugt eine Liste und Angaben zum Mitarbeiter in der view_o 
auswertung_weiterbildungen_p(self)    Erzeugt eine Liste in der view_o                             
auswertung_weiterbildung_Info_p(...)  Erzeugt ein Liste und Angaben zur Weiterbildung in der view_o
auswertung_zertifikat_p(self)         Erzeugt eine Liste in der view_o                             

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
Funktion          Zweck                                                                                                  
----------------- -------------------------------------------------------------------------------------------------------
init(self)        Legt die Datensätze an und ließt Sie aus der JSON Datei aus                                            
read_px()         Lädt die Daten data_o                                                                                  
readData_p(self)  Lädt die Daten aus der JSON Datei                                                                      
saveData_p(self)  Schreibt die Daten in die JSON Datei                                                                   
getDefault_px()   Gibt eine Anzahl von default Werten zurück                                                             
update_px()       Aktualisiert die Daten zwischen JSON und data_o                                                        
create_px()       Durch eine Schleife wird ein freier Platz in der Liste gesucht,  die erste freie ID wird zurückgegeben 
delete_px()       Alte Daten werden mit default Werten überschrieben                                                     

### Datenablage
Die Daten werden in mehreren JSON Dateien abgelegt und aufgerufen.

* Mitarbeiter.json
* Weiterbildung.json
* Teilnahme.json
* Qualifikationen.json
* Zertifikat.json

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
	* Beim validieren wurden ein paar Warnung angezeigt
	* diese entstehen durch das anhängen der .tpl Dateien.


- CSS Validierung:
	* header.css -> Fehlerfrei
	* sidebar.css -> Fehlerfrei
	* webteams.css -> Fehlerfrei