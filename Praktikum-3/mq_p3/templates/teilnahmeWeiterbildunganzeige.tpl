<!-- Template -->
<div class="headline"> Teilnahme - Weiterbildung - Detail</div>

<hr>

<div class="headline_small">Weiterbildung</div>
<table class="overview">
	<tr>
        <th>Bezeichnung</th>
        <th>Von</th>
        <th>Bis</th>
        <th>Beschreibung</th>
        <th>max. Teilnehmer</th>
        <th>min. Teilnehmer</th>
    </tr>
    <tr id="#context['id_w']#">
        <td id="weiid" data-value=#context['id_w']# hidden>#context['id_w']#</td>
        <td>#context['bezeichnung_w']#</td>
        <td>#context['von_w']#</td>
		<td>#context['bis_w']#</td>
		<td>#context['beschreibung_w']#</td>
        <td>#context['maxteilnehmer_w']#</td>
        <td>#context['minteilnehmer_w']#</td>
    </tr>
</table>

<hr>

<div class="headline_small">Teilnehmer</div>
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
            @if entry_a['id_m'] != null@
		        <tr id="#entry_a['id_m']#">
		        	<td>#entry_a['name']#</td>
                	<td>#entry_a['vorname']#</td>
                	<td>#entry_a['akagrad']#</td>
		        	<td>#entry_a['taetigkeit']#</td>
                </tr>		
            @endif@
	@endfor@							
</table>

<button class="erfolg" id="erfolgTeilnahme">Erfolg</button>
<button class="nichterfolg" id="nichterfolgTeilnahme">Nichterfolg</button>
<button class="abbruch" id="abbruchTeilnahme">Abbruch</button>

<!-- EOF -->