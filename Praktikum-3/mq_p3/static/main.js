//------------------------------------------------------------------------------
//Demonstrator evs/tco/tmg
//------------------------------------------------------------------------------
'use strict'

// Aktuelles Datum
var currentDate = new Date();
var dd = String(currentDate.getDate()).padStart(2, '0');
var mm = String(currentDate.getMonth()+1).padStart(2, '0'); // Januar ist 0
var yyyy = currentDate.getFullYear();
currentDate = yyyy + '-' + mm + '-' + dd; // Heutiges Datum

//------------------------------------------------------------------------------
class FormView_cl {
//------------------------------------------------------------------------------

   constructor (el_spl, template_spl, action) {
      this.el_s = el_spl;
      this.template_s = template_spl;
	   this.action = action;
   }
   render_px (id_spl, typ) {

      // Daten anfordern
      let path_s = "/app/" + this.action + "/" + id_spl;
	   if(typ != ""){
		   path_s = path_s + "/" + typ;
	   }
	   console.log("render_px | path_s = " + path_s);
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.request_px(path_s,
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("Form - render failed");
         }
      );
   }

   doRender_p (data_opl) {

      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }

   configHandleEvent_p () {

      let el_o = document.querySelector("form");
      if (el_o != null) {
		   console.log("c: this.action = " + this.action);
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }

   handleEvent_p (event_opl) {

      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }
      
	   else if (event_opl.target.id == "idSave") {

		   let data ={};
         var form = document.getElementById("idForm");
         var inputs = form[0].getElementsByTagName("input");
         var input_action = document.getElementById("action");
         
         for (var i = 0; i< inputs.length; i++){

            data[inputs[i].name] = inputs[i].value;
         }
		   let json = JSON.stringify(data);
		 
		   var para = new URLSearchParams(new FormData(form));
		   let url = "/app/" + input_action.value + "/";

		   var type = "POST";
		   if(form[0].value != ''){

			   type = "PUT";
		   }
		 
		   console.log("Save: url = " + url);
		   console.log("Save: form[0].value = " + form[0].value);
		 
		   fetch(url, {method: type, body: para, header: {"Content-type": "application/x-www-form-urlencoded"}}).then(res => res.json())
		   .then(response => console.log("Success ID = ", response, alert("speichern erfolgreich"), APPUTIL.es_o.publish_px("app.cmd", ["input_action", response])))
		   .catch(error => console.error("Error", error));
		 
		   console.log("handleEvent_p() -> idSave 2");
		   APPUTIL.es_o.publish_px("app.cmd", ["idSave", null]);
		   event_opl.preventDefault();
	   }
	}
}

//------------------------------------------------------------------------------
class AnzeigenView_cl {
//------------------------------------------------------------------------------
   
   constructor (el_spl, template_spl, action) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.action = action;
   }

   render_px (id_spl, typ) {
   
      // Daten anfordern
      let path_s = "/app/" + this.action + "/" + id_spl;
      if(typ != ""){
         path_s = path_s + "/" + typ;
      }
      console.log("render_px | path_s = " + path_s);
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.request_px(path_s,
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("Anzeigen - render failed");
         }
      );
   }
   
   doRender_p (data_opl) {
   
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   
   configHandleEvent_p () {
   
      let el_o = document.querySelector("form");
      if (el_o != null) {
         console.log("c: this.action = " + this.action);
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   
   handleEvent_p (event_opl) {
   
      if (event_opl.target.id == "idBack") {
         APPUTIL.es_o.publish_px("app.cmd", ["idBack", null]);
         event_opl.preventDefault();
      }
   }
}

//------------------------------------------------------------------------------
class ListView_cl {
//------------------------------------------------------------------------------

   constructor (el_spl, template_spl, action) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
	   this.action = action;
	   console.log("lv: this.action = " + this.action);
   }
   render_px (id) {

      // Daten anfordern
      let path_s = "/app/" + this.action + "/";
	   console.log("render_px: id = " + id);
	   if (id != null && id != -1){ //ID wird z.B. bei der komponente benötigt für die Projekt ID / Angestellten-typ
		   path_s = path_s + null + "/" + id + "/";
	   }
	   console.log("path_s = " + path_s);
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.request_px(path_s,
         function (responseText_spl) {
			//alert("responseText_spl = " responseText_spl);
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("List - render failed ");
			//alert("responseText_spl = " responseText_spl);
         }
      );

   }
   doRender_p (data_opl) {

      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }

   configHandleEvent_p () {

      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }

   handleEvent_p (event_opl) {

      if (event_opl.target.tagName.toUpperCase() == "TD") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {

            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      }

      //Löschen
	   else if (event_opl.target.id == "idDelete") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else {

            APPUTIL.es_o.publish_px("app.cmd", ["idDelete", elx_o.id] );
         }
      }

      //Anzeigen Mitarbeiter
	   else if (event_opl.target.id == "anzeigen_mitarbeiter") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("anzeigen_mitarbeiter");
            APPUTIL.es_o.publish_px("app.cmd", ["anzeigen_mitarbeiter", elx_o.id] );
         }
      }

      //Auswertung Mitarbeiter Anzeigen
	   else if (event_opl.target.id == "anzeigen_auswertung_mitarbeiter") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("anzeigen_auswertung_mitarbeiter");
            APPUTIL.es_o.publish_px("app.cmd", ["anzeigen_auswertung_mitarbeiter", elx_o.id] );
         }
      }

      //Auswertung Weiterbildung Anzeigen
	   else if (event_opl.target.id == "anzeigen_auswertung_weiterbildung") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("anzeigen_auswertung_weiterbildung");
            APPUTIL.es_o.publish_px("app.cmd", ["anzeigen_auswertung_weiterbildung", elx_o.id] );
         }
      }

      //Teilnahme Mitarbeiter Anzeigen
	   else if (event_opl.target.id == "anzeigen_teilnahme_mitarbeiter") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("anzeigen_teilnahme_mitarbeiter");
            APPUTIL.es_o.publish_px("app.cmd", ["anzeigen_teilnahme_mitarbeiter", elx_o.id] );
         }
      }

      //Erfassen Mitarbeiter
	   else if (event_opl.target.id == "erfassen_mitarbeiter") {

		   console.log("erfassen_mitarbeiter");
		   APPUTIL.es_o.publish_px("app.cmd", ["form_mitarbeiter", null] );
      }
      
      //Liste anzeigen aller Mitarbeiter
	   else if (event_opl.target.id == "mitarbeiter") {

		   APPUTIL.es_o.publish_px("app.cmd", ["mitarbeiter", null] );
      }
      
      //Bearbeiten Mitarbeiter
      else if (event_opl.target.id == "bearbeiten_mitarbeiter") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("bearbeiten_mitarbeiter");
            APPUTIL.es_o.publish_px("app.cmd", ["form_mitarbeiter", elx_o.id] );
         }
      }

      //Anzeigen Weiterbildung
	   else if (event_opl.target.id == "anzeigen_weiterbildung") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("anzeigen_weiterbildung");
            APPUTIL.es_o.publish_px("app.cmd", ["anzeigen_weiterbildung", elx_o.id] );
         }
      }

      //Erfassen Weiterbildung
	   else if (event_opl.target.id == "erfassen_weiterbildung") {

		   console.log("erfassen_weiterbildung");
		   APPUTIL.es_o.publish_px("app.cmd", ["form_weiterbildung", null] );
      }

      //Liste anzeigen aller Weiterbildungen
	   else if (event_opl.target.id == "weiterbildung") {

		   APPUTIL.es_o.publish_px("app.cmd", ["weiterbildung", null] );
      }

      //Bearbeiten Weiterbildung
      else if (event_opl.target.id == "bearbeiten_weiterbildung") {

         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {

            alert("Bitte zuerst einen Eintrag auswählen!");
         }else {

            console.log("bearbeiten_weiterbildung");
            APPUTIL.es_o.publish_px("app.cmd", ["form_weiterbildung", elx_o.id] );
         }
      }
   }
}

//------------------------------------------------------------------------------
class SideBar_cl {
//------------------------------------------------------------------------------

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }

   render_px (data_opl) {

      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }

   configHandleEvent_p () {

      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }

   handleEvent_p (event_opl) {

      let cmd_s = event_opl.target.dataset.action;
      APPUTIL.es_o.publish_px("app.cmd", [cmd_s, null]);
   }
}

class Application_cl {

   constructor () {

      APPUTIL.es_o.subscribe_px(this, "templates.loaded");
      APPUTIL.es_o.subscribe_px(this, "templates.failed");
      APPUTIL.es_o.subscribe_px(this, "app.cmd");

      // Design
      this.sideBar_o = new SideBar_cl("aside", "sidebar.tpl");  // Sidebar (Menü) laden
      
      // Pflege Mitarbeiter
      this.listView_mitarbeiter_o = new ListView_cl("main", "pflegeMitarbeiter.tpl", "mitarbeiter");     //Anzeigen aller Mitarbeiter
      this.FormView_mitarbeiter_o = new FormView_cl("main", "formularMitarbeiter.tpl", "mitarbeiter");   //Erfassen/Bearbeiten neuer Mitarbeiter
      this.AnzeigenView_mitarbeiter_o = new AnzeigenView_cl("main", "anzeigenMitarbeiter.tpl", "mitarbeiter"); //Anzeigen Mitarbeiter

      // Pflege Weiterbildung
      this.listView_weiterbildung_o = new ListView_cl("main", "pflegeWeiterbildung.tpl", "weiterbildung");     //Anzeigen aller Weiterbildungen
      this.FormView_weiterbildung_o = new FormView_cl("main", "formularWeiterbildung.tpl", "weiterbildung");   //Erfassen/Bearbeiten neuer Weiterbildungen
      this.AnzeigenView_weiterbildung_o = new AnzeigenView_cl("main", "anzeigenWeiterbildung.tpl", "weiterbildung"); //Anzeigen Mitarbeiter
      
      // Teilnahme Mitarbeiter
      this.listView_teilnahme_mitarbeiter_o = new ListView_cl("main", "teilnahmeMitarbeiter.tpl", "mitarbeiter");     //Anzeigen aller Mitarbeiter
      this.AnzeigenView_teilnahme_mitarbeiter_o = new AnzeigenView_cl("main", "teilnahmeMitarbeiteranzeige.tpl", "mitarbeiter");

      // Teilnahme Weiterbildung
      this.listView_teilnahme_weiterbildung_o = new ListView_cl("main", "teilnahmeWeiterbildung.tpl", "weiterbildung");     //Anzeigen aller Weiterbildungen
   
      // Auswertung Mitarbeiter
      this.listView_auswertung_mitarbeiter_o = new ListView_cl("main", "auswertungMitarbeiter.tpl", "mitarbeiter");     //Anzeigen aller Mitarbeiter
      this.AnzeigenView_auswertung_mitarbeiter_o = new AnzeigenView_cl("main", "auswertungMitarbeiteranzeigen.tpl", "mitarbeiter"); //Anzeigen Mitarbeiter

      // Auswertung Weiterbildung
      this.listView_auswertung_weiterbildung_o = new ListView_cl("main", "auswertungWeiterbildung.tpl", "weiterbildung");     //Anzeigen aller Weiterbildung
      this.AnzeigenView_auswertung_weiterbildung_o = new AnzeigenView_cl("main", "auswertungWeiterbildunganzeigen.tpl", "weiterbildung"); //Anzeigen Weiterbildung
   }
   
   notify_px (self, message_spl, data_opl) {

      switch (message_spl) {

      case "templates.failed":
         alert("Vorlagen konnten nicht geladen werden.");
         break;

      case "templates.loaded":
         // Templates stehen zur Verfügung, Bereiche mit Inhalten füllen
         let markup_s;
         let el_o;
         markup_s = APPUTIL.tm_o.execute_px("header.tpl", null);
         el_o = document.querySelector("header");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         let nav_a = [
            ["home", "Startseite"],
            ["mitarbeiter", "Pflege: Mitarbeiter"],
            ["weiterbildung", "Pflege: Weiterbildung"],
            ["teilnahme_mitarbeiter", "Teilnahme: Mitarbeiter"],
            ["teilnahme_weiterbildung", "Teilnahme: Weiterbildung"],
            ["auswertung_mitarbeiter", "Auswertung: Mitarbeiter"],
            ["auswertung_weiterbildung", "Auswertung: Weiterbildung"],
            ["auswertung_zertifikate", "Auswertung: Zertifikate"]
         ];
         self.sideBar_o.render_px(nav_a);
         markup_s = APPUTIL.tm_o.execute_px("startseite.tpl", null);
         el_o = document.querySelector("main");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         break;

      case "app.cmd":
         // hier müsste man überprüfen, ob der Inhalt gewechselt werden darf
         switch (data_opl[0]) {

         case "home":
            let markup_s = APPUTIL.tm_o.execute_px("startseite.tpl", null);
            let el_o = document.querySelector("main");
            if (el_o != null) {
               el_o.innerHTML = markup_s;
            }
            break;


         // Mitarbeiter
         case "mitarbeiter":
            this.listView_mitarbeiter_o.render_px(data_opl[1]);
            break;

         case "form_mitarbeiter":
            this.FormView_mitarbeiter_o.render_px(data_opl[1]);
            break;

         case "anzeigen_mitarbeiter":
            this.AnzeigenView_mitarbeiter_o.render_px(data_opl[1]);
            break;


         // Weiterbildung
         case "weiterbildung":
            this.listView_weiterbildung_o.render_px(data_opl[1]);
            break;

         case "form_weiterbildung":
            this.FormView_weiterbildung_o.render_px(data_opl[1]);
            break;

         case "anzeigen_weiterbildung":
            this.AnzeigenView_weiterbildung_o.render_px(data_opl[1]);
            break;


         // Teilnahme Mitarbeiter
         case "teilnahme_mitarbeiter":
            this.listView_teilnahme_mitarbeiter_o.render_px(data_opl[1]);
            break;

         // Teilnahme Mitarbeiter Anzeigen
         case "anzeigen_teilnahme_mitarbeiter":
            this.AnzeigenView_teilnahme_mitarbeiter_o.render_px(data_opl[1]);
            break;


         // Teilnahme Weiterbildung
         case "teilnahme_weiterbildung":
            this.listView_teilnahme_weiterbildung_o.render_px(data_opl[1], currentDate);
            break;


         // Auswertung Mitarbeiter
         case "auswertung_mitarbeiter":
            this.listView_auswertung_mitarbeiter_o.render_px(data_opl[1]);
            break;

         case "anzeigen_auswertung_mitarbeiter":
            this.AnzeigenView_auswertung_mitarbeiter_o.render_px(data_opl[1]);
            break;

         // Auswertung Weiterbildung
         case "auswertung_weiterbildung":
            this.listView_auswertung_weiterbildung_o.render_px(data_opl[1]);
            break;

         case "anzeigen_auswertung_weiterbildung":
            this.AnzeigenView_auswertung_weiterbildung_o.render_px(data_opl[1]);
            break;

         case "idBack":
			   var input_action = document.getElementById("action");
			   console.log("action = " + input_action.value);
            APPUTIL.es_o.publish_px("app.cmd", [input_action.value, null]);
            break;

		   case "idDelete":
			   if(confirm("Entfernen?")){
				   var input_action = document.getElementById("action");
				   var url = "/app/" + input_action.value + "/" + data_opl[1];
				   fetch(url, {
					   method: 'DELETE',
					   headers: {
						   'Content-Type': 'application/json'
					   }
				   })
				   APPUTIL.es_o.publish_px("app.cmd", [input_action.value, null]);
			   }
			   break;
         }
         break;
      }
   }
}

window.onload = function () {
   APPUTIL.es_o = new APPUTIL.EventService_cl();
   var app_o = new Application_cl();
   APPUTIL.createTemplateManager_px();
}