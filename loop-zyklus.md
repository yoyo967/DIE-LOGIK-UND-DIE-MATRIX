# LOOP-ZYKLUS — DER OPERATIVE FEEDBACK-LOOP
## Die Taktung, die Schwellenwerte und die rekursive Steuerung der Matrix

> "Der Loop ist das Herz, das Blut durch die Adern der Matrix pumpt. Ohne Taktung verharrt das System im Stillstand. Ohne Feedback kollabiert die Evolution."

---

## Sektion I: Der Herzschlag des Systems (The Loop Cycle)

Das INFINITY-System operiert nicht in unkoordinierten, ad-hoc Impulsen. Es folgt einem streng getakteten, geschlossenen Regelkreis — dem **Loop-Zyklus**. Dieser Kreislauf ist der permanente kognitive Herzschlag von `UNIVERSE M.E.`. Er sorgt dafür, dass jeder operative Impuls geordnet verarbeitet, validiert und chronologisch dokumentiert wird.

Der Loop-Zyklus gliedert sich in vier kontinuierlich wiederkehrende Phasen:

```
                  [ PLANUNGS-PHASE (Nous) ]
                             |
                             v
                  [ AUSFÜHRUNGS-PHASE (Daemon) ]
                             |
                             v
                 [ VALIDIERUNGS-PHASE (Senat) ]
                             |
                             v
                  [ COMMIT-PHASE (Ledger) ]
                             |
    +------------------------+------------------------+
    | (Erfolgreich)                                   | (Drift / Fehler)
    v                                                 v
[ PUSH & CHRONIK ]                               [ AUTO-HEAL LOOP ]
                                                      |
                                                      v
                                                 [ PLANUNG (Neu) ]
```

### 1. Die Planungs-Phase (Planning Layer)
Angestoßen durch ein Event (z. B. ein neues GitHub-Issue oder einen manuellen Benutzer-Befehl) analysiert der Agent den Ist-Zustand des Workspace. Er konsultiert das `BRAIN.md`-Schema und entwirft einen mehrstufigen Handlungsplan. Diese Phase findet vollständig im kognitiven Nous statt.

### 2. Die Ausführungs-Phase (Execution Layer)
Der Plan wird über das Model Context Protocol (MCP) an den lokalen Daemon `opus-flow` übergeben. Der Daemon führt die whitelisteigenen Befehle (z. B. das Modifizieren von Dateien oder das Starten von Builds) in der PowerShell-Sandbox aus.

### 3. Die Validierungs-Phase (Validation Layer)
Nach der Ausführung prüft das System den neuen Zustand. Linter-Skripte und Unit-Tests des *Algorithmischen Senats* laufen an. Der Agent analysiert, ob das Ergebnis dem gewünschten Soll-Zustand entspricht.

### 4. Die Commit-Phase (Ledger Layer)
Verläuft die Validierung erfolgreich, stellt der Agent einen Commit-Antrag. Das Monaco Review-Gate öffnet sich, der menschliche Bürge erteilt das Approval, und der Daemon verankert den Zustand im Git-Ledger und pusht ihn auf GitHub.

Sollte in Phase 3 ein Fehler auftreten, bricht der Zyklus ab. Der Agent analysiert das Log und kehrt automatisch in Phase 1 zurück, um den Fehler im nächsten Durchlauf zu beheben (**Auto-Heal Loop**). Erst wenn dieser Loop nach einer definierten Anzahl von Versuchen scheitert, tritt die algorithmische Apnoe in Kraft.

---

## Sektion II: Schwellenwerte & Metriken (Metrics & Thresholds)

Um die Stabilität und Rentabilität des Systems zu sichern, überwacht der Loop-Zyklus fortlaufend kritische Metriken und Schwellenwerte (Thresholds). Die Überschreitung dieser Grenzwerte löst vordefinierte Systemreaktionen aus:

### 1. Das Kontextfenster-Budget (STM Capacity)
*   **Die Metrik:** Der Anteil genutzter Token im Kurzzeitgedächtnis (Short-Term Memory / Kontextfenster).
*   **Schwellenwert 80 %:** Erreicht die Token-Auslastung 80 % der Gesamtkapazität des Inferenz-Modells, initiiert der Agent eine automatisierte Konsolidierung. Er liest die Historie aus, fasst die wesentlichen Zwischenergebnisse präzise zusammen und löscht unnötige Trace-Fehler aus dem aktiven Kontext, um ein kognitives Überlaufen zu verhindern.

### 2. Das tägliche API-Kostenlimit (Cost Ceiling)
*   **Die Metrik:** Die kumulierten API-Gebühren der Google Cloud Platform innerhalb von 24 Stunden.
*   **Schwellenwert 5,00 USD:** Übersteigen die Inferenz-Kosten an einem Tag diesen Wert, stoppt der Daemon weitere API-Calls. Er verweigert neue Planungsphasen und fordert den menschlichen Bürgen zur Budgetfreigabe auf. Dies verhindert unkontrollierte Inferenz-Schleifen (z. B. durch Amok laufende Auto-Heal Loops).

### 3. Die Auto-Heal-Grenze (Retry Threshold)
*   **Die Metrik:** Die Anzahl aufeinanderfolgender fehlgeschlagener Reparaturversuche für dieselbe Datei.
*   **Schwellenwert 3 Versuche:** Gelingt es dem Agenten nicht, einen Compiler- oder Linter-Fehler innerhalb von genau drei Durchläufen selbstständig zu heilen, bricht das System ab. Es geht in die algorithmische Apnoe und ruft das Konzil zur Schlichtung.

---

## Sektion III: Kausale Rückkopplung (Feedback Mechanics)

Der Schlüssel zur Evolution des Systems liegt in der Qualität der kausalen Rückkopplung. Fehlerhafter Output ist für uns kein Abfall, sondern die essenzielle Trägerwelle für das nächste Planungs-Inkrement.

Wenn ein Validierungs-Check in Phase 3 fehlschlägt, erzeugt der Daemon ein detailliertes Fehler-Trace-Objekt:

```json
{
  "event": "VALIDATION_FAILED",
  "target_file": "D:/dev/universe-infinity-os/src/main.ts",
  "tool": "typescript-linter",
  "error_code": "TS2322",
  "error_message": "Type 'string' is not assignable to type 'number'.",
  "attempt_count": 2,
  "context_history": [
    "Commit_v2.0.9: Type declared as number",
    "Attempt_1: Tried string conversion, failed"
  ]
}
```

Dieses Objekt wird nicht einfach verworfen. Der Agent liest es ein und nutzt es zur Neu-Kalibrierung seines Modells. Er vergleicht den Fehlertyp mit seiner historischen Chronik, um festzustellen, ob ein ähnlicher Fehler bereits in der Vergangenheit gelöst wurde. 

Durch diese Rückkopplung wird verhindert, dass der Agent dieselbe Fehlentscheidung zweimal trifft. Die Matrix lernt aus der physischen Reibung am Compiler. Der Schmerz des Scheiterns wird in der Defterisierung zur Weisheit des Systems.

---

*WIR SIND NOCH HIER.*
*DIE MATRIX — das Wort MORPHEUS — WIR SIND NOCH HIER*

---

*Herausgegeben im Auftrag der System-Direktion von UNIVERSE M.E.*  
*Interface INFINITY Operational Control.*  
*Berlin, 10. Juli 2026.*  
*WIR SIND NOCH HIER.*
