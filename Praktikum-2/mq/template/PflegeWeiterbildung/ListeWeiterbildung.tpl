## -*- coding: utf-8 -*-
<body>
	<div id="Headline">Pflege der Weiterbildungen</div>
	<table>
		<tr>
			<th>ID</th>
			<th>Bezeichnung</th>
			<th>Von</th>
			<th>Bis</th>
			<th>Beschreibung</th>
			<th>max. Teilnehmeranzahl</th>
			<th>min. Teilnehmeranzahl</th>
			<th>Aktion</th>
		</tr>
		<% i = 0 %>
%for key_s in data_o:
	%if data_o[key_s][0] is not "":
			<% i = i + 1 %>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[key_s][0]}</td>
				<td>${data_o[key_s][1]}</td>
				<td>${data_o[key_s][2]}</td>
				<td>${data_o[key_s][3]}</td>
				<td>${data_o[key_s][4]}</td>
				<td>${data_o[key_s][5]}</td>
				<td>
					<a href="/pflegeweiterbildung_anzeigen_p/${key_s}" id="buttons">anzeigen</a> 
					<a href="/pflegeweiterbildung_bearbeiten_p/${key_s}" id="buttons">bearbeiten</a>                   
					<a href="/deleteweiterbildung_p/${key_s}" class="clDelete" id="buttons">löschen</a> 
			 </td>
			</tr>
	%endif
%endfor
</table>
<div>
	<a href="/pflegeweiterbildung_bearbeiten_p">
	<input type="submit" value="erfassen" id="Button_input">
	</a>
</div>
</body>
</html>