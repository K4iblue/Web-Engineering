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
@var entry_a;@
@var loop_i;@
@for loop_i in context@
   @entry_a = context[loop_i];@
    <!-- Weiterbildungen "rausfiltern"-->
    @if entry_a['id_w'] != null@
        <tr>
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

<div class="headline_small">Erfolgreiche Teilnehmer</div>
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
            <tr>
                <td>#entry_a['name']#</td>
                <td>#entry_a['vorname']#</td>
            	<td>#entry_a['akagrad']#</td>
            	<td>#entry_a['taetigkeit']#</td>
            </tr>
        @endif@
    @endfor@
    </table>

<div>
    <button class="zurück_auswertung_weiterbildung" id="idBackAuswertungWeiterbildung">Zurück</button>
</div>

<div> </div>
<!-- EOF -->
		