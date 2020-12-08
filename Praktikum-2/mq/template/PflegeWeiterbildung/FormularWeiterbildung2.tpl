## -*- coding: utf-8 -*-
<form id="idWTForm" action="/pflegeweiterbildung_q_speichern_p" method="POST">
	<div id="FormStud1">
		<input type="hidden" value="${id_str}" id="id_s" name="id_s" />
		<div id="Formular">
			<label id="HeadlineStudent"> Qualifikation </label>
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="bezeichnung_s">Bezeichnung</label>
			</div>
			<input type="text" value="${data_o[0]}" id="bezeichnung_s" name="bezeichnung_s" required />
		</div>
		<div id="Formular">
			<div id="Formular1">
				<label for="beschreibung_text">Beschreibung</label>
			</div>
			<input type="text" value="${data_o[1]}" id="beschreibung_text" name="beschreibung_text" required />
		</div>
			<div id="Button_Formular">
				<input id="Button_input" type="submit" value="Speichern">
			</div>
		</div>
</form>