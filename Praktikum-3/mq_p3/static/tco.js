//------------------------------------------------------------------------------
// Template-Engine: Compiler
//------------------------------------------------------------------------------
// rev. 1, 21.11.2018, Bm
//------------------------------------------------------------------------------

'use strict'

if (APPUTIL == undefined) {
   var APPUTIL = {};
}

APPUTIL.Generator_cl = class {
   constructor () {
      this.reset_px();
   }
   reset_px () {
      this.code_a = ['var result_a = [];\n'];
   }
   write_px (text_spl) {
      // Escape-Zeichen bei Strings ergänzen
      var text_s = text_spl.replace(/"/g, '\\"');
      text_s = text_s.replace(/'/g, "\\'");
      this.code_a.push('result_a.push("' + text_s + '");\n');
   }
   code_px (code_spl) {
      if (code_spl.startsWith('if')) {
         this.code_a.push('if (' + code_spl.substr(2) + ') {\n');
      } else if (code_spl.startsWith('else')) {
         this.code_a.push('} else {\n');
      } else if (code_spl.startsWith('endif')) {
         this.code_a.push('}\n');
      } else if (code_spl.startsWith('for')) {
         this.code_a.push('for (' + code_spl.substr(3) + ') {\n');
      } else if (code_spl.startsWith('endfor')) {
         this.code_a.push('}\n');
      } else if (code_spl.startsWith('include')) {
         // Aufbau: include template data-object
         let parts_a = code_spl.split(' '); // einfache Lösung
         this.code_a.push('result_a.push(new APPUTIL.TemplateManager_cl().execute_px("' + parts_a[1] + '", ' + parts_a[2] + '));\n');
      } else {
         this.code_a.push(code_spl + '\n');
      }
   }
   substitute_px (subst_spl) {
      let value_s = subst_spl == null ? '' : String(subst_spl);
      this.code_a.push('result_a.push(' + value_s + ');\n');
   }
   generate_px () {
      var result_s = this.code_a.join('') + ' return result_a.join("");';
      var f_o = new Function ('context', result_s);
      return f_o;
   }
}

APPUTIL.TemplateCompiler_cl = class {
   constructor () {
      this.gen_o = new APPUTIL.Generator_cl();
      this.reset_px();
   }
   reset_px () {
      this.gen_o.reset_px();
      this.preservePreWS_b = false;
      this.preservePostWS_b = false;
   }
   setPreWS_px (on_bpl) {
      if ((on_bpl == undefined) || (on_bpl == false)) {
         this.preservePreWS_b = false;
      } else {
         this.preservePreWS_b = true;
      }
   }
   setPostWS_px (on_bpl) {
      if ((on_bpl == undefined) || (on_bpl == false)) {
         this.preservePostWS_b = false;
      } else {
         this.preservePostWS_b = true;
      }
   }
   compile_px (source_spl) {
      var state_i = 0;
      var pos_i = 0;
      var len_i = source_spl.length;
      var text_s = '';
      var code_s = '';
      var subst_s = '';
      this.gen_o.reset_px();

      var doubletest_f = function (char_spl) {
         var status_b = false;
         if ((pos_i + 1) < len_i) {
            if ((source_spl[pos_i] == char_spl) && (source_spl[pos_i+1] == char_spl)) {
               status_b = true;
            }
         }
         return status_b;
      }

      while (pos_i < len_i) {
         switch (state_i) {
         case 0:
            // outside
            if (source_spl[pos_i] == '@') { // ECMA 5!
               if (doubletest_f('@') == false) {
                  state_i = 2;
                  code_s = '';
               } else {
                  // als normales Zeichen verarbeiten, ein Zeichen überlesen
                  state_i = 1;
                  text_s = '@';
                  pos_i++;
               }
            } else if (source_spl[pos_i] == '#') {
               if (doubletest_f('#') == false) {
                  state_i = 3;
                  subst_s = '';
               } else {
                  // als normales Zeichen verarbeiten, ein Zeichen überlesen
                  state_i = 1;
                  text_s = '#';
                  pos_i++;
               }
            } else if ((source_spl[pos_i] == ' ') || (source_spl[pos_i] == '\t')) {
               state_i = 4;
               text_s = '';
               pos_i--; // Zeichen erneut verarbeiten
            } else {
               state_i = 1;
               text_s = '';
               pos_i--; // Zeichen erneut verarbeiten
            }
            break;
         case 1:
            // inText
            if (source_spl[pos_i] == '@') {
               if (doubletest_f('@') == false) {
                  // Textende, neuer Code
                  state_i = 0;
                  this.gen_o.write_px(text_s);
                  pos_i--; // Zeichen erneut verarbeiten
               } else {
                  // als normales Zeichen verarbeiten, ein Zeichen überlesen
                  text_s += '@';
                  pos_i++;
               }
            } else if (source_spl[pos_i] == '#') {
               if (doubletest_f('#') == false) {
                  // Textende, neue Substitution
                  state_i = 0;
                  this.gen_o.write_px(text_s);
                  pos_i--; // Zeichen erneut verarbeiten
                  // Textende, neuer Code
               } else {
                  // als normales Zeichen verarbeiten, ein Zeichen überlesen
                  text_s += '#';
                  pos_i++;
               }
            } else if ((source_spl[pos_i] == ' ') || (source_spl[pos_i] == '\t')) {
               // Textende
               state_i = 0;
               this.gen_o.write_px(text_s);
               pos_i--; // Zeichen erneut verarbeiten
            } else {
               // sammeln
               if ((source_spl[pos_i] != '\n') && (source_spl[pos_i] != '\r')) {
                  text_s += source_spl[pos_i];
               } else if (source_spl[pos_i] == '\n') {
                  text_s += '\\n';
               } else {
                  text_s += '\\r';
               }
            }
            break;
         case 2:
            // inCode
            if (source_spl[pos_i] == '@') {
               if (doubletest_f('@') == false) {
                  // zu Ende, erzeugen
                  this.gen_o.code_px(code_s);
                  state_i = 5;  //0
               } else {
                  // als normales Zeichen verarbeiten, ein Zeichen überlesen
                  code_s += '@';
                  pos_i++;
               }
            } else {
               // sammeln
               code_s += source_spl[pos_i];
            }
            break;
         case 3:
            // inSubst
            // Verdopplung # hier nicht zulässig!
            if (source_spl[pos_i] == '#') {
               // zu Ende, erzeugen
               this.gen_o.substitute_px(subst_s);
               state_i = 0;
            } else {
               // sammeln
               subst_s += source_spl[pos_i];
            }
            break;
         case 4:
            // pre-code-whitespace
            switch (source_spl[pos_i]) {
            case ' ':
            case '\t':
               // sammeln
               text_s += source_spl[pos_i];
               break;
            default:
               state_i = 0;
               if (source_spl[pos_i] != '@') {
                  this.gen_o.write_px(text_s);
               } else {
                  if (doubletest_f('@') == false) {
                     // Whitespace vor Code-Beginn erkannt
                     if (this.preservePreWS_b == true) {
                        // trotzdem ausgeben
                        this.gen_o.write_px(text_s);
                     }
                  } // ansonsten wie normales Zeichen behandeln
               }
               pos_i--; // Zeichen erneut verarbeiten
            }
            break;
         case 5:
            // post-code-whitespace
            switch (source_spl[pos_i]) {
            case '\n':
               text_s += '\\n';
               state_i = 0;
               break;
            case '\r':
               text_s += '\\r';
               state_i = 0;
               break;
            case ' ':
            case '\t':
               // ggf. sammeln
               text_s += source_spl[pos_i];
               break;
            default:
               // Whitespace nach Code erkannt
               if (this.preservePostWS_b == true) {
                  // trotzdem ausgeben
                  this.gen_o.write_px(text_s);
               }
               state_i = 0;
               pos_i--; // Zeichen erneut verarbeiten
            }
            break;
         }
         pos_i++;
      }
      // welcher Zustand liegt abschließend vor?
      if (state_i == 1) {
         this.gen_o.write_px(text_s);
      } else if (state_i == 2) {
         this.gen_o.code_px(code_s);
      } else if (state_i == 3) {
         this.gen_o.substitute_px(subst_s);
      } else if (state_i == 4) {
         if (this.preservePreWS_b == true) {
            this.gen_o.write_px(text_s);
         }
      } else if (state_i == 5) {
         if (this.preservePostWS_b == true) {
            this.gen_o.write_px(text_s);
         }
      }

      return this.gen_o.generate_px();
   }
}
// EOF