function confirmDelete_p (event_opl) {
	if ((event_opl.target.tagName.toLowerCase() == 'a'       ) &&	//event_opl = event = click/focusout/keypress etc. Target = Event ansprechbar, tagName = div, a, input etc. (tagnames werden in Großbuchstaben gespeichert, deshalb tolowercase(). ==a = ist es ein Link? Wurde die clDelete mit übergeben?)
		(event_opl.target.className             == "clDelete")    ) {
	   // Ergänzung: Löschen von Einträgen
	   if(confirm('Sollen die Daten wirklich gelöscht werden?')){

	   } else {
		   event_opl.preventDefault();
	   }
	}
 }

 function confirmStorno_p (event_opl) {
	if ((event_opl.target.tagName.toLowerCase() == 'a'       ) &&	//event_opl = event = click/focusout/keypress etc. Target = Event ansprechbar, tagName = div, a, input etc. (tagnames werden in Großbuchstaben gespeichert, deshalb tolowercase(). ==a = ist es ein Link? Wurde die clDelete mit übergeben?)
		(event_opl.target.className             == "clstorno")    ) {
	   // Ergänzung: Löschen von Einträgen
	   if(confirm('Soll die Weiterbildung wirklich storniert werden?')){

	   } else {
		   event_opl.preventDefault();
	   }
	}
}

 window.onload = function () {
	let body_o = document.getElementsByTagName('body')[0];
	body_o.addEventListener('click', confirmDelete_p, false);	//bei Webseite laden, click-Event wird definiert. Immer wenn auf was geklickt wird, wird confirmDelete_p aufgerufen.
	body_o.addEventListener('click', confirmStorno_p, false);
}