<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Auswertung - Weiterbildung - Detail</div>

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
        <tr>
            <td>#context['bezeichnung_w']#</td>
            <td>#context['von_w']#</td>
            <td>#context['bis_w']#</td>
            <td>#context['beschreibung_w']#</td>
    		<td>#context['maxteilnehmer_w']#</td>
    		<td>#context['minteilnehmer_w']#</td>
        </tr>
    </table>

<hr>

<div class="headline_small">Erfolgreiche Teilnehmer</div>
    <table class="overview">
    <tr>
        <th>Name</th>
        <th>Vorname</th>
        <th>akademische Grade</th>
        <th>Tätigkeit</th>
        <th>Status</th>
    </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i in context@
       @entry_a = context[loop_i];@
           <!-- Erfolgreiche Teilnehmer "rausfiltern"-->
         @if entry_a['status'] == "angemeldet"@
        <tr>
            <td>#entry_a['name']#</td>
            <td>#entry_a['vorname']#</td>
            <td>#entry_a['akagrad']#</td>
            <td>#entry_a['taetigkeit']#</td>
            <td>#entry_a['status']#</td>
        </tr>
    </table>

<div>
    <button class="buttons" id="idBack">Zurück</button>
</div>

<div> </div>
<!-- EOF -->
		