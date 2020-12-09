## -*- coding: utf-8 -*-
<body>
	<div>
	<div id="Headline">Pflege der Mitarbeiterdaten</div>
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
					<a href="/pflegemitarbeiter_anzeigen_p/${key_s}" id="buttons">anzeigen</a> 
					<a href="/pflegemitarbeiter_bearbeiten_p/${key_s}" id="buttons">bearbeiten</a>                   
					<a href="/deletemitarbeiter_p/${key_s}" class="clDelete" id="buttons">löschen</a> 
			 </td>
			</tr>
	%endif
%endfor
</table>
<div>
	<a href="/pflegemitarbeiter_bearbeiten_p">
	<input type="submit" value="erfassen" id="Button_input">
	</a>
</div>
</div>
</body>
</html>