## -*- coding: utf-8 -*-
<hr>
<h4>Weiterbildungen zum anmelden<h4>
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
		
						<% datum = data_o[1] %>

						<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>

						<% x = 0 %>
						<% i = 0 %>
						%for key_s in data_o[0][1]:
							%if data_o[0][1][key_s][0] != "":

								<% x = 0 %>
								%for key_B_s in data_o[0][2]:
									%if data_o[0][2][key_B_s][0] is key_s and data_o[0][2][key_B_s][1] is id_str:
										<!--## ID Weiterbildung = key_s(Weiterbildung), dann soll nichts angezeigt werden-->
										<% x = 1 %>
									%endif
								%endfor

								% if x is 0:
									<% anfang = data_o[0][1][key_s][1] %>
									%if heute <= anfang:
										<% i = i + 1 %>
						<tr>
							<td>${key_s}</td>
							<td>${data_o[0][1][key_s][0]}</td>
							<td>${data_o[0][1][key_s][1]}</td>
							<td>${data_o[0][1][key_s][2]}</td>
							<td>${data_o[0][1][key_s][3]}</td>
							<td>${data_o[0][1][key_s][4]}</td>
							<td>${data_o[0][1][key_s][5]}</td>
							<td>
								<a href="/sichtweisemitarbeiter_eintragen_p/${key_s}?idM_spl=${id_str}" id="buttons">anmelden</a>
							</td>
						</tr>
									%endif
								%endif
							%endif
						%endfor
					</table>
