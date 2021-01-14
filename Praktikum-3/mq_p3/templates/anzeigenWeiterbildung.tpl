<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Anzeige - Weiterbildung</div>
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
        @var entry_a;@
        @var loop_i;@
        @for loop_i in context@
            @entry_a = context[loop_i];@
            <!-- Weiterbildungen "rausfiltern"-->
            @if entry_a['bezeichnung_w'] != null@
                <td>#entry_a['bezeichnung_w']#</td>
                <td>#entry_a['von_w']#</td>
                <td>#entry_a['bis_w']#</td>
                <td>#entry_a['beschreibung_w']#</td>
		        <td>#entry_a['maxteilnehmer_w']#</td>
                <td>#entry_a['minteilnehmer_w']#</td>
            @endif@
        @endfor@  
    </tr>
</table>
<p><br>
<div class="headline">Qualifikation</div>
<table class="overview">
	<tr>
        <th>Bezeichnung</th>
        <th>Beschreibung</th>
	</tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i in context@
        @entry_a = context[loop_i];@
        <!-- Qualifikation "rausfiltern"-->
        @if entry_a['bezeichnung_q'] != null@
            <tr>
                <td>#entry_a['bezeichnung_q']#</td>
                <td>#entry_a['beschreibung_q']#</td>
            </tr>
        @endif@
    @endfor@  	
</table>
<p><br>
<div class="headline">Zertifikat</div>
<table class="overview">
	    <tr>
            <th>Bezeichnung</th>
            <th>Beschreibung</th>
            <th>berechtigt zu</th>
        </tr>
    @var entry_a;@
    @var loop_i;@
    @for loop_i in context@
        @entry_a = context[loop_i];@
        <!-- Zertifikat "rausfiltern"-->
        @if entry_a['bezeichnung_z'] != null@
            <tr>
                <td>#entry_a['bezeichnung_z']#</td>
                <td>#entry_a['beschreibung_z']#</td>
                <td>#entry_a['berechtigtzu_z']#</td>
            </tr>
        @endif@
    @endfor@ 	
</table>
<p><br>
<div class="headline">Teilnehmer</div>
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
    <button class="zurückweiterbildung" id="idBackweiterbildung">Zurück</button>
</div>

<div> </div>
<!-- EOF -->
		