## -*- coding: utf-8 -*-
				<h4>Teilnehmer mit erfolgreichen Abschluss<h4>
			<table>
				<tr>
					<th>ID</th>
					<th>Name</th>
					<th>Vorname</th>
					<th>Akademischer Grad</th>
					<th>Tätigkeit</th>
				</tr>
			
				<!-- Schleife über Teilnahmen (data_o[2]) -->
				<!-- Nur Mitarbeiter mit "erfolgreich beendet"  werden angezeigt-->
				%for key_s in data_o[2]:
					%if data_o[2][key_s][0] is id_str:
						<% MitarbeiterID = data_o[2][key_s][1] %>
						%if data_o[2][key_s][2] == "erfolgreich beendet":
				<tr>
					<td>${key_s}</td>
					<td>${data_o[0][MitarbeiterID][0]}</td>
					<td>${data_o[0][MitarbeiterID][1]}</td>
					<td>${data_o[0][MitarbeiterID][2]}</td>
					<td>${data_o[0][MitarbeiterID][3]}</td> 
				</tr>
						%endif
					%endif
				%endfor
			</table>

			<p>
				<a id="hauptseite" href="/auswertung_weiterbildungen_p">
				<input type="submit" value="zurueck" id="buttons">
				</a>
			</p>
			
		</div>
</body>
</html>