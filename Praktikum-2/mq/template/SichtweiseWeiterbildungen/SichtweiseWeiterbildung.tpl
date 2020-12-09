## -*- coding: utf-8 -*-
<body>
	<div>
	<div id="Headline">Aktuelle Weiterbildungen</div>
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
		
<% datum = data_o[1] %>
<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>
<% i = 0 %>
%for key_s in data_o[0]:
	%if data_o[0][key_s][0] != "":
		<% anfang = data_o[0][key_s][1] %>
		%if anfang < heute:
			<% i = i + 1%>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[0][key_s][0]}</td>
				<td>${data_o[0][key_s][1]}</td>
				<td>${data_o[0][key_s][2]}</td>
				<td>${data_o[0][key_s][4]}</td>
				<td>${data_o[0][key_s][5]}</td>
				<td>
					<a href="/sichtweiseweiterbildungen_Aktuelle_Weiterbildungen_p/${key_s}" id="buttons">Information</a> 
			 </td>
			</tr>
		%endif
	%endif
%endfor
</table>

<body>
	<div>
	<div id="Headline">Geplante Weiterbildungen</div>
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
<% datum = data_o[1] %>
<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

%for key_s in data_o[0]:
	%if data_o[0][key_s][0] != "":
		<% anfang = data_o[0][key_s][1] %>
		%if anfang > heute:
			<% i = i + 1 %>
			<tr>
				<th>${key_s}</td>
				<td>${data_o[0][key_s][0]}</td>
				<td>${data_o[0][key_s][1]}</td>
				<td>${data_o[0][key_s][2]}</td>
				<td>${data_o[0][key_s][4]}</td>
				<td>${data_o[0][key_s][5]}</td>
				<td>
					<a href="/sichtweiseweiterbildungen_Zukuenftige_Weiterbildungen_p/${key_s}" id="buttons">Information</a> 
			 </td>
			</tr>
		%endif
	%endif
%endfor
</table>
</div>
</body>
</html>