<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Datenpflege - Weiterbildung</div>
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
      <tr id="#entry_a['id_w']#">
		 <td>#entry_a['bezeichnung_w']#</td>
         <td>#entry_a['von_w']#</td>
         <td>#entry_a['bis_w']#</td>
		 <td>#entry_a['beschreibung_w']#</td>
		 <td>#entry_a['maxteilnehmer_w']#</td>
		 <td>#entry_a['minteilnehmer_w']#</td>
      </tr>
   @endfor@
</table>
<input type="hidden" id="action" name="action" value="weiterbildung" />

<div>
	<button class="buttons" id="erfassen_weiterbildung">Erfassen</button>
	<button class="buttons" id="bearbeiten_weiterbildung">Bearbeiten</button>
	<button class="buttons" id="anzeigen_weiterbildung">Anzeigen</button>
	<button class="buttons" id="idDelete">Entfernen</button>
</div>
<!-- EOF -->