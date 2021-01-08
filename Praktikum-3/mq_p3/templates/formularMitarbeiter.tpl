<!-- Template -->
<!-- Contentbereich -->
<div class="headline">Formular - Mitarbeiter</div>

   <form class="formular" id="idForm">
         <input type="hidden" id="id" name="id" value="#context['id']#" />
         
      <div>
         <label for="name">Name</label>
         <input type="string" id="name" name="name" value="#context['name']#" />
      </div>

      <div>
         <label for="vorname">Vorname</label>
         <input type="string" id="vorname" name="vorname" value="#context['vorname']#" />
      </div>

      <div>
         <label for="akagrad">Akademischer Grad</label>
         <input type="string" id="akagrad" name="akagrad" value="#context['akagrad']#" />
      </div>

      </div>
         <label for="taetigkeit">Tätigkeit</label>
         <input type="string" id="taetigkeit" name="taetigkeit" value="#context['taetigkeit']#" />
      </div>

      <div>
         <button class="buttons" id="idBack">Zurück</button>
         <button class="buttons" id="idSave">Speichern</button>
      </div>
   </form>

   <input type="hidden" id="action" name="action" value="mitarbeiter" />

<div> </div>
<!-- EOF -->