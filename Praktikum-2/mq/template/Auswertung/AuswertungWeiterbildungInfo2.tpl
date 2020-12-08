## -*- coding: utf-8 -*-
	<div id="Headline">Teilnehmer</div>
<table>
	<tr>
		<th>ID</th>
		<th>Akademischer Grad</th>
		<th>Vorname</th>
		<th>Name</th>
		<th>Tätigkeit</th>
	</tr>


%for key_s in data_o[2]:
	%if data_o[2][key_s][0] is id_str:
		<% MitarbeiterID = data_o[2][key_s][1] %>

			<tr>
				<td>${key_s}</td>
				<td>${data_o[0][MitarbeiterID][2]}</td>
				<td>${data_o[0][MitarbeiterID][1]}</td>
				<td>${data_o[0][MitarbeiterID][0]}</td>
				<td>${data_o[0][MitarbeiterID][3]}</td> 
			</tr>
	%endif
%endfor
</table>
<p>
	<a id="hauptseite" href="/auswertung_weiterbildungen_p">
		<input type="submit" value="zurueck" id="Button_input">
	</a>
	</p>
</body>
</html>