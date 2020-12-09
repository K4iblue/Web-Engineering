## -*- coding: utf-8 -*-
	<div id="Headline">Weiterbildungen zum stornieren</div>
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
%for key_s in data_o[1]:
	%if data_o[1][key_s][0] != "":
	
		%for key_B_s in data_o[2]:
			%if data_o[2][key_B_s][1] is id_str:
				%if data_o[2][key_B_s][0] is key_s:
					<% i = i + 1 %>
					<!--${i}, ${key_B_s}, ${id_str}-->
						<tr>
							<td>${key_s}</td>
							<td>${data_o[1][key_s][0]}</td>
							<td>${data_o[1][key_s][1]}</td>
							<td>${data_o[1][key_s][2]}</td>
							<td>${data_o[1][key_s][3]}</td>
							<td>${data_o[1][key_s][4]}</td>
							<td>${data_o[1][key_s][5]}</td>
							<td>
								<a href="/deleteteilnahme_p/${key_B_s}?idM_spl=${id_str}" id="buttons">stonieren</a>
							</td>
						</tr>
				%endif
			%endif
		%endfor
		
	%endif
%endfor
		</table>
	<p>
	<a id="hauptseite" href="/sichtweisemitarbeiter_p">
		<input type="submit" value="zurueck" id="Button_input">
	</a>
	</p>
</body>
</html>