## coding: utf-8
<!DOCTYPE html>
<html>

   <head>
      <title>Web-Teams</title>
      <meta charset="UTF-8" />
      <script type="text/javascript" src="/webteams.js"></script>
   </head>
   
   <body>
      <%
         nr_i = 0
      %>
      <ul>
         % for key_s in data_o:
         <%
            nr_i += 1
         %>
         <li>
            Team ${nr_i}:
            <a href="/edit/${key_s}/?listform=${listform}">bearbeiten</a>                    <!-- Ergänzung: History "Funktion" -->
            <a href="/delete/${key_s}/?listform=${listform}" class="clDelete">löschen</a>    <!-- Ergänzung: Löschen von Einträgen / History "Funktion" -->
            <ul>
               <!-- Ergänzung: Zweites Team Mitglied anzeigen // Semesteranzahl hinzugfügen -->
               <li>${data_o[key_s][0]}, ${data_o[key_s][1]}, ${data_o[key_s][2]}, ${data_o[key_s][3]}</li>
               <li>${data_o[key_s][4]}, ${data_o[key_s][5]}, ${data_o[key_s][6]}, ${data_o[key_s][7]}</li>
               <br>
            </ul>
         </li>
         % endfor
      </ul>
      <div>
         <a href="/add/?listform=${listform}">erfassen</a>     <!-- Ergänzung: History "Funktion" -->
      </div>
      <div>
         <a href="/?listform=tabelle">Darstellung ändern</a>   <!-- Ergänzung: History "Funktion" -->
      </div>
   </body>

</html>