<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Auswertung - Zertifikate - Detail</div>

<hr>

<div class="headline_small">Mitarbeiter</div>
<table class="overview">
	<tr>
        <th>Name</th>
        <th>Vorname</th>
        <th>akademische Grade</th>
        <th>Tätigkeit</th>
    </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i in context@
       @entry_a = context[loop_i];@
            <tr>
                <td>#entry_a['name']#</td>
                <td>#entry_a['vorname']#</td>
	        	<td>#entry_a['akagrad']#</td>
	        	<td>#entry_a['taetigkeit']#</td>
            </tr>
    @endfor@
</table>


<div>
    <button class="zurück_auswertung_zertifikat" id="idBackAuswertungZertifikat">Zurück</button>
</div>

<div> </div>
<!-- EOF -->
				
				