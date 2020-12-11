## -*- coding: utf-8 -*-
				<hr>
				<h3> Qualifikation </h3>

				<form id="mitarbeiterform" action="/pflegeweiterbildung_q_speichern_p" method="POST">
						<input type="hidden" value="${id_str}" id="id_s" name="id_s" />
				
						<div>			
							<label for="bezeichnung_s">Bezeichnung</label>
							<input type="text" value="${data_o[0]}" id="bezeichnung_s" name="bezeichnung_s" required />
						</div>
					
						<div>
							<label for="beschreibung_text">Beschreibung</label>
							<input type="text" value="${data_o[1]}" id="beschreibung_text" name="beschreibung_text" required />
						</div>
					
							<div id="Button_Formular">
								<input id="buttons" type="submit" value="Speichern">
							</div>
				</form>
