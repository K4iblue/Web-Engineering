			
					## -*- coding: utf-8 -*-
					<div>Weiterbildungen an denen Teilgenommen wird/wurde:</div>
			
						<table>
							<tr>
								<th>ID</th>
								<th>Bezeichnung</th>
								<th>Von</th>
								<th>Bis</th>
								<th>Zustand</th>
							</tr>

								<!-- Schleife über alle Weiterbildungen (data_o[1]) -->
								<!-- Schleife über alle Teilnahmen (data_o[2]) -->
								%for key_s in data_o[1]:
									%if data_o[1][key_s][0] != "":
						
										%for key_B_s in data_o[2]:
											%if data_o[2][key_B_s][1] is id_str:
												%if data_o[2][key_B_s][0] is key_s:
						
							<tr>
								<td>${key_s}</td>
								<td>${data_o[1][key_s][0]}</td>
								<td>${data_o[1][key_s][1]}</td>
								<td>${data_o[1][key_s][2]}</td>
								<td>${data_o[2][key_B_s][2]}</td>
							</tr>
						
												%endif
											%endif
										%endfor
						
									%endif
								%endfor
						</table>
						
						<p>
							<a id="hauptseite" href="/auswertung_mitarbeiter_p">
							<input type="submit" value="zurueck" id="buttons">
							</a>
						</p>
	</body>
</html>