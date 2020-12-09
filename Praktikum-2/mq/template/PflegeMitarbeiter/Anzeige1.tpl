## -*- coding: utf-8 -*-
		<div id="Headline">Weiterbildungen an denen Teilgenommen wird/wurde</div>

	<table>
		<tr>
			<th>ID</th>
			<th>Bezeichnung</th>
			<th>Von</th>
			<th>Bis</th>
			<th>Beschreibung</th>
			<th>max. Teilnehmeranzahl</th>
			<th>min. Teilnehmeranzahl</th>
		</tr>

%for key_s in data_o[1]:
	%if data_o[1][key_s][0] != "":
	
		%for key_B_s in data_o[2]:
			%if data_o[2][key_B_s][1] is id_str:
				%if data_o[2][key_B_s][0] is key_s:

						<tr>
							<th>${key_s}</td>
							<td>${data_o[1][key_s][0]}</td>
							<td>${data_o[1][key_s][1]}</td>
							<td>${data_o[1][key_s][2]}</td>
							<td>${data_o[1][key_s][3]}</td>
							<td>${data_o[1][key_s][4]}</td>
							<td>${data_o[1][key_s][5]}</td>
						</tr>

				%endif
			%endif
		%endfor
		
	%endif
%endfor
		
</table>

<div id="Headline">Qualifikation</div>

	<table>
		<tr>
			<th>ID</th>
			<th>Bezeichnung</th>
			<th>Beschreibung</th>
			<th>Zustand</th>
		</tr>
%for key_s in data_o[1]:
	%if data_o[1][key_s][0] != "":
	
		%for key_B_s in data_o[2]:
			%if data_o[2][key_B_s][1] is id_str:
				%if data_o[2][key_B_s][0] is key_s:
					%if data_o[3][key_s][0] != "":
						<tr>
							<th>${key_s}</td>
							<td>${data_o[3][key_s][0]}</td>
							<td>${data_o[3][key_s][1]}</td>
							<td>${data_o[2][key_B_s][2]}</td>
						</tr>
					%endif
				%endif
			%endif
		%endfor
		
	%endif
%endfor
</table>

<div id="Headline">Zertifikat</div>

	<table>
		<tr>
			<th>ID</th>
			<th>Bezeichnung</th>
			<th>Beschreibung</th>
			<th>berechtigt zu</th>
			<th>Zustand</th>
		</tr>
%for key_s in data_o[1]:
	%if data_o[1][key_s][0] != "":
	
		%for key_B_s in data_o[2]:
			%if data_o[2][key_B_s][1] is id_str:
				%if data_o[2][key_B_s][0] is key_s:
					%if data_o[3][key_s][0] != "":
						<tr>
							<th>${key_s}</td>
							<td>${data_o[4][key_s][0]}</td>
							<td>${data_o[4][key_s][1]}</td>
							<td>${data_o[4][key_s][2]}</td>
							<td>${data_o[2][key_B_s][2]}</td>
						</tr>
					%endif
				%endif
			%endif
		%endfor
		
	%endif
%endfor		
</table>

	<p>
	<a id="hauptseite" href="/pflegemitarbeiter_p">
		<input type="submit" value="zurueck" id="Button_input">
	</a>
	</p>
</body>
</html>