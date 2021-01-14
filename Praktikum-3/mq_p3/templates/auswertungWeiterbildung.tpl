<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Auswertung - Weiterbildung</div>
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
		@if entry_a['von_w'] != null@
      	<tr id="#entry_a['id_w']#">
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
<input type="hidden" id="action" name="action" value="weiterbildung" />

<div>
	<button class="buttons" id="anzeigen_auswertung_weiterbildung">Anzeigen</button>
</div>
<!-- EOF -->