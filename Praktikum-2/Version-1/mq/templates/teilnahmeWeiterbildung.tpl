## coding: utf-8

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

			<!-- Oben nichts verändern-->
			<!-- Hier wird immer der Inhaltsbereich verändert-->
			<div class="item-main">
				<div id="ueberschrift">Teilnahme Weiterbildung</div>
				<p><br>
				<div id="ueberschrift">Abgeschlossene/Laufende Weiterbildungen</div>
				<table id="overview">
					<tr>
            			<th>Bezeichnung</th><th>Von</th><th>Bis</th><th>Beschreibung</th><th>max. Teilnehmer</th><th>min. Teilnehmer</th><th>Status</th><th>Aktion</th>
         			</tr>

					<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

					% for key_w in data_w:

						<% anfang = data_w[key_w][1] %>
						<% ende = data_w[key_w][2] %>
						%if anfang <= heute:
				
							%if ende < heute:
								<% status = "abgeschlossen" %>
							%else:
								<% status = "laufend" %>
							%endif
         					<tr>
            					<td>${data_w[key_w][0]}</td>
            					<td>${data_w[key_w][1]}</td>
            					<td>${data_w[key_w][2]}</td>
            					<td>${data_w[key_w][3]}</td>
								<td>${data_w[key_w][4]}</td>
								<td>${data_w[key_w][5]}</td>
								<td>${status}</td>
            					<td>
									<a href="/teilnahmeWeiterbildunganzeige/${key_w}" id="buttons">anzeigen</a>
            					</td>
         					</tr>
					 	%endif
         			% endfor
				</table>
				<p><br>
				<div id="ueberschrift">Geplante Weiterbildungen</div>
				<table id="overview">
					<tr>
            			<th>Bezeichnung</th><th>Von</th><th>Bis</th><th>Beschreibung</th><th>max. Teilnehmer</th><th>min. Teilnehmer</th><th>Aktion</th>
         			</tr>

					<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

					% for key_w in data_w:
						<% anfang = data_w[key_w][1] %>
						%if anfang > heute:
         					<tr>
            					<td>${data_w[key_w][0]}</td>
            					<td>${data_w[key_w][1]}</td>
            					<td>${data_w[key_w][2]}</td>
            					<td>${data_w[key_w][3]}</td>
								<td>${data_w[key_w][4]}</td>
								<td>${data_w[key_w][5]}</td>
            					<td>
									<a href="/teilnahmeWeiterbildunganzeige/${key_w}" id="buttons">anzeigen</a>
            					</td>
         					</tr>
					 	%endif
         			%endfor
				</table>
			</div>
		</div>
	</body>
</html>