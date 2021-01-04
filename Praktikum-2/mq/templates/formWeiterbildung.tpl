## coding: utf-8

<!DOCTYPE html>
<html>
<head>
   <title>Weiterbildung erfassen</title>
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
      <form id="weiterbildungform" action="/saveweiterbildung" method="POST">
         <div id="ueberschrift">Weiterbildung erfassen</div>
         <input type="hidden" value="${key_s}" id="id_spaw" name="id_spaw" />
         <div>
            <label for="bezeichnung_w">Bezeichnung</label>
            <input type="string"
                  value="${data_w[0]}"
                  id="bezeichnung_w"
                  name="bezeichnung_w" required />
         </div>
         <div>
            <label for="von_w">Von</label>
            <input type="date"
                  value="${data_w[1]}"
                  id="von_w"
                  name="von_w" required />
         </div>
         <div>
            <label for="bis_w">Bis</label>
            <input type="date"
                  value="${data_w[2]}"
                  id="bis_w"
                  name="bis_w" required />
         </div>
         <div>
            <label for="beschreibung_w">Beschreibung</label>
            <textarea
                  id="beschreibung_w"
                  name="beschreibung_w" required>${data_w[3]}</textarea>
         </div>
         <div>
            <label for="maxteilnehmer_w">max. Teilnehmer</label>
            <input type="number"
                  value="${data_w[4]}"
                  id="maxteilnehmer_w"
                  name="maxteilnehmer_w" required />
         </div>
         <div>
            <label for="minteilnehmer_w">min. Teilnehmer</label>
            <input type="number"
                  value="${data_w[5]}"
                  id="minteilnehmer_w"
                  name="minteilnehmer_w" required />
         </div>
         <p><br>
         <div id="ueberschrift">Qualifikation erfassen</div>
         <div>
            <label for="bezeichnung_q">Bezeichnung</label>
            <input type="text"
                  value="${data_q[0]}"
                  id="bezeichnung_q"
                  name="bezeichnung_q" required />
         </div>
         <div>
            <label for="beschreibung_q">Beschreibung</label>
            <textarea
                  id="beschreibung_q"
                  name="beschreibung_q" required>${data_q[1]}</textarea>
         </div>
         <p><br>
         <div id="ueberschrift">Zertifikate erfassen</div>
         <div>
            <label for="bezeichnung_z">Bezeichnung</label>
            <input type="text"
                  value="${data_z[0]}"
                  id="bezeichnung_z"
                  name="bezeichnung_z" />
         </div>
         <div>
            <label for="beschreibung_z">Beschreibung</label>
            <textarea
                  id="beschreibung_z"
                  name="beschreibung_z">${data_z[1]}</textarea>
         </div>
         <div>
            <label for="berechtigtzu_z">berechtigt zu</label>
            <input type="text"
                  value="${data_z[2]}"
                  id="berechtigtzu_z"
                  name="berechtigtzu_z" />
         </div>
         <div>
            <input id="buttons" type="submit" value="Speichern"/>
            <a href="/pflegeWeiterbildung" id="buttons"> Zurück </a>
         </div>
         <p><br>
      </form>
   </body>
</html>