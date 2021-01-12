<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Teilnahme - Mitarbeiter - Detail</div>

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
        <td id="mitid" data-value=#context['id']# hidden>#context['id']#</td>
        <td>#context['name']#</td>
        <td>#context['vorname']#</td>
		<td>#context['akagrad']#</td>
		<td>#context['taetigkeit']#</td>
    </tr>
</table>

<hr>

<div class="headline_small">Verfügbare - Weiterbildungen</div>
    <table class="overview">
        <tr>
            <th>Bezeichnung</th>
            <th>Von</th>
            <th>Bis</th>
            <th>Beschreibung</th>
            <th>max. Teilnehmer</th>
            <th>min. Teilnehmer</th>
        </tr>

        @var entry_a;@
   	    @var loop_i;@
   	    @for loop_i in context@
      	    @entry_a = context[loop_i];@

		    @var anfang = entry_a['von_w'];@
		    @var ende = entry_a['bis_w'];@
		    @if currentDate <= anfang@
                <tr id="#entry_a['id']#">
			        <td>#entry_a['bezeichnung_w']#</td>
        	        <td>#entry_a['von_w']#</td>
        	        <td>#entry_a['bis_w']#</td>
			        <td>#entry_a['beschreibung_w']#</td>
			        <td>#entry_a['maxteilnehmer_w']#</td>
			        <td>#entry_a['minteilnehmer_w']#</td>
                </tr>
            @endif@
        @endfor@
    </table>

<hr>

<div class="headline_small">Geplante - Weiterbildungen</div>
    <table class="overview">
        <tr>
            <th>Bezeichnung</th>
            <th>Von</th>
            <th>Bis</th>
            <th>Beschreibung</th>
            <th>max. Teilnehmer</th>
            <th>min. Teilnehmer</th>
        </tr>

        @var entry_a;@
   	    @var loop_i;@
   	    @for loop_i in context@
      	    @entry_a = context[loop_i];@

		    @var anfang = entry_a['von_w'];@
		    @var ende = entry_a['bis_w'];@
		    @if currentDate <= anfang@
                <tr id="#entry_a['id']#">
			        <td>#entry_a['bezeichnung_w']#</td>
        	        <td>#entry_a['von_w']#</td>
        	        <td>#entry_a['bis_w']#</td>
			        <td>#entry_a['beschreibung_w']#</td>
			        <td>#entry_a['maxteilnehmer_w']#</td>
			        <td>#entry_a['minteilnehmer_w']#</td>
                </tr>
            @endif@
        @endfor@
    </table>

    <div>
        <button class="buttons" id="idSaveTeilnahme">Anmelden</button>
        <button class="buttons" id="idDeleteTeilnahme">Stornieren</button>
    </div>   
<!-- EOF -->