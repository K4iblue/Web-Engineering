## -*- coding: utf-8 -*-
<body>
	<div>
	<div id="Headline">Auswertung der Weiterbildungdaten</div>
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
<% j = -1 %>
<% id = 0 %>
%for key_s in data_o:
	<% j = j + 1 %>
	%if data_o[key_s][0] is not "":
		<% i = i + 1 %>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[key_s][0]}</td>
				<td>${data_o[key_s][1]}</td>
				<td>${data_o[key_s][2]}</td>
				<td>${data_o[key_s][4]}</td>
				<td>${data_o[key_s][5]}</td>
				<td>
					<a href="/auswertung_weiterbildung_Info_p/${key_s}" id="buttons">Information</a>		<!--TODO-->
				</td>
			</tr>
	%endif
%endfor
	</table>
</div>
</body>
</html>