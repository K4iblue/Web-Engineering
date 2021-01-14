# coding:utf-8

# Demonstrator es/te/tm

import sys
import os.path
import cherrypy

from app import application, template

#----------------------------------------------------------
def main():
#----------------------------------------------------------

   # aktuelles Verzeichnis ermitteln, damit es in der Konfigurationsdatei als
   # Bezugspunkt verwendet werden kann
   try:                                    # aktuelles Verzeichnis als absoluter Pfad
      currentDir_s = os.path.dirname(os.path.abspath(__file__))
   except:
      currentDir_s = os.path.dirname(os.path.abspath(sys.executable))
   cherrypy.Application.currentDir_s = currentDir_s

   configFileName_s = os.path.join(currentDir_s, 'server.conf') # im aktuellen Verzeichnis
   if os.path.exists(configFileName_s) == False:
      # Datei gibt es nicht
      configFileName_s = None

   # autoreload-Monitor hier abschalten
   cherrypy.engine.autoreload.unsubscribe()

   # 1. Eintrag: Standardverhalten, Berücksichtigung der Konfigurationsangaben im configFile
   cherrypy.tree.mount(
      None, '/', configFileName_s
   )

   # 2. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   """
   cherrypy.tree.mount(
      application.Application_cl(),
      '/app',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )
   """

   # 2. Eintrag: Method-Dispatcher für die "Applikation Mitarbeiter" "app/mitarbeiter/" vereinbaren
   cherrypy.tree.mount(
      application.App_mitarbeiter_cl(),
      '/app/mitarbeiter/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # 2. Eintrag: Method-Dispatcher für "Weiterbildung"
   cherrypy.tree.mount(
      application.App_weiterbildung_cl(),
      '/app/weiterbildung/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # 2. Eintrag: Method-Dispatcher für "Weiterbildung Anzeigen"
   cherrypy.tree.mount(
      application.App_weiterbildung_anzeigen_cl(),
      '/app/weiterbildungAnzeigen/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # 2. Eintrag: Method-Dispatcher für "Teilnahme"
   cherrypy.tree.mount(
      application.App_teilnahme_cl(),
      '/app/teilnahme/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )     

   # 2. Eintrag: Method-Dispatcher für "Auswertung Mitarbeiter"
   cherrypy.tree.mount(
      application.App_auswertung_mitarbeiter_cl(),
      '/app/auswertungMitarbeiter/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # 2. Eintrag: Method-Dispatcher für "Auswertung Weiterbildung"
   cherrypy.tree.mount(
      application.App_auswertung_weiterbildung_cl(),
      '/app/auswertungWeiterbildung/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # 2. Eintrag: Method-Dispatcher für "Auswertung Zertifikate"
   cherrypy.tree.mount(
      application.App_auswertung_zertifikat_cl(),
      '/app/auswertungZertifikat/',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   ) 

   # 2. Eintrag: Method-Dispatcher für die "Applikation" "templates" vereinbaren
   cherrypy.tree.mount(
      template.Template_cl(),
      '/templates',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.engine.start()
   cherrypy.engine.block()

#----------------------------------------------------------
if __name__ == '__main__':
#----------------------------------------------------------
   main()