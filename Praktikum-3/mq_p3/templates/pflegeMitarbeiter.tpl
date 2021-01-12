<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Datenpflege - Mitarbeiter</div>
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
	<button class="buttons" id="erfassen_mitarbeiter">Erfassen</button>
	<button class="buttons" id="bearbeiten_mitarbeiter">Bearbeiten</button>
	<button class="buttons" id="anzeigen_mitarbeiter">Anzeigen</button>
	<button class="buttons" id="idDelete">Entfernen</button>
</div>
<!-- EOF -->