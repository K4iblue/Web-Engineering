<!-- Template -->
<div class="headline"> Startseite</div>

<div>
	@var entry_a;@
	@var status_geplant = 0;@
	@var status_laufend = 0;@
	@var status_abgeschlossen = 0;@
	@var loop_i;@
	@for loop_i in context@
	   @entry_a = context[loop_i];@
	
	 @var anfang = entry_a['von_w'];@
	 @var ende = entry_a['bis_w'];@
	 @var status;@
	 @if anfang <= currentDate@
		 @if ende < currentDate@
			 @status_abgeschlossen++;@ <!-- Anzahl "abgeschlossen" erhöhen -->
		 @else:@
			 @status_laufend++;@ <!-- Anzahl "laufend" erhöhen -->
		 @endif@

	@if anfang > currentDate@
		@status_geplant++;@	<!-- Anzahl "geplant" erhöhen -->
	@endif@

	<table class="overview">
		<tr>
			<th>Anzahl Mitarbeiter</th>
			<th>Anzahl Weiterbildungen geplant</th>
			<th>Anzahl Weiterbildungen laufend</th>
			<th>Anzahl Weiterbildungen abgeschlossen</th>
			<th>Anzahl Teilnahmen</th>
		</tr>

		<tr>
			<td>TODO</td>
			<td>status_geplant</td>
			<td>status_laufend</td>
			<td>status_abgeschlossen</td>
			<td>TODO</td>
		</tr>
	</table>
</div>

<div> </div>