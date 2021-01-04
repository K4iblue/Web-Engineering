# -*- coding: utf-8 -*-

<!DOCTYPE html>
<html>
<head>
   <title>Mitarbeiter-Qualifizierung</title>
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
			<div class="item-main">
				<div id="ueberschrift">Zertifikate-Auswertung</div>
				<table id="overview">
					<tr>
            			<th>Bezeichnung</th><th>Beschreibung</th><th>berechtigt zu</th><th>Aktion</th>
         			</tr>
					% for key_z in data_z:
						% if data_z[key_z][0] != "":
         				<tr>
            				<td>${data_z[key_z][0]}</td>
            				<td>${data_z[key_z][1]}</td>
            				<td>${data_z[key_z][2]}</td>
							<td>
								<a href="/anzeigeauswertungzertifikate/${key_z}" id="buttons">anzeigen</a>
            				</td>
         				</tr>
						%endif
					%endfor
				</table>
			</div>

		</div>
	</body>
</html>