## coding: utf-8

<!DOCTYPE html>
<html>
<head>
   <title>Mitarbeiter-Qualifizierung</title>
   <meta charset="UTF-8" />
   <script type='text/javascript' src='/mitarbeiterquali.js'></script>
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

			<!-- Oben nichts verändern-->
			<!-- Hier wird immer der Inhaltsbereich verändert-->
			<div class="item-main">
				<div id="ueberschrift"> Pflege Weiterbildung </div>
				<table id="overview">
					<tr>
            			<th>Bezeichnung</th><th>Von</th><th>Bis</th><th>Beschreibung</th><th>max. Teilnehmer</th><th>min. Teilnehmer</th><th>Aktion</th>
         			</tr>
					 % for key_s in data_w:
         			<tr>
            			<td>${data_w[key_s][0]}</td>
            			<td>${data_w[key_s][1]}</td>
            			<td>${data_w[key_s][2]}</td>
            			<td>${data_w[key_s][3]}</td>
						<td>${data_w[key_s][4]}</td>
						<td>${data_w[key_s][5]}</td>
            			<td>
               				<a href="/editweiterbildung/${key_s}" id="buttons">bearbeiten</a>                   
               				<a href="/deleteweiterbildung/${key_s}" class="clDelete" id="buttons">löschen</a>
							<a href="/anzeigeweiterbildung/${key_s}" id="buttons">anzeigen</a>
            			</td>
         			</tr>
         			% endfor
				</table>
				<div>
         			<a href="/addweiterbildung" id="erfassen">erfassen</a> 
      			</div>
			</div>
		</div>
	</body>
</html>