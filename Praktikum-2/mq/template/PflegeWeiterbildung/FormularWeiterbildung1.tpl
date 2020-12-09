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
			<div> Datenpflege: </div>
				<div> <a href="/pflegemitarbeiter_p"> Pflege: Mitarbeiterdaten </a> </div>
				<div> <a href="/pflegeweiterbildung_p"> Pflege: Weiterbildung </a> </div>
		</div>

		<div class="item-teilnahme">
			<div> Teilnahme: </div>
			<div> <a href="/sichtweisemitarbeiter_p"> - Sichtweise: Mitarbeiter </a> </div>
			<div> <a href="/sichtweiseweiterbildungen_p"> - Sichtweise: Weiterbildung </a> </div>				
		</div>

		<div class="item-auswertung">
			<div> Auswertung: </div>
			<div> <a href="/auswertung_mitarbeiter_p"> - Mitarbeiter </a> </div>
			<div> <a href="/auswertung_weiterbildungen_p"> - Weiterbildung </a> </div>
			<div> <a href="/auswertung_zertifikat_p"> - Zertifikate </a> </div>
		</div>
		
		<!-- Oben nichts verändern-->
		<!-- Hier wird immer der Inhaltsbereich verändert-->

		<div class="item-main">
			<h3>Weiterbildung Formular</h3>
		
				<form id="mitarbeiterform" action="/pflegeweiterbildung_speichern_p" method="POST">
						<input type="hidden" value="${id_str}" id="id_s" name="id_s" />

						<div>
							<label for="bezeichnung_s">Bezeichnung</label>
							<input type="text" value="${data_o[0]}" id="bezeichnung_s" name="bezeichnung_s" required />
						</div>
					
						<div>
							<label for="von_date">Von</label>
							<input type="date" value="${data_o[1]}" id="von_date" name="von_date" required />
						</div>
					
						<div>
							<label for="bis_date">Bis</label>
							<input type="date" value="${data_o[2]}" id="bis_date" name="bis_date" required />
						</div>
					
						<div>
							<label for="beschreibung_text">Beschreibung</label>
							<input type="text" value="${data_o[3]}" id="beschreibung_text" name="beschreibung_text" required />
						</div>
					
						<div>
							<label for="max_teilnehmeranzahl_int">max. Teilnehmeranzahl</label>
							<input type="integer" value="${data_o[4]}" id="max_teilnehmeranzahl_int" name="max_teilnehmeranzahl_int" required />
						</div>
					
						<div id="Formular">
							<label for="min_teilnehmeranzahl_int">min. Teilnehmeranzahl</label>
							<input type="integer" value="${data_o[5]}" id="min_teilnehmeranzahl_int" name="min_teilnehmeranzahl_int" required />
						</div>
					
						<div id="Button_Formular">
							<input id="buttons" type="submit" value="Speichern">
						</div>
					
				</form>
