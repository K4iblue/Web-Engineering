## -*- coding: utf-8 -*-
	<body>

	<label id="HeadlineStudent"> Weiterbildung </label>
		<p>Name: ${data_o[1][id_str][0]}</p>
		<p>vom ${data_o[1][id_str][1]} bis zum ${data_o[1][id_str][2]}</p>
		<p>min. Anzahl: ${data_o[1][id_str][5]} </p>
		<p>max. Anzahl: ${data_o[1][id_str][4]}</p>
		
	<label id="HeadlineStudent"> Qualifikation </label>
		<p>Beschreibung: ${data_o[3][0]}</p>
		<p>Bezeichnung: ${data_o[3][1]}</p>
		
	<label id="HeadlineStudent"> Zertifikat </label>
		<p>Beschreibung: ${data_o[4][0]}</p>
		<p>Bezeichnung: ${data_o[4][1]}</p>
		<p>berechtigt zu: ${data_o[4][2]}</p>

		<div id="Headline">Teilnehmer</div>
		<table>
			<tr>
				<th>ID</th>
				<th>Akademischer Grad</th>
				<th>Vorname</th>
				<th>Name</th>
				<th>Qualifikation</th>
				<th>Zertifikate</th>
			</tr>
		
		
		%for key_s in data_o[2]:
			%if data_o[2][key_s][0] is id_str:
				<% MitarbeiterID = data_o[2][key_s][1] %>
		
					<tr>
						<td>${key_s}</td>
						<td>${data_o[0][MitarbeiterID][2]}</td>
						<td>${data_o[0][MitarbeiterID][1]}</td>
						<td>${data_o[0][MitarbeiterID][0]}</td>
						
						%if data_o[2][key_s][2] is ["erfolgreich beendet"]:
							<td>JA</td>
						%elif data_o[2][key_s][2] is "nicht erfolgreich beendet":
							<td>NEIN</td>
						%else:
							<td>"${data_o[2][key_s][2]}"</td>
						%endif
						
						%if data_o[2][key_s][2] is "erfolgreich beendet":
							<td>JA</td>
						%elif data_o[2][key_s][2] is "nicht erfolgreich beendet":
							<td>NEIN</td>
						%else:
							<td>"${data_o[2][key_s][2]}"</td>
						%endif
					</tr>
			%endif
		%endfor
		</table>

		<p>
			<a id="hauptseite" href="/pflegeweiterbildung_p">
				<input type="submit" value="zurueck" id="Button_input">
			</a>
			</p>
		</body>
		</html>