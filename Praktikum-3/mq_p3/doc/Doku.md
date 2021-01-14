## Dokumentation zum dritten WEB-Praktikum
__Datum: 14.01.2021__

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
Ist für die Verwaltung des Datenverkehrs zuständig

#### Allgemeine Funktionen:
Funktion     Zweck                                              
------------ --------------------------------
init(self)   Legt "database" und "view_o" an

#### Funktionen für die Mitarbeiter:
Funktion       Zweck                                                               
-------------- -----------------------------------------------
GET()          Daten anfordern
POST()         Daten neu erstellen
PUT()          Daten updaten
DELETE()       Daten löschen
getList_m()    Alle Mitarbeiterdaten anfordern
getDetail_m()  Daten eines bestimmten Mitarbeiters anfordern

#### Funktionen für die Pflege der Weiterbildungen (inkl. Qualifikation, Zertifikat):
Funktion       Zweck                                                                
-------------- -----------------------------------------------
GET()          Daten anfordern
POST()         Daten neu erstellen
PUT()          Daten updaten
DELETE()       Daten löschen
getList_w()    Alle Weiterbildungsdaten anfordern
getDetail_w()  Daten einer bestimmten Weiterbildung anfordern

#### Funktionen für die Teilnahme:
Funktion       Zweck                                                                                             
-------------- -----------------------------------------------
GET()          Daten anfordern
POST()         Daten neu erstellen
PUT()          Daten updaten
DELETE()       Daten löschen

#### Funktionen für die Auswertung (jeweils für Mitarbeiter, Weiterbildung, Zertifikat):
Funktion                Zweck                                                                                             
--------------          -----------------------------------------------
GET()                   Daten anfordern
POST()                  Daten neu erstellen
PUT()                   Daten updaten
DELETE()                Daten löschen
getList_auswertung()    Anforderung der Liste aller Daten
getDetail_auswertung()  Anforderung eines Details 

### database.py
Die Datenbank ist ausschließlich für die Verwaltung der Daten zuständig.

#### Funktionen der Datenbank:

Funktion                 Zweck                                                                                                  
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

### Datenablage
Die Daten werden in mehreren JSON Dateien abgelegt und aufgerufen.
* mitarbeiter.json
* weiterbildung.json
* qualifikation.json
* zertifikat.json
* teilnahme.json
* teilnahmeIDs.json

### Konfiguration
```python
   # Method-Dispatcher für "Mitarbeiter"
   cherrypy.tree.mount(
      application.App_mitarbeiter_cl(),
      '/app/mitarbeiter/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # Method-Dispatcher für "Weiterbildung"
   cherrypy.tree.mount(
      application.App_weiterbildung_cl(),
      '/app/weiterbildung/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )       

   # Method-Dispatcher für "Auswertung"
   cherrypy.tree.mount(
      application.App_auswertung_cl(),
      '/app/auswertung/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # Eintrag: Method-Dispatcher für "Auswertung Zertifikate"
   cherrypy.tree.mount(
      application.App_auswertung_zertifikat_cl(),
      '/app/auswertungZertifikat/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # Method-Dispatcher für "Templates"
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
