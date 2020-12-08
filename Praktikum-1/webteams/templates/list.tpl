## coding: utf-8
<!DOCTYPE html>
<html>

   <head>
      <title>Web-Teams</title>
      <meta charset="UTF-8" />
      <script type='text/javascript' src='/webteams.js'></script>       <!-- Ergänzung: Löschen von Einträgen -->
      <style> @import "/webteams.css"; </style>                         <!-- Ergänzung: CSS einbinden-->
   </head>

   <body>
      <table id="overview"> <!-- Ergänzung: CSS "id"-->
         <tr>
            <!-- Ergänzung: Zweites Team Mitglied anzeigen // Semesteranzahl hinzugfügen -->
            <th>Name (1)</th><th>Vorname (1)</th><th>Matr.-Nr. (1)</th><th>Semester (1)</th>
            <th>Name (2)</th><th>Vorname (2)</th><th>Matr.-Nr. (2)</th><th>Semester (2)</th>
            <th>Aktion</th>
         </tr>
         % for key_s in data_o:
         <tr>
            <!-- Ergänzung: Zweites Team Mitglied anzeigen // Semesteranzahl hinzugfügen -->
            <td>${data_o[key_s][0]}</td>
            <td>${data_o[key_s][1]}</td>
            <td>${data_o[key_s][2]}</td>
            <td>${data_o[key_s][3]}</td>

            <td>${data_o[key_s][4]}</td>
            <td>${data_o[key_s][5]}</td>
            <td>${data_o[key_s][6]}</td>
            <td>${data_o[key_s][7]}</td>
            <td>
               <a href="/edit/${key_s}/?listform=${listform}" id="buttons">bearbeiten</a>                   <!-- Ergänzung: History "Funktion" -->
               <a href="/delete/${key_s}/?listform=${listform}" class="clDelete" id="buttons">löschen</a>   <!-- Ergänzung: Löschen von Einträgen -->
            </td>
         </tr>
         % endfor
      </table>
      <div>
         <a href="/add/?listform=${listform}" id="erfassen">erfassen</a>   <!-- Ergänzung: CSS "id"-->
         <a href="/?listform=liste" id="erfassen">Darstellung ändern</a>     <!-- Ergänzung: History "Funktion" -->
      </div>
   </body>
   
</html>