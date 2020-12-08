## -*- coding: utf-8 -*-
<body>
	<div id="Headline">Mitarbeiter Formular</div>

<form id="idWTForm" action="/pflegeweiterbildung_speichern_p" method="POST">
	<div id="FormStud1">
		<input type="hidden" value="${id_str}" id="id_s" name="id_s" />
		<div id="Formular">
			<label id="HeadlineStudent"> Weiterbildung </label>
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="bezeichnung_s">Bezeichnung</label>
			</div>
			<input type="text" value="${data_o[0]}" id="bezeichnung_s" name="bezeichnung_s" required />
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="von_date">Von</label>
			</div>
			<input type="date" value="${data_o[1]}" id="von_date" name="von_date" required />
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="bis_date">Bis</label>
			</div>
			<input type="date" value="${data_o[2]}" id="bis_date" name="bis_date" required />
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="beschreibung_text">Beschreibung</label>
			</div>
			<input type="text" value="${data_o[3]}" id="beschreibung_text" name="beschreibung_text" required />
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="max_teilnehmeranzahl_int">max. Teilnehmeranzahl</label>
			</div>
			<input type="integer" value="${data_o[4]}" id="max_teilnehmeranzahl_int" name="max_teilnehmeranzahl_int" required />
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="min_teilnehmeranzahl_int">min. Teilnehmeranzahl</label>
			</div>
			<input type="integer" value="${data_o[5]}" id="min_teilnehmeranzahl_int" name="min_teilnehmeranzahl_int" required />
		</div>
			<div id="Button_Formular">
				<input id="Button_input" type="submit" value="Speichern">
			</div>
		</div>
</form>
