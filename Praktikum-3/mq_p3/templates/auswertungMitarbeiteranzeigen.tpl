<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Auswertung - Mitarbeiter - Detail</div>

<hr>

<div class="headline_small">Mitarbeiter</div>
<table class="overview">
	<tr>
        <th>Name</th>
        <th>Vorname</th>
        <th>akademische Grade</th>
        <th>Tätigkeit</th>
    </tr>
    <tr>
        <td>#context['name']#</td>
        <td>#context['vorname']#</td>
		<td>#context['akagrad']#</td>
		<td>#context['taetigkeit']#</td>
    </tr>
</table>

<hr>

<div class="headline_small">Weiterbildungen</div>
<table class="overview">
	<tr>
        <th>Bezeichnung</th>
        <th>Von</th>
        <th>Bis</th>
        <th>Status</th>
    </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i in context@
        @entry_a = context[loop_i];@
        @if entry_a['id_w'] != null@	
        <tr>
            <td>#entry_a['bezeichnung_w']#</td>
            <td>#entry_a['von_w']#</td>
	        <td>#entry_a['bis_w']#</td>
	        <td>#entry_a['status']#</td>
        </tr>
        @endif@	
    @endfor@
</table>

<div>
    <button class="zurück_auswertung_mitarbeiter" id="idBackAuswertungMitarbeiter">Zurück</button>
</div>

<div> </div>
<!-- EOF -->
				
				