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

			<div class="item-main">
				<div id="ueberschrift">Startseite</div>

				<% heute = str(datum.year) + "-" + str(datum.month) + "-" + '0' + str(datum.day) %>

				<!-- Weiterbildungen planend berechnen -->
				<% y = 0 %>
				%for key_s in data_w:
					%if data_w[key_s][0] != "":
						<% anfang = data_w[key_s][1] %>
						<% ende = data_w[key_s][2] %>
						
						%if ( ( int(anfang.split('-')[0]) > int(heute.split('-')[0] ) ) or ( int(anfang.split('-')[0] ) == int(heute.split('-')[0] ) and int(anfang.split('-')[1] ) > int(heute.split('-')[1] ) ) or ( int(anfang.split('-')[0] ) == int(heute.split('-')[0] ) and int(anfang.split('-')[1] ) == int(heute.split('-')[1] ) and int(anfang.split('-')[2] ) > int(heute.split('-')[2] ) ) ):
							<% y = y + 1 %>
						%endif
					%endif
				%endfor

				<!-- Weiterbildungen laufend berechnen -->	
				<% z = 0 %>
				%for key_s in data_w:
					%if data_w[key_s][0] != "":
						<% anfang = data_w[key_s][1] %>
						<% ende = data_w[key_s][2] %>
						%if ( ( ( int(anfang.split('-')[0]) < int(heute.split('-')[0] ) ) or ( int(anfang.split('-')[0] ) == int(heute.split('-')[0] ) and int(anfang.split('-')[1] ) < int(heute.split('-')[1] ) ) or ( int(anfang.split('-')[0] ) == int(heute.split('-')[0] ) and int(anfang.split('-')[1] ) == int(heute.split('-')[1] ) and int(anfang.split('-')[2] ) <= int(heute.split('-')[2] ) ) ) and ( ( int(ende.split('-')[0] ) > int(heute.split('-')[0] ) ) or ( int(ende.split('-')[0] ) == int(heute.split('-')[0] ) and int(ende.split('-')[1] ) > int(heute.split('-')[1] ) ) or ( int(ende.split('-')[0] ) == int(heute.split('-')[0] ) and int(ende.split('-')[1] ) == int(heute.split('-')[1] ) and int(ende.split('-')[2] ) >= int(heute.split('-')[2] ) ) ) ):
							<% z = z + 1 %>
						%endif
					%endif
				%endfor

				<!-- Weiterbildungen abgeschlossen berechnen -->
				<% a = 0 %>
				%for key_s in data_w:
					%if data_w[key_s][0] != "":
						<% anfang = data_w[key_s][1] %>
						<% ende = data_w[key_s][2] %>
						%if ( ( int(ende.split('-')[0] ) < int(heute.split('-')[0] ) ) or ( int(ende.split('-')[0] ) == int(heute.split('-')[0] ) and int(ende.split('-')[1] ) < int(heute.split('-')[1] ) ) or ( int(ende.split('-')[0] ) == int(heute.split('-')[0] ) and int(ende.split('-')[1] ) == int(heute.split('-')[1] ) and int(ende.split('-')[2] ) < int(heute.split('-')[2] ) ) ):
							<% a = a + 1 %>
						%endif
					%endif
				%endfor

				<table id="overview">
					<tr>
						<td>Anzahl Mitarbeiter</td>
						<td>Anzahl Weiterbildungen geplant</td>
						<td>Anzahl Weiterbildungen laufend</td>
						<td>Anzahl Weiterbildungen abgeschlossen</td>
						<td>Anzahl Teilnahmen</td>
					</tr>

					<tr>
						<td>${id_s[0]}</td>
						<td>${y}</td>
						<td>${z}</td>
						<td>${a}</td>
						<td>${id_s[2]}</td>
					</tr>
				</table>

			</div>
		</div>
	</body>
</html>