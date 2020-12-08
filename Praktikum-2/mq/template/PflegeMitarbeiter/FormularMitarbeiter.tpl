## -*- coding: utf-8 -*-
<body>
	<div id="Headline">Mitarbeiter Formular</div>
	<form id="idWTForm" action="/pflegemitarbeiter_speichern_p" method="POST">
		<div id="FormStud1">
			<input type="hidden" value="${id_str}" id="id_s" name="id_s" />
			<div id="Formular">
				<label id="HeadlineStudent"> Mitarbeiter </label>
			</div>
			<div id="Formular">
				<div id="Formular1">
					<label for="name_s">Name</label>
				</div>
				<input type="string" value="${data_o[0]}" id="name_s" name="name_s" required />
			</div>
			<div id="Formular">
				<div id="Formular1">
					<label for="vorname_s">Vorname</label>
				</div>
				<input type="string" value="${data_o[1]}" id="vorname_s" name="vorname_s" required />
			</div>
			<div id="Formular">
				<div id="Formular1">
					<label for="titel_s">Akademischer Grad</label>
				</div>
				<input type="string" value="${data_o[2]}" id="titel_s" name="titel_s" required />
			</div>
			<div id="Formular">
				<div id="Formular1">
					<label for="taetigkeit_s">Tätigkeit</label>
				</div>
				<input type="string" value="${data_o[3]}" id="taetigkeit_s" name="taetigkeit_s" required />
			</div>
		</div>
	</div>
	<div id="Button_Formular">
		<input id="Button_input" type="submit" value="Speichern">
	</div>

</form>
		<a id="hauptseite" href="/pflegemitarbeiter_p">
			<input type="submit" value="zurueck" id="Button_input">
		</a>
</body>
</html>