## coding: utf-8

<!DOCTYPE html>
<html>
<head>
   <title>Teilnahme-Weiterbildung-Anzeige</title>
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
			<div class="item-main">
			<div id="ueberschrift">Teilnahme-Weiterbildung-Anzeige</div>
			<table id="overview">
				<tr>
            		<th>Bezeichnung</th><th>Von</th><th>Bis</th><th>Beschreibung</th><th>max. Teilnehmer</th><th>min. Teilnehmer</th>
         		</tr>
         		<tr>
            		<td>${data_w[key_w][0]}</td>
            		<td>${data_w[key_w][1]}</td>
            		<td>${data_w[key_w][2]}</td>
            		<td>${data_w[key_w][3]}</td>
					<td>${data_w[key_w][4]}</td>
					<td>${data_w[key_w][5]}</td>
         		</tr>
			</table>
			<p><br>
			<div id="ueberschrift">Teilnehmer</div>
			<table id="overview">
				<tr>
            		<th>Name</th><th>Vorname</th><th>akademische Grade</th><th>Tätigkeit</th><th>Status</th><th>Aktion</th>
         		</tr>

				<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

				% for key_t in data_t[key_w]:
         			<tr>
            			<td>${data_t[key_w][key_t][0]}</td>
            			<td>${data_t[key_w][key_t][1]}</td>
            			<td>${data_t[key_w][key_t][2]}</td>
            			<td>${data_t[key_w][key_t][3]}</td>
						<td>${data_t[key_w][key_t][4]}</td>
						<td>
							<% anfang = data_w[key_w][1] %>
							<% ende = data_w[key_w][2] %>

							%if heute > ende:
								<a href="/statuserfolg/${key_w}/${key_t}" id="buttons">Erfolg</a> <a href="/statusnichterfolg/${key_w}/${key_t}" id="buttons">Nichterfolg</a>
							%else:
								<a href="/abbruchWeiterbildung/${key_w}/${key_t}" id="buttons">abbrechen</a>
							%endif
						</td>
         			</tr>
				%endfor
			</table>
			<div>
				<a href="/teilnahmeWeiterbildung" id="buttonzurück"> Zurück </a>
			</div>
		</div>
	</body>
</html>