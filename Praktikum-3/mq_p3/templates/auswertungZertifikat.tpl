<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Auswertung - Zertifikate</div>
<table class="overview">
   <tr>
		<th>Bezeichnung</th>
		<th>Beschreibung</th>
		<th>Berechtigt zu</th>
	</tr>
   @var entry_a;@
   @var loop_i;@
   @for loop_i in context@
      @entry_a = context[loop_i];@
      <!-- Zertifikate "rausfiltern"-->
         @if (entry_a['bezeichnung_z'] != null)@
         <tr id="#entry_a['id_z']#">
		      <td>#entry_a['bezeichnung_z']#</td>
            <td>#entry_a['beschreibung_z']#</td>
            <td>#entry_a['berechtigtzu_z']#</td>
         </tr>
      @endif@
   @endfor@
</table>
<input type="hidden" id="action" name="action" value="mitarbeiter" />

<div>
	<button class="buttons" id="anzeigen_auswertung_zertifikat">Anzeigen</button>
</div>
<!-- EOF -->