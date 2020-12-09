## -*- coding: utf-8 -*-
<!DOCTYPE html>
<html id="overview">

<head>
	<title>Mitarbeiter-Qualifizierung</title>
	<meta charset="UTF-8" />
	<style> @import "/style.css"; </style>
	<script type="text/javascript" src="/mitarbeiterquali.js"></script>
</head>

<% x = 0 %>
%for key_s in data_o[0][0]:
	%if data_o[0][0][key_s][0] is not "":
		<% x = x + 1 %>
	%endif
%endfor

<% datum = data_o[1] %>

<% heute = str(datum.year) + "-" + str(datum.month) + "-" + '0' + str(datum.day) %>

<body>
	<div class="container">
		<div class="item-header">
			<div> Mitarbeiter-Qualifizierung: </div>
			<div> Version 1.0 / 10.12.2020 </div>
		</div>

		<div class="item-team">
			<div> Gruppe: Kai Klaps, Matthias Wiese, Marvin Schlitter, Tomas Kublickas</div>
		</div>

		<div class="item-startseite">
			<div> <a href="/hauptseite_p"> Startseite </a> </div>
		</div>

		<div class="item-pflege">
			<div> Datenpflege: </div>
				<div> <a href="/pflegemitarbeiter_p"> Pflege: Mitarbeiterdaten </a> </div>
				<div> <a href="/pflegeweiterbildung_p"> Pflege: Weiterbildung </a> </div>
		</div>

		<div class="item-teilnahme">
			<div> Teilnahme: </div>
			<div> <a href="/sichtweisemitarbeiter_p"> - Sichtweise: Mitarbeiter </a> </div>
			<div> <a href="/sichtweiseweiterbildungen_p"> - Sichtweise: Weiterbildung </a> </div>				
		</div>

		<div class="item-auswertung">
			<div> Auswertung: </div>
			<div> <a href="/auswertung_mitarbeiter_p"> - Mitarbeiter </a> </div>
			<div> <a href="/auswertung_weiterbildungen_p"> - Weiterbildung </a> </div>
			<div> <a href="/auswertung_zertifikat_p"> - Zertifikate </a> </div>
		</div>
		
		<!-- Oben nichts verändern-->
		<!-- Hier wird immer der Inhaltsbereich verändert-->
		<div class="item-main">
			<p>Anzahl der Mitarbeiter: ${x}</p>
			
	<% y = 0 %>
	%for key_s in data_o[0][1]:
		%if data_o[0][1][key_s][0] is not "":
			<% anfang = data_o[0][1][key_s][1] %>
			<% ende = data_o[0][1][key_s][2] %>
			%if ( ( anfang.split('-')[0] > heute.split('-')[0] ) or ( anfang.split('-')[0] == heute.split('-')[0] and anfang.split('-')[1] > heute.split('-')[1]) or ( anfang.split('-')[0] 	== heute.split('-')[0] and anfang.split('-')[1] == heute.split('-')[1] and anfang.split('-')[2] > heute.split('-')[2]) ):
				<% y = y + 1 %>
			%endif
		%endif
	%endfor
			
		<p>Anzahl der Weiterbildungen (in Planung): ${y}</p>
			
			
	<% z = 0 %>
	%for key_s in data_o[0][1]:
		%if data_o[0][1][key_s][0] is not "":
			<% anfang = data_o[0][1][key_s][1] %>
			<% ende = data_o[0][1][key_s][2] %>
			%if ( ( ( anfang.split('-')[0] < heute.split('-')[0] ) or ( anfang.split('-')[0] == heute.split('-')[0] and anfang.split('-')[1] < heute.split('-')[1]) or ( anfang.split('-')[0] 	== heute.split('-')[0] and anfang.split('-')[1] == heute.split('-')[1] and anfang.split('-')[2] < heute.split('-')[2]) ) and ( ( ende.split('-')[0] > heute.split('-')[0] ) or ( 	ende.split('-')[0] == heute.split('-')[0] and ende.split('-')[1] > heute.split('-')[1]) or ( ende.split('-')[0] == heute.split('-')[0] and ende.split('-')[1] == heute.split('-')	[1] and ende.split('-')[2] > heute.split('-')[2] ) ) ):
				<% z = z + 1 %>
			%endif
		%endif
	%endfor
		<p>Anzahl der Weiterbildungen (laufend): ${z}</p>
			
			
	<% a = 0 %>
	%for key_s in data_o[0][1]:
		%if data_o[0][1][key_s][0] is not "":
			<% anfang = data_o[0][1][key_s][1] %>
			<% ende = data_o[0][1][key_s][2] %>
			%if ( ( ende.split('-')[0] < heute.split('-')[0] ) or ( ende.split('-')[0] == heute.split('-')[0] and ende.split('-')[1] < heute.split('-')[1]) or ( ende.split('-')[0] == heute.	split('-')[0] and ende.split('-')[1] == heute.split('-')[1] and ende.split('-')[2] < heute.split('-')[2]) ):
				<% a = a + 1 %>
			%endif
		%endif
	%endfor
		<p>Anzahl der Weiterbildungen (abgeschlossen): ${a}</p>
			
			
	<% b = 0 %>
	%for key_s in data_o[0][2]:
		%if data_o[0][2][key_s][0] is not "":
			<% b = b + 1 %>
		%endif
	%endfor
		<p>Anzahl der Teilnahmen: ${b}</p>
	</div>
</body>
</html> 