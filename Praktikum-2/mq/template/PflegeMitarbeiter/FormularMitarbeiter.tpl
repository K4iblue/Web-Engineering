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
				<div> <a href="/pflegemitarbeiter_p"> - Pflege: Mitarbeiter </a> </div>
				<div> <a href="/pflegeweiterbildung_p"> - Pflege: Weiterbildung </a> </div>
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
			<h3>Mitarbeiter Formular</h3>
				<form id="mitarbeiterform" action="/pflegemitarbeiter_speichern_p" method="POST">
							<input type="hidden" value="${id_str}" id="id_s" name="id_s" />

							<div>
								<label for="name_s">Name</label>
								<input type="string" value="${data_o[0]}" id="name_s" name="name_s" required />
							</div>

							<div>
								<label for="vorname_s">Vorname</label>
								<input type="string" value="${data_o[1]}" id="vorname_s" name="vorname_s" required />
							</div>

							<div>
								<label for="titel_s">Akademischer Grad</label>							
								<input type="string" value="${data_o[2]}" id="titel_s" name="titel_s" required />
							</div>

							<div>
								<label for="taetigkeit_s">Tätigkeit</label>
								<input type="string" value="${data_o[3]}" id="taetigkeit_s" name="taetigkeit_s" required />
							</div>

							<div>
								<input id="buttons" type="submit" value="Speichern">
							</div>
				</form>

				<div>
					<a id="hauptseite" href="/pflegemitarbeiter_p">
						<input type="submit" value="zurueck" id="buttons">
					</a>
				</div>
		</div>
</body>
</html>