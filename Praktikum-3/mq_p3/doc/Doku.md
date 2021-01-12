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

#### Allgemeine Funktionen:
Funktion            Zweck                                              
------------------- ---------------------------------------------------
init(self)          Welche die Datenbanken, den Pfad und view_o anlegt 


#### Funktionen für die Pflege der Mitarbeiter:
Funktion                             Zweck                                                               
------------------------------------ --------------------------------------------------------------------


#### Funktionen für die Pflege der Weiterbildungen:
Funktion                                Zweck                                                                
--------------------------------------- ---------------------------------------------------------------------


#### Funktionen für die Teilnahme:
Funktion                                  Zweck                                                                                             
----------------------------------------- --------------------------------------------------------------------------------------------------
                

#### Funktionen für die Auswertung:
Funktion                              Zweck                                                        
------------------------------------- --------------------------------------------------------------


### database.py
Die Datenbank ist ausschließlich für die Verwaltung der Daten zuständig.

#### Funktionen der Datenbank:

Funktion                 Zweck                                                                                                  
------------------------ ----------------------------------
init(self)               Legt die Datensätze an und ließt Sie aus der JSON Datei aus


### Datenablage
Die Daten werden in mehreren JSON Dateien abgelegt und aufgerufen.

* mitarbeiter.json
* weiterbildung.json
* teilnahme.json
* qualifikationen.json
* zertifikat.json

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
