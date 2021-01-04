## coding: utf-8

<!DOCTYPE html>
<html>
<head>
   <title>Teilnahme-Mitarbeiter-Anzeige</title>
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
				<div id="ueberschrift">Teilnahme-Mitarbeiter-Anzeige</div>
				<table id="overview">
					<tr>
            			<th>Name </th><th>Vorname</th><th>akademische Grade</th><th>Tätigkeit</th>
         			</tr>
         			<tr>
            			<td>${data_m[key_s][0]}</td>
            			<td>${data_m[key_s][1]}</td>
            			<td>${data_m[key_s][2]}</td>
            			<td>${data_m[key_s][3]}</td>
         			</tr>
				</table>
				<p><br>
				<div id="ueberschrift">Angebot Weiterbildungen</div>
				<table id="overview">
					<tr>
            			<th>Bezeichnung</th><th>Von</th><th>Bis</th><th>Beschreibung</th><th>max. Teilnehmer</th><th>min. Teilnehmer</th><th>Aktion</th>
         			</tr>

					<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

			 		% for key_w in data_w:
			 			% if key_s not in data_t[key_w]:
							<% anfang = data_w[key_w][1] %>
							<% ende = data_w[key_w][2] %>
							%if heute <= anfang:
         						<tr>
            						<td>${data_w[key_w][0]}</td>
            						<td>${data_w[key_w][1]}</td>
            						<td>${data_w[key_w][2]}</td>
            						<td>${data_w[key_w][3]}</td>
									<td>${data_w[key_w][4]}</td>
									<td>${data_w[key_w][5]}</td>
									<td>
										<a href="/anmeldungWeiterbildung/${key_s}/${key_w}" id="buttons">Anmelden</a>
									</td>
         						</tr>
							 %endif
						%endif
					%endfor
				</table>
				<p><br>
				<div id="ueberschrift">abgeschlossene/geplante Weiterbildungen</div>

				<table id="overview">
					<tr>
            			<th>Bezeichnung</th><th>Von</th><th>Bis</th><th>Beschreibung</th><th>max. Teilnehmer</th><th>min. Teilnehmer</th><th>Aktion</th>
         			</tr>
					% for key_t in data_t:
						% if key_s in data_t[key_t]:
         					<tr>
            					<td>${data_w[key_t][0]}</td>
            					<td>${data_w[key_t][1]}</td>
            					<td>${data_w[key_t][2]}</td>
            					<td>${data_w[key_t][3]}</td>
								<td>${data_w[key_t][4]}</td>
								<td>${data_w[key_t][5]}</td>
								<td>
									<a href="/stornierenWeiterbildung/${key_s}/${key_t}" class="clstorno" id="buttons">Stornieren</a>
								</td>
         					</tr>
						%endif
					%endfor
				</table>
				<div>
					<a href="/teilnahmeMitarbeiter" id="buttonzurück"> Zurück </a>
				</div>
			</div>
		</div>
	</body>
</html>