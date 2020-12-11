## -*- coding: utf-8 -*-
			<h3>Teilnehmer</h3>
			<table>
				<tr>
					<th>ID</th>					
					<th>Name</th>
					<th>Vorname</th>
					<th>Akademischer Grad</th>
					<th>Tätigkeit</th>
					<th>Status</th>
					<th>Aktion</th>
				</tr>

				<!-- Schleife über alle Mitarbeiter -->
				<!-- Todo -->
				<% datum = data_o[1] %>
				<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>
				<% i = 0 %>

				%for key_s in data_o[0][2]:
					%if data_o[0][2][key_s][0] is id_str:
								<% MitarbeiterID = data_o[0][2][key_s][1] %>
								<% anfang = data_o[0][1][id_str][1] %>
								<% ende = data_o[0][1][id_str][2] %>
								<% i = i + 1%>
				
				<tr>
					<td>${key_s}</td>
					<td>${data_o[0][0][MitarbeiterID][0]}</td>
					<td>${data_o[0][0][MitarbeiterID][1]}</td>
					<td>${data_o[0][0][MitarbeiterID][2]}</td>
					<td>${data_o[0][0][MitarbeiterID][3]}</td>
					<td>${data_o[0][2][key_s][2]}</td>
					<td>
						%if heute > ende:
							<a href="/sichtweiseweiterbildungen_Status_p/${id_str}?id_s=${key_s}&Status=erfolgreich beendet" id="buttons">Erfolgreich</a>
							<a href="/sichtweiseweiterbildungen_Status_p/${id_str}?id_s=${key_s}&Status=nicht erfolgreich beendet" id="buttons">Nicht Erfolgreich</a>
						%else:
							<a href="/deleteteilnahme2_p/${key_s}?idW_spl=${id_str}" id="buttons">entfernen</a>
						%endif
					</td>
				</tr>
					%endif
				%endfor
			</table>

			<div>
			<a id="hauptseite" href="/sichtweiseweiterbildungen_p">
				<input type="submit" value="zurueck" id="buttons">
			</a>
			</div>
		</div>
	</div>
</body>
</html>