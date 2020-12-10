## -*- coding: utf-8 -*-

<h4>Weiterbildungen an denen Teilgenommen wird/wurde</h4>

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
					
						<!-- Schleife über alle Weiterbildungen (data_o[1]) -->
							<!-- Schleife über alle Teilnehmer (data_o[2]) -->
								<!-- Diese werden dann miteinander verglichen -->
								<!-- Wenn wir übereinstimmungen haben >> fülle Tabelle mit werten von  Weiterbildung -->
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

<h4>Qualifikation</h4>

					<table>
						<tr>
							<th>ID</th>
							<th>Bezeichnung</th>
							<th>Beschreibung</th>
							<th>Zustand</th>
						</tr>

						<!-- Schleife über alle Weiterbildungen (data_o[1]) -->
							<!-- Schleife über alle Teilnehmer (data_o[2]) -->
								<!-- Diese werden dann miteinander verglichen -->
								<!-- Wenn wir übereinstimmungen haben >> fülle Tabelle mit werten von der zugehörigen Qualifikation (data_o[3] -->
						%for key_s in data_o[1]:
							%if data_o[1][key_s][0] != "":

								%for key_B_s in data_o[2]:
									%if data_o[2][key_B_s][1] is id_str:
										%if data_o[2][key_B_s][0] is key_s:
											%if data_o[3][key_s][0] != "":
						<tr>
							<td>${key_s}</td>
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

<h4>Zertifikat<h4>

					<table>
						<tr>
							<th>ID</th>
							<th>Bezeichnung</th>
							<th>Beschreibung</th>
							<th>berechtigt zu</th>
							<th>Zustand</th>
						</tr>

						<!-- Schleife über alle Weiterbildungen (data_o[1]) -->
							<!-- Schleife über alle Teilnehmer (data_o[2]) -->
								<!-- Diese werden dann miteinander verglichen -->
									<!-- Wenn wir übereinstimmungen haben >> fülle Tabelle mit werten von dem zugehörigen Zertifikat (data_o[4] -->
						%for key_s in data_o[1]:
							%if data_o[1][key_s][0] != "":
								%for key_B_s in data_o[2]:
									%if data_o[2][key_B_s][1] is id_str:
										%if data_o[2][key_B_s][0] is key_s:
											%if data_o[3][key_s][0] != "":

						<tr>
							<td>${key_s}</td>
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

			<div>
				<a id="hauptseite" href="/pflegemitarbeiter_p">
					<input type="submit" value="zurueck" id="buttons">
				</a>
			</div>
		</div>
</body>
</html>