## coding: utf-8

<!DOCTYPE html>
<html>
<head>
   <title>Mitarbeiter erfassen</title>
   <meta charset="UTF-8" />
   <style> @import "/style.css"; </style>
</head>
<body>
   <div class="container">	
	   <div class="item-header">
			<div> Mitarbeiter-Qualifizierung: </div>
			<div> Version xx / 10.12.2020 </div>
		</div>

		<div class="item-team">
			<div> Gruppe: Kai Klaps, Matthias Wiese, Marvin Schlitter, Tomas Kublickas</div>
		</div>

		<div class="item-startseite">
			<div> <a href="/startseite"> Startseite </a> </div>
		</div>

		<div class="item-pflege">
			<div> Datenpflege: </div>
				<div> <a href="/pflegeMitarbeiter"> Pflege: Mitarbeiterdaten </a> </div>
				<div> <a href="/pflegeWeiterbildung"> Pflege: Weiterbildung </a> </div>
		</div>

		<div class="item-teilnahme">
			<div> Teilnahme: </div>
			<div> <a href="/teilnahmeMitarbeiter"> - Sichtweise: Mitarbeiter </a> </div>
			<div> <a href="/teilnahmeWeiterbildung"> - Sichtweise: Weiterbildung </a> </div>				
		</div>

		<div class="item-auswertung">
			<div> Auswertung: </div>
			<div> <a href="/auswertungMitarbeiter"> - Mitarbeiter </a> </div>
			<div> <a href="/auswertungWeiterbildung"> - Weiterbildung </a> </div>
			<div> <a href="/auswertungZertifikate"> - Zertifikate </a> </div>
		</div>
      <form id="mitarbeiterform" action="/savemitarbeiter" method="POST">
         <div id="ueberschrift">Mitarbeiter erfassen</div>
         <input type="hidden" value="${key_s}" id="id_spam" name="id_spam" />
         <div>
            <label for="namemitarbeiter">Name</label>
            <input type="string"
                  value="${data_m[0]}"
                  id="namemitarbeiter"
                  name="namemitarbeiter" required />
         </div>
         <div>
            <label for="vornamemitarbeiter">Vorname</label>
            <input type="string"
                  value="${data_m[1]}"
                  id="vornamemitarbeiter"
                  name="vornamemitarbeiter" required />
         </div>
         <div>
            <label for="akagrad">akademische Grade</label>
            <input type="string"
                  value="${data_m[2]}"
                  id="akagrad"
                  name="akagrad" required />
         </div>
         <div>
            <label for="taetigkeit">Tätigkeit</label>
            <input type="string"
                  value="${data_m[3]}"
                  id="taetigkeit"
                  name="taetigkeit" required />
         </div>
         <div>
            <input id="buttons" type="submit" value="Speichern"/>
            <a href="/pflegeMitarbeiter" id="buttons"> Zurück </a>
         </div>
      </form>
   </div>
</body>
</html>