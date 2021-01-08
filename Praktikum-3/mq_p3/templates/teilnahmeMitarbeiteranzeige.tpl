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
        <td>#context['name']#</td>
        <td>#context['vorname']#</td>
		<td>#context['akagrad']#</td>
		<td>#context['taetigkeit']#</td>
    </tr>
</table>

<hr>

<div class="headline_small">Angebot - Weiterbildungen</div>
    <table class="overview">
        <tr>
            <th>Bezeichnung</th>
            <th>Von</th>
            <th>Bis</th>
            <th>Beschreibung</th>
            <th>max. Teilnehmer</th>
            <th>min. Teilnehmer</th>
        </tr>

        <!-- TODO: Schleife über alle Weiterbildungen, wo der Mitarbeiter eingeschrieben ist-->
        <tr>
            <td>TODO</td>
            <td>TODO</td>
            <td>TODO</td>
            <td>TODO</td>
            <td>TODO</td>
            <td>TODO</td>
        </tr>
    </table>

<hr>

<div class="headline_small">Abgeschlosse/Geplante - Weiterbildungen</div>
<table class="overview">
    <tr>
        <th>Bezeichnung</th>
        <th>Von</th>
        <th>Bis</th>
        <th>Beschreibung</th>
        <th>max. Teilnehmer</th>
        <th>min. Teilnehmer</th>
    </tr>

    <!-- TODO: Schleife über alle geplanten Weiterbildungen und abgeschlossenen (?), wo der Mitarbeiter NICHT eingeschrieben ist-->
    <tr>
        <td>TODO</td>
        <td>TODO</td>
        <td>TODO</td>
        <td>TODO</td>
        <td>TODO</td>
        <td>TODO</td>
    </tr>
</table>

<div> </div>