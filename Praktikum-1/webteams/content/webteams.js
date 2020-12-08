function confirmDelete_p (event_opl) {
	if ((event_opl.target.tagName.toLowerCase() == 'a'       ) &&
		(event_opl.target.className             == "clDelete")    ) {
	   // Ergänzung: Löschen von Einträgen
	   if(confirm('Sollen die Daten wirklich gelöscht werden?')){

	   } else {
		   event_opl.preventDefault();
	   }
	}
 }
 window.onload = function () {
	let body_o = document.getElementsByTagName('body')[0];
	body_o.addEventListener('click', confirmDelete_p, false);
 }