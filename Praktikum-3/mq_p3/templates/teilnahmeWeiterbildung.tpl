<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Teilnahme - Weiterbildung</div>

<hr>
<div class="headline_small">Abgeschlossene/Laufende Weiterbildungen</div>
<table class="overview">
   	<tr>
		<th>Bezeichnung</th>
		<th>Von</th>
		<th>Bis</th>
		<th>Beschreibung</th>
		<th>max. Teilnehmer</th>
		<th>min. Teilnehmer</th>
		<th>Status</th>
	</tr>

   	@var entry_a;@
   	@var loop_i;@
   	@for loop_i in context@
      	@entry_a = context[loop_i];@

		@var anfang = entry_a['von_w'];@
		@var ende = entry_a['bis_w'];@
		@var status;@
		@if anfang <= currentDate@
			@if ende < currentDate@
				@status = "abgeschlossen";@
			@else:@
				@status = "laufend";@
			@endif@

      		<tr id="#entry_a['id']#">
				<td>#entry_a['bezeichnung_w']#</td>
        		<td>#entry_a['von_w']#</td>
        		<td>#entry_a['bis_w']#</td>
				<td>#entry_a['beschreibung_w']#</td>
				<td>#entry_a['maxteilnehmer_w']#</td>
				<td>#entry_a['minteilnehmer_w']#</td>
				<td>#status#</td>
      		</tr>
		@endif@
   	@endfor@
</table>

<hr>
<div class="headline_small">Geplante Weiterbildungen</div>
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
		@var status;@
		@if anfang > currentDate@
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

<input type="hidden" id="action" name="action" value="weiterbildung" />

<div>
	<button class="buttons" id="anzeigen_weiterbildung">Anzeigen</button>
</div>
<!-- EOF -->