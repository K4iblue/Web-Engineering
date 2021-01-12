<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Teilnahme - Mitarbeiter</div>
<table class="overview">
   <tr>
		<th>Name</th>
		<th>Vorname</th>
		<th>Akademischer Grad</th>
		<th>Tätigkeit</th>
	</tr>
   @var entry_a;@
   @var loop_i;@
   @for loop_i in context@
      @entry_a = context[loop_i];@
      <tr id="#entry_a['id_m']#">
		   <td>#entry_a['name']#</td>
         <td>#entry_a['vorname']#</td>
         <td>#entry_a['akagrad']#</td>
		   <td>#entry_a['taetigkeit']#</td>
      </tr>
   @endfor@
</table>

<input type="hidden" id="action" name="action" value="mitarbeiter" />

<div>
	<button class="buttons" id="anzeigen_teilnahme_mitarbeiter">Anzeigen</button>
</div>
<!-- EOF -->