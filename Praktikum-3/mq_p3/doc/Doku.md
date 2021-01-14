## Dokumentation zum dritten WEB-Praktikum
__Datum: 14.01.2021__

__Team:__

- Kai Klaps, Matthias Wiese, Marvin Schlitter

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
Ist für die Verwaltung des Datenverkehrs zuständig

#### Funktionen für Startseite:
Funktion:           Zweck:                                              
------------------- ---------------------------------------------------
init(self)          Legt "database" und "view_o" an
GET()               Daten anfordern
getAllData()        Alle Daten für die Startseite aus Datenbank holen

#### Funktionen für die Mitarbeiter:
Funktion:                    Zweck:                                                               
---------------------------- -----------------------------------------------
GET()                        Daten anfordern
POST()                       Daten neu erstellen
PUT()                        Daten updaten
DELETE()                     Daten löschen
getList_m()                  Alle Mitarbeiterdaten anfordern
getDetail_m()                Daten eines bestimmten Mitarbeiters anfordern
get_mitarbeiter_anzeigen()   Daten auslesen für die Mitarbeiter Anzeige

#### Funktionen für die Weiterbildungen (inkl. Qualifikation, Zertifikat):
Funktion:                     Zweck:                                                                
----------------------------  ----------------------------------------------
GET()                         Daten anfordern
POST()                        Daten neu erstellen
PUT()                         Daten updaten
DELETE()                      Daten löschen
getList_w()                   Alle Weiterbildungsdaten anfordern
getDetail_w()                 Daten einer bestimmten Weiterbildung anfordern
get_weiterbildung_anzeigen()  Daten auslesen für die Weiterbildungs Anzeige

#### Funktionen für die Teilnahme:
Funktion:      Zweck:                                                                                             
-------------- -----------------------------------------------
GET()          Daten anfordern
POST()         Daten neu erstellen
PUT()          Daten updaten
DELETE()       Daten löschen
getList_w()    Alle Weiterbildungsdaten anfordern
getDetail_mt() Daten auslesen für die Teilnahme Mitarbeiter Anzeige
getDetail_wt() Daten auslesen für die Teilnahme Weiterbildung Anzeige

#### Funktionen für die Auswertung (jeweils für Mitarbeiter, Weiterbildung, Zertifikat):
Funktion:               Zweck:                                                                                            
--------------          -----------------------------------------------
GET()                   Daten anfordern
POST()                  Daten neu erstellen
PUT()                   Daten updaten
DELETE()                Daten löschen
getList_auswertung()    Anforderung der Liste aller Daten
getDetail_auswertung()  Anforderung eines Details 

### database.py
Die database.py ist ausschließlich für die Verwaltung der Daten zuständig.

#### Funktionen der Datenbank:

Funktion:                Zweck:                                                                                                  
------------------------ ------------------------------------------------------------
init(self)               Legt die Datensätze an und ließt Sie aus der JSON Datei aus
create_mitarbeiter()     Erstellt einen neuen Mitarbeiter
create_weiterbildung()   Erstellt eine neue Weiterbildung 
create_qualifikation()   Erstellt eine neue Qualifikation
create_zertifikat()      Erstellt ein neues Zertifikat
create_teilnahme()       Erstellt eine neue Teilnahme
create_teilnahmeIDs()    Erstellt eine neue Teilname ID
read_mitarbeiter()       Lädt die Daten data_m
read_weiterbildung()     Lädt die Daten data_w
read_qualifikation()     Lädt die Daten data_q
read_zertifikat()        Lädt die Daten data_z
read_teilnahme()         Lädt die Daten data_t
read_teilnahmeIDs()      Lädt die Daten data_tIDs
update_mitarbeiter()     Aktualisiert die Daten zwischen JSON und data_m
update_weiterbildung()   Aktualisiert die Daten zwischen JSON und data_w
update_qualifikation()   Aktualisiert die Daten zwischen JSON und data_q
update_zertifikat()      Aktualisiert die Daten zwischen JSON und data_z
update_teilnahme()       Aktualisiert die Daten zwischen JSON und data_t
delete_mitarbeiter()     Löscht einen Mitarbeiter
delete_weiterbildung()   Löscht eine Weiterbildung
delete_qualifikation()   Löscht eine Qualifikation
delete_zertifikat()      Löscht ein Zertifikat
delete_teilnahme()       Löscht eine Teilahme
delete_teilnahmeIDs()    Löscht eine Teilnahme ID
readData_mitarbeiter()   Lädt die Daten aus der JSON Datei
readData_weiterbildung() Lädt die Daten aus der JSON Datei
readData_qualifikation() Lädt die Daten aus der JSON Datei
readData_zertifikat()    Lädt die Daten aus der JSON Datei
readData_teilnahme()     Lädt die Daten aus der JSON Datei
readData_teilnahmeIDs()  Lädt die Daten aus der JSON Datei
saveData_mitarbeiter()	 Schreibt die Daten in die JSON Datei
saveData_weiterbildung() Schreibt die Daten in die JSON Datei
saveData_qualifikation() Schreibt die Daten in die JSON Datei
saveData_zertifikate()	 Schreibt die Daten in die JSON Datei
saveData_teilnahme()	    Schreibt die Daten in die JSON Datei            
saveData_teilnahmeIDs()  Schreibt die Daten in die JSON Datei

### view.py
Die View.py ist für die Zusammenstellung von Daten für die verschiedenen Templates zuständig.

#### Funktionen der View:

Funktion:                                    Zweck:                                                                                             
------------------------------------------   -----------------------------------------------
createStartseite()                           Daten für die Startseite zusammenfassen
createList_m()                               Daten von allen Mitarbeitern zusammenfassen
createDetail_m()                             Daten von einem bestimmten Mitarbeiter zusammenfassen
mitarbeiter_anzeigen()                       Daten für die Mitarbeiter Anzeige zusammenfassen
createList_w()                               Daten von allen Weiterbildungen(inkl. Qualifikation, Zertifikat) zusammenfassen
createDetail_w()                             Daten von einer bestimmten Weiterbildungen(inkl. Qualifikation, Zertifikat) zusammenfassen
weiterbildung_anzeigen()                     Daten für die Weiterbildungs Anzeige zusammenfassen
createDetail_t()                             Daten von einer bestimmten Teilnahme zusammenfassen
createList_auswertung_mitarbeiter()          Daten für die Auswertung Mitarbeiter zusammenfassen
createDetail_auswertung_mitarbeiter()        Daten für die Auswertung Mitarbeiter Anzeigen zusammenfassen
createList_auswertung_weiterbildung()        Daten für die Auswertung Qualifikation  zusammenfassen
createDetail_auswertung_weiterbildung()      Daten für die Auswertung Qualifikation Anzeigen zusammenfassen
createList_auswertung_zertifikat()           Daten für die Auswertung Zertifikat zusammenfassen
createDetail_auswertung_zertifikat()         Daten für die Auswertung Zertifikat Anzeigen zusammenfassen

### Datenablage
Die Daten werden in mehreren JSON Dateien abgelegt und aufgerufen.

Datei:               Verantwortlich für:                                                                                                        
-------------------  -----------------------------------------------
mitarbeiter.json     Mitarbeiter Daten
weiterbildung.json   Weiterbildungs Daten
qualifikation.json   Qualfikations Daten
zertifikat.json      Zertifikats Daten
teilnahme.json       Teilnahmen Daten
teilnahmeIDs.json    Speichert die Teilnahme IDs separat

### Konfiguration
```python
   # Method-Dispatcher für die "Startseite" Klasse
   cherrypy.tree.mount(
      application.App_startseite_cl(),
      '/app/startseite/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # Method-Dispatcher für die "Mitarbeiter" Klasse
   cherrypy.tree.mount(
      application.App_mitarbeiter_cl(),
      '/app/mitarbeiter/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # Method-Dispatcher für "Mitarbeiter Anzeigen" Klasse
   cherrypy.tree.mount(
      application.App_mitarbeiter_anzeigen_cl(),
      '/app/mitarbeiterAnzeigen/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # Method-Dispatcher für "Weiterbildung" Klasse
   cherrypy.tree.mount(
      application.App_weiterbildung_cl(),
      '/app/weiterbildung/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # Method-Dispatcher für "Weiterbildung Anzeigen" Klasse
   cherrypy.tree.mount(
      application.App_weiterbildung_anzeigen_cl(),
      '/app/weiterbildungAnzeigen/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # Method-Dispatcher für "Teilnahme" Klasse
   cherrypy.tree.mount(
      application.App_teilnahme_cl(),
      '/app/teilnahme/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )     

   # Method-Dispatcher für "Auswertung Mitarbeiter" Klasse
   cherrypy.tree.mount(
      application.App_auswertung_mitarbeiter_cl(),
      '/app/auswertungMitarbeiter/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # Method-Dispatcher für "Auswertung Weiterbildung" Klasse
   cherrypy.tree.mount(
      application.App_auswertung_weiterbildung_cl(),
      '/app/auswertungWeiterbildung/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # Method-Dispatcher für "Auswertung Zertifikate" Klasse
   cherrypy.tree.mount(
      application.App_auswertung_zertifikat_cl(),
      '/app/auswertungZertifikat/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # Method-Dispatcher für die "Templates" Klasse
   cherrypy.tree.mount(
      template.Template_cl(),
      '/templates',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )
```

```python
# Static config
tools.staticdir.root = cherrypy.Application.currentDir_s
tools.staticdir.on = True
tools.staticdir.dir = './static'
tools.staticdir.index = 'main.html'
```

### Durchführung und Ergebnis der geforderten Prüfung
- Markup Validierung:
	* Beim validieren wurden keine Fehler gefunden

- CSS Validierung:
	* Beim validieren wurden keine Fehler gefunden

- REST Tests:
   * Bei den Tests sind unerwartete Ergebnisse aufgetreten
