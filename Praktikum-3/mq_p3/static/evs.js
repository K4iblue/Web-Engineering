//------------------------------------------------------------------------------
// Event-Service: asynchroner Nachrichtenaustausch
//------------------------------------------------------------------------------
// rev. 1, 21.11.2018, Bm
//------------------------------------------------------------------------------

'use strict'

if (APPUTIL == undefined) {
   var APPUTIL = {};
}

//------------------------------------------------------------------------------
APPUTIL.EventService_cl = class {
//------------------------------------------------------------------------------
   constructor () {
      this.Data_o       = null;
      this.Subscriber_o = {};
      this.Method_o     = null;
   }

   subscribe_px (Subscriber_opl, Message_spl) {
      if (Message_spl in this.Subscriber_o) {
         // Message bekannt, Liste der Subscriber untersuchen
         if (this.Subscriber_o[Message_spl].indexOf(Subscriber_opl) == -1) {
            this.Subscriber_o[Message_spl].push(Subscriber_opl);
         }
      } else {
         // Message noch nicht vorhanden, neu eintragen
         this.Subscriber_o[Message_spl] = [Subscriber_opl];
      }
   }

   unSubscribe_px (Subscriber_opl, Message_spl) {
      if (Message_spl in this.Subscriber_o) {
         // Message bekannt, Liste der Subscriber untersuchen
         var Entry_a = this.Subscriber_o[Message_spl];
         var index_i = Entry_a.indexOf(Subscriber_opl);
         if (index_i >= 0) {
            // Eintrag entfernen
            Entry_a[index_i] = null;
            Entry_a = this.compact_p(Entry_a); // compact liefert Kopie!
            if (Entry_a.length == 0) {
               // keine Subscriber mehr, kann entfernt werden
               delete this.Subscriber_o[Message_spl];
            }
         }
      } else {
         // Message nicht vorhanden, falsche Anforderung
      }
   }

   publish_px (Message_spl, Data_opl) {
      console.info('es - publish ' + Message_spl);

      this.each_p(this.Subscriber_o, function (value_apl, key_spl) {
         // geliefert wird jeweils ein Wert, hier ein Array, und der Key
         if (key_spl == Message_spl) {
            // an alle Subscriber weitergeben
            this.each_p(value_apl, function (entry_opl, index_ipl) {
               // geliefert wird hier das Element und der Index
               this.defer_p(entry_opl.notify_px, entry_opl, Message_spl, Data_opl);
            });
         }
      })
   }

   defer_p (notifier_ppl, entry_opl, message_spl, data_opl) {
      return setTimeout(function() {
         return notifier_ppl.apply(entry_opl, [entry_opl, message_spl, data_opl]);
      }, 1);
   }

   each_p(object_opl, iterator) {
      for (var key_s in object_opl) {
         iterator.call(this, object_opl[key_s], key_s);
      }
   }

   findAll_p(object_opl, iterator) {
      var results = [];
      this.each_p(object_opl, function(value, index) {
         if (iterator.call(this, value, index)) {
            results.push(value);
         }
      });
      return results;
   }

   compact_p(object_opl) {
      return this.findAll_p(object_opl, function(value) {
         return value != null;
      });
   }

}
// EOF
