## -*- coding: utf-8 -*-
<body>
	<div>
	<div id="Headline">Auswertung der Zertifikate</div>
	<table>
		<tr>
			<th>ID</th>
			<th>Bezeichnung</th>
			<th>Beschreibung</th>
			<th>berechtigt zu</th>
		</tr>
		<% i = 0 %>
<% j = -1 %>
%for key_s in data_o:
	<% j = j + 1 %>
	%if data_o[key_s][0] != "":
		<% i = i + 1 %>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[key_s][0]}</td>
				<td>${data_o[key_s][1]}</td>
				<td>${data_o[key_s][2]}</td>
			</tr>
	%endif
%endfor
</table>
</div>
</body>
</html>