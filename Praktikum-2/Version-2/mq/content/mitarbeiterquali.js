function confirmDelete_p (event_opl) {
	// event_opl = event = click/focusout/keypress etc. Target = Event ansprechbar, tagName = div, a, input etc.
	// tagnames werden in Großbuchstaben gespeichert, deshalb tolowercase(). ==a = ist es ein Link? Wurde die clDelete mit übergeben?
	if ((event_opl.target.tagName.toLowerCase() == 'a'       ) &&	
		(event_opl.target.className             == "clDelete")    ) {

	   if(confirm('Sollen die Daten wirklich gelöscht werden?')){

	   } else {
		   event_opl.preventDefault();
	   }
	}
 }
 window.onload = function () {
	let body_o = document.getElementsByTagName('body')[0];
	//bei Webseite laden, click-Event wird definiert. Immer wenn auf was geklickt wird, wird confirmDelete_p aufgerufen.
	body_o.addEventListener('click', confirmDelete_p, false);
 }