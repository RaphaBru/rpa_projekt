# Willkommen auf dem GitHub unseres RPA-Projekts!

Dieses Repository wurde einerseits für die Versionenkontrolle und die kollaborative Mitarbeit des Teams genutzt und dient andererseits als Wekzeug zur Präsentation und Abgabe der Resultate.

Die funktionierende Automatisierung wird in einer Demo vorgestellt:
[Link zum Demo-Video](https://photos.onedrive.com/share/3083D8FE9F20F472!600763?cid=3083D8FE9F20F472&resId=3083D8FE9F20F472!600763&authkey=!AGHJWZlXzTnmB2M&ithint=video&e=FbJku4)

Die fünf Hauptaufgaben der Automatisierung wurden in Separaten Workflow-Sequenzen implementiert. Der Main-Workflow ruft die fünf Frequenzen auf.

**Sequenz 01 "get_pdf"** - Webscraping aller PDF-Rechnungen.  
**Sequenz 02 "read_pdf"** - Extraktion der relevanten Rechnungsdaten mit *generative AI*. Wir nutzen die OpenAI API mit dem ChatGPT 4.o Modell, um die Rechnungsdaten in einem JSON-Format zu speichern.  
**Sequenz 03 "write_db"** - Die Rechnungsdaten werden in eine MongoDB geschrieben. Ist die Rechnung bereits abgelegt, wird sie nicht nochmals hinzugefügt.  
**Sequenz 04 "read_db_to_excel"** - Die Rechnungen, welche noch nicht verschickt wurden, werden ermittelt und in einen Excel-Report geschrieben. Sind alle Rechnungen bereits verschickt, wird kein Report erstellt.  
**Sequenz 05 "email"** - Der Excel-Report wird via E-Mail als Attachment verschickt. Falls bereits alle Rechnungen zugestellt sind, wird eine alternative E-Mail zur Information ausgelöst.


- [UiPath](UiPath) - Code des Projekts.
- [Requirements](Requirements.pdf) - Aufzählung, was für die Ausführung der Automatisierung benötigt wird.
- [Beispiel Logfile](Beispiel_Logfile.txt) - Zur Veranschaulichung, das Logfile einer erfolgreichen Durchfürhung.
- [Architekturmodell](Architekturmodell.pdf) - Beschreibung des Architekturmodells.
- [Architekturtestspezifikation](Architekturtestspezifikation.pdf) - Testspezifikationen zur Architektur.
- [Datenmodell](Datenmodell.pdf) - Beschreibung des Datenmodells.
- [Datentestspezifikation](Datentestspezifikation.pdf) - Testspezifikationen zu den Daten.
- [Codemodell](Codemodell.pdf) - Beschreibung des Codemodells.
- [Codetestspezifikation](Codetestspezifikation.pdf) Testspezifikationen zum Code


**Gruppenmitglieder:**
- Silvano Stupan
- Joshua Kohler
- Daniel Schafhäutle
- Raphael Brunold