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
		<h3>Aktuelle & Abgeschlossene Weiterbildungen</h3>
			<table>
				<tr>
					<th>ID</th>
					<th>Bezeichnung</th>
					<th>Von</th>
					<th>Bis</th>
					<th>Max. Teilnehmer</th>
					<th>Min. Teilnehmer</th>
					<th>Status</th>
					<th>Aktion</th>
				</tr>

				<% datum = data_o[1] %>
				<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>
				<% i = 0 %>
				%for key_s in data_o[0]:
					%if data_o[0][key_s][0] != "":
						<% anfang = data_o[0][key_s][1] %>
						<% ende = data_o[0][key_s][2] %>
							%if anfang < heute:
								<% i = i + 1%>
				
								%if ende < heute:
									<% status = "abgeschlossen"%>
								%else:
									<% status = "läuft"%>
								%endif

				<tr>
					<td>${key_s}</td>
					<td>${data_o[0][key_s][0]}</td>
					<td>${data_o[0][key_s][1]}</td>
					<td>${data_o[0][key_s][2]}</td>
					<td>${data_o[0][key_s][4]}</td>
					<td>${data_o[0][key_s][5]}</td>
					<td>${status}</td>
					<td>
						<a href="/sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_p/${key_s}" id="buttons">Information</a> 
				 </td>
				</tr>
							
						%endif
					%endif
				%endfor
			</table>


		<hr>
		<h3>Geplante Weiterbildungen</h3>
			<table>
				<tr>
					<th>ID</th>
					<th>Bezeichnung</th>
					<th>Von</th>
					<th>Bis</th>
					<th>Max. Teilnehmer</th>
					<th>Min. Teilnehmer</th>
					<th>Aktion</th>
				</tr>

				<% i = 0 %>
				<% datum = data_o[1] %>
				<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

				%for key_s in data_o[0]:
					%if data_o[0][key_s][0] != "":
						<% anfang = data_o[0][key_s][1] %>
						%if anfang > heute:
							<% i = i + 1 %>

				<tr>
					<td>${key_s}</td>
					<td>${data_o[0][key_s][0]}</td>
					<td>${data_o[0][key_s][1]}</td>
					<td>${data_o[0][key_s][2]}</td>
					<td>${data_o[0][key_s][4]}</td>
					<td>${data_o[0][key_s][5]}</td>
					<td>
						<a href="/sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_p/${key_s}" id="buttons">Information</a> 
				 </td>
				</tr>
							%endif
						%endif
					%endfor
			</table>
		</div>
	</div>
</body>
</html>