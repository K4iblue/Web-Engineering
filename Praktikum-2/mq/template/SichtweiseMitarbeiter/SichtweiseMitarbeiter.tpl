## -*- coding: utf-8 -*-
<body>
	<div>
	<div id="Headline">Sichtweise der Mitarbeiterdaten</div>
	<table>
		<tr>
			<th>ID</th>
			<th>Name</th>
			<th>Vorname</th>
			<th>Akademischer Grad</th>
			<th>Tätigkeit</th>
			<th>Aktion</th>
		</tr>
		<% i = 0 %>
%for key_s in data_o:
	%if data_o[key_s][0] != "":
			<% i = i + 1 %>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[key_s][0]}</td>
				<td>${data_o[key_s][1]}</td>
				<td>${data_o[key_s][2]}</td>
				<td>${data_o[key_s][3]}</td>
				<td>
					<a href="/sichtweisemitarbeiter_information_p/${key_s}" id="buttons">Information</a> 
			 </td>
			</tr>
	%endif
%endfor
		</table>
	</div>
	</body>
</html>