## -*- coding: utf-8 -*-
<!DOCTYPE html>
<html id="overview">

<head>
	<title>Mitarbeiter-Qualifizierung</title>
	<meta charset="UTF-8" />
	<style> @import "/style.css"; </style>
	<script type="text/javascript" src="/mitarbeiterquali.js"></script>
</head>

<body>
	<div class="container">
		<div class="item-header">
			<div> Mitarbeiter-Qualifizierung: </div>
			<div> Version 1.0 / 10.12.2020 </div>
		</div>

		<div class="item-team">
			<div> Gruppe: Kai Klaps, Matthias Wiese, Marvin Schlitter, Tomas Kublickas</div>
		</div>

		<div class="item-startseite">
			<div> <a href="/hauptseite_p"> Startseite </a> </div>
		</div>

		<div class="item-pflege">
			<div> Datenpflege </div>
				<div> <a href="/pflegemitarbeiter_p"> - Pflege: Mitarbeiter </a> </div>
				<div> <a href="/pflegeweiterbildung_p"> - Pflege: Weiterbildung </a> </div>
		</div>

		<div class="item-teilnahme">
			<div> Teilnahme </div>
			<div> <a href="/sichtweisemitarbeiter_p"> - Sichtweise: Mitarbeiter </a> </div>
			<div> <a href="/sichtweiseweiterbildungen_p"> - Sichtweise: Weiterbildung </a> </div>				
		</div>

		<div class="item-auswertung">
			<div> Auswertung </div>
			<div> <a href="/auswertung_mitarbeiter_p"> - Mitarbeiter </a> </div>
			<div> <a href="/auswertung_weiterbildungen_p"> - Weiterbildung </a> </div>
			<div> <a href="/auswertung_zertifikat_p"> - Zertifikate </a> </div>
		</div>
		
		<!-- Oben nichts verändern -->
		<!-- Hier wird immer der Inhaltsbereich verändert -->
		<div class="item-main">

			<h3> Weiterbildung: ${data_o[1][id_str][0]}</h3>
			<div>
				<p>vom ${data_o[1][id_str][1]} bis zum ${data_o[1][id_str][2]}</p>
				<p>min. Anzahl: ${data_o[1][id_str][5]} </p>
				<p>max. Anzahl: ${data_o[1][id_str][4]}</p>
			</div>


			<h3>Teilnehmer</h3>
					<table>
						<tr>
							<th>ID</th>
							<th>Name</th>
							<th>Vorname</th>
							<th>Akademischer Grad</th>
							<th>Tätigkeit</th>
						</tr>
			
			
						%for key_s in data_o[2]:
							%if data_o[2][key_s][0] is id_str:
								<% MitarbeiterID = data_o[2][key_s][1] %>
			
						<tr>
							<td>${key_s}</td>
							<td>${data_o[0][MitarbeiterID][0]}</td>
							<td>${data_o[0][MitarbeiterID][1]}</td>
							<td>${data_o[0][MitarbeiterID][2]}</td>
							<td>${data_o[0][MitarbeiterID][3]}</td> 
						</tr>
							%endif
						%endfor
					</table>

			<div>
				<a id="hauptseite" href="/sichtweiseweiterbildungen_p">
					<input type="submit" value="zurueck" id="buttons">
				</a>
			</div>

		</div>
	</div>
</body>
</html>