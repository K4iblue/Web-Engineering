## -*- coding: utf-8 -*-
<hr>
<h4>Weiterbildungen zum stornieren</h4>
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

				<div>
				<a id="hauptseite" href="/sichtweisemitarbeiter_p">
					<input type="submit" value="zurueck" id="buttons">
				</a>
				</div>
		</div>
	</div>
</body>
</html>