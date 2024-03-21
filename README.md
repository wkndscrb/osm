# Open Street Map

Hydraten und Wasserentnahmestellen haben die folgenden Eigenschaften

|Parameter|Wert|Beschreibung|
|---|---|---|
|emergency: |suction_point | Saugstelle|
|emergency: |water_tank | Löschteich|
|emergency: |fire_hydrant | Hydrant|
|emergency:tpye |underground| Unterflurhydrant|
|emergency:tyoe |pillar| Überflurhydrant|
|emergency:type: |pipe | Verschlossenes Rohr|

Das Skript setFireHydrants.py erstellt Wasserentnahmestellen an den Geokordinaten. Diese Daten erhält das Skript aus der einer JSON Datei. Ein Beispiel für die JSON Datei ist mit data/WES.json abgelegt. 

Für unseren Zweck wurden die Daten für die Wasserentnahmestellen aus FOX112 als Ecxel Datei generiert und in das gewünschte JSON Format konvertiert. Die Konvertierung ist mit dem Skript convertF112Data.py erfolgt.

Um zu Prüfen welche Wasserentnahmestellen schon in einem Ort vorahanden sind kann das Skript getFireWaterData.py eingesetzt werden. Ortsnamen eintragen und los ... Das Skript erstellt ebenfalls eine JSON Datei mit den Waserentnahmestellen. 




