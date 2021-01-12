<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Formular - Weiterbildung</div>

   <form class="formular" id="idForm">
         <input type="hidden" id="id" name="id" value="#context['id_w']#" />
         
      <div>
         <label for="bezeichnung_w">Bezeichnung</label>
         <input type="string" id="bezeichnung_w" name="bezeichnung_w" value="#context['bezeichnung_w']#" required />
      </div>

      <div>
         <label for="von_w">Von</label>
         <input type="date" id="von_w" name="von_w" value="#context['von_w']#" required />
      </div>

      <div>
         <label for="bis_w">Bis</label>
         <input type="date" id="bis_w" name="bis_w" value="#context['bis_w']#" required />
      </div>

      <div>
         <label for="beschreibung_w">Beschreibung</label>
         <input type="text" id="beschreibung_w" name="beschreibung_w" value="#context['beschreibung_w']#" required />
      </div>

      <div>
         <label for="maxteilnehmer_w">max. Teilnehmer</label>
         <input type="number" id="maxteilnehmer_w" name="maxteilnehmer_w" value="#context['maxteilnehmer_w']#" required />
      </div>

      <div>
         <label for="minteilnehmer_w">min. Teilnehmer</label>
         <input type="number" id="minteilnehmer_w" name="minteilnehmer_w" value="#context['minteilnehmer_w']#" required />
      </div>

      <hr>

      <div class="headline">Formular - Qualifikation</div>
      <div>
         <label for="bezeichnung_q">Bezeichnung</label>
         <input type="text" id="bezeichnung_q" name="bezeichnung_q" value="#context['bezeichnung_q']#" required />
      </div>

      <div>
         <label for="beschreibung_q">Beschreibung</label>
         <input type="text" id="beschreibung_q" name="beschreibung_q" value="#context['beschreibung_q']#" required />
      </div>
      
      <hr>

      <div class="headline">Formular - Zertifikate</div>
      <div>
         <label for="bezeichnung_z">Bezeichnung</label>
         <input type="text" id="bezeichnung_z" name="bezeichnung_z" value="#context['bezeichnung_z']#" />
      </div>

      <div>
         <label for="beschreibung_z">Beschreibung</label>
         <input type="text" id="beschreibung_z" name="beschreibung_z" value="#context['beschreibung_z']#" />
      </div>

      <div>
         <label for="berechtigtzu_z">berechtigt zu</label>
         <input type="text" id="berechtigtzu_z" name="berechtigtzu_z" value="#context['berechtigtzu_z']#" />
      </div>

      <div>
         <button class="buttons" id="idBack">Zurück</button>
         <button class="buttons" id="idSave">Speichern</button>
      </div>
   </form>

   <input type="hidden" id="action" name="action" value="weiterbildung" />

<div> </div>
<!-- EOF -->