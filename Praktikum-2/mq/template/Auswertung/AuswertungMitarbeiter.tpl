## -*- coding: utf-8 -*-
<body>
	<div>
	<div id="Headline" > Auswertung der Mitarbeiterdaten</div>
	<table>
		<tr>
			<th>ID</th>
			<th>Akademischer Grad</th>
			<th>Name</th>
			<th>Vorname</th>
			<th>Tätigkeit</th>
			<th>Aktion</th>
		</tr>
		<% i = 0 %>
<% j = -1 %>
%for key_s in data_o:
	<% j = j + 1 %>
	%if data_o[key_s][0] is not "":
		<% i = i + 1 %>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[key_s][2]}</td>
				<td>${data_o[key_s][0]}</td>
				<td>${data_o[key_s][1]}</td>
				<td>${data_o[key_s][3]}</td>
				<td>
					<a href="/auswertung_mitarbeiter_Info_p/${key_s}" id="buttons">Information</a>		<!--TODO-->
				</td>
			</tr>
	%endif
%endfor
</table>
</div>
</body>
</html>