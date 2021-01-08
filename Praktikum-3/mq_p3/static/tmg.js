//------------------------------------------------------------------------------
// Template-Manager
// - Laden und Bereitstellen von Template-Quellen
// - setzt evs.js und tco.js voraus
//------------------------------------------------------------------------------
// rev. 1, 21.11.2018, Bm
//------------------------------------------------------------------------------

'use strict'

if (APPUTIL == undefined) {
   var APPUTIL = {};
}

APPUTIL.TemplateManager_cl = class {
   constructor () {
      if (!APPUTIL.TemplateManager_cl.instance) {
         APPUTIL.TemplateManager_cl.instance = this;
         this.templates_o = {};
         this.compiled_o  = {};
         this.teCompiler_o = new APPUTIL.TemplateCompiler_cl();
      }
      return APPUTIL.TemplateManager_cl.instance;
   }
   init_px () {
      // Templates als Ressource anfordern und speichern
      let path_s = "/templates/";
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.request_px(path_s,
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.templates_o = data_o['templates'];
            APPUTIL.es_o.publish_px("templates.loaded", null);
         }.bind(this),
         function (responseText_spl) {
            APPUTIL.es_o.publish_px("templates.failed", responseText_spl);
         }
      );
   }
   get_px (name_spl) {
      if (name_spl in this.templates_o) {
         return this.templates_o[name_spl];
      } else {
         return null;
      }
   }
   execute_px (name_spl, data_opl) {
      var compiled_o = null;
      if (name_spl in this.compiled_o) {
         compiled_o = this.compiled_o[name_spl];
      } else {
         // Übersetzen und ausführen
         if (name_spl in this.templates_o) {
            this.teCompiler_o.reset_px();
            compiled_o = this.teCompiler_o.compile_px(this.templates_o[name_spl]);
            this.compiled_o[name_spl] = compiled_o;
         }
      }
      if (compiled_o != null) {
         return compiled_o(data_opl);
      } else {
         return null;
      }
   }
}

APPUTIL.createTemplateManager_px = function () {
   APPUTIL.tm_o = new APPUTIL.TemplateManager_cl();
   APPUTIL.tm_o.init_px();
}
// EOF