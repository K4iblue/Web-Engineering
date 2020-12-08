## -*- coding: utf-8 -*-
<% x = 0 %>
%for key_s in data_o[0][0]:
	%if data_o[0][0][key_s][0] is not "":
		<% x = x + 1 %>
	%endif
%endfor

<% datum = data_o[1] %>

<% heute = str(datum.year) + "-" + str(datum.month) + "-" + str(datum.day) %>


<body>
	<p>Anzahl der Mitarbeiter: ${x}</p>
	
	
<% y = 0 %>
%for key_s in data_o[0][1]:
	%if data_o[0][1][key_s][0] is not "":
		<% anfang = data_o[0][1][key_s][1] %>
		%if heute < anfang:
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
		%if heute >= anfang and ende >= heute:
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
		%if ende < heute:
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

</body>
</html> 