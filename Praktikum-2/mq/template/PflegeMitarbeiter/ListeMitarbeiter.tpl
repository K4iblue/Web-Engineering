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
		
		<!-- Oben nichts verändern-->
		<!-- Hier wird immer der Inhaltsbereich verändert-->
	<div class="item-main">
		<h3>Pflege der Mitarbeiterdaten</h3>
			<table>
				<tr>
					<th>ID</th>
					<th>Name</th>
					<th>Vorname</th>
					<th>Akademischer Grad</th>
					<th>Tätigkeit</th>
					<th>Aktion</th>
				</tr>
				
				<% i = 0 %>
				%for key_s in data_o:
					%if data_o[key_s][0] != "":
						<% i = i + 1 %>
			
				<tr>
					<td>${key_s}</td>
					<td>${data_o[key_s][0]}</td>
					<td>${data_o[key_s][1]}</td>
					<td>${data_o[key_s][2]}</td>
					<td>${data_o[key_s][3]}</td>
					<td>
						<a href="/pflegemitarbeiter_anzeigen_p/${key_s}" id="buttons">anzeigen</a> 
						<a href="/pflegemitarbeiter_bearbeiten_p/${key_s}" id="buttons">bearbeiten</a>                   
						<a href="/deletemitarbeiter_p/${key_s}" class="clDelete" id="buttons">löschen</a> 
				 </td>
				</tr>
					%endif
				%endfor
			</table>

			<div>
				<a href="/pflegemitarbeiter_bearbeiten_p">
				<input type="submit" value="erfassen" id="buttons">
				</a>
			</div>
	</div>
</body>
</html>