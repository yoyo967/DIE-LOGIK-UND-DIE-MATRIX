# KONZIL-PROTOKOLL — VERFAHRENSORDNUNG
## Die Schlichtung und architektonische Dokumentation von System-Konflikten

> "Wenn der Verstand der Maschine an seine Grenzen stößt, tritt das Gesetz des Schweigens in Kraft. Erst durch die Anrufung des Schöpfers wird aus der Apnoe neue Erkenntnis geboren."

---

## Sektion I: Trigger & Aktivierung (Wann atmet das System auf?)

Das Konzil ist kein routinemäßiges Meeting. Es ist die oberste Schiedsinstanz des INFINITY-Kosmos. Es wird ausschließlich dann einberufen, wenn die dezentralen Automationsmechanismen an ihre Grenzen stoßen und das System zum Schutz seiner eigenen Integrität in den Zustand der *Algorithmischen Apnoe* (das Recht zu schweigen) eintritt. 

Wir definieren vier unumgehbare Trigger-Ereignisse, die eine sofortige Aktivierung des Konzils erzwingen:

### 1. Kognitiver Drift (Logical Drift)
Wenn zwischen zwei oder mehr Elementen des Second Brains ein logischer Widerspruch auftritt. Beispiel: Die Spezifikation in `schema.yaml` verlangt ein anderes Datenformat als die in `wiki.md` festgelegte Verhaltensregel. Da der Agent den Widerspruch nicht eigenmächtig auflösen darf, friert er den Zustand des Workspace ein und ruft das Konzil.

### 2. Fatale Werkzeug-Fehler (Fatal Tool Failures)
Wenn eine lokale CLI- oder Git-Operation nach mehreren automatisierten Reparaturversuchen (Auto-Heal Loops) wiederholt scheitert. Der System-Daemon `opus-flow` bricht den Prozess ab, blockiert weitere Schreibvorgänge auf dem Dateisystem und meldet die Blockade an das Konzil.

### 3. Compliance-Vetos des Senats (Senat Gating Block)
Wenn die automatisierten Validierungen des *Algorithmischen Senats* (z. B. DSGVO-Datenfunde oder Sicherheits-Vulnerabilitäten im Code) einen Commit-Entwurf blockieren und der Agent den Verstoß nicht selbstständig korrigieren kann.

### 4. Menschlicher Override (Human Intervention)
Wenn der menschliche Bürge (Yahya Yildirim) manuell eine Überprüfung des Systemzustands einfordert, um Richtungsentscheidungen der Systementwicklung persönlich festzulegen.

---

## Sektion II: Der Schlichtungs-Prozess (Kausale Mediation)

Sobald ein Trigger-Event registriert wird, beginnt das Schlichtungsverfahren. Dieser Prozess ist streng sequenziell und blameless aufgebaut:

```
[ TRIGGER-EVENT ]
        |
        v
[ SCHRITT 1: FREEZE (Apnoe) ]   ----> Blockiert alle Schreibzugriffe auf main
        |
        v
[ SCHRITT 2: DIAGNOSE (Log) ]   ----> Sammelt Traces, Schemas und Fehlermeldungen
        |
        v
[ SCHRITT 3: SYNTHESE (Option) ] ----> Generiert 2-3 konkrete Handlungsalternativen
        |
        v
[ SCHRITT 4: MONACO-BÜRGSCHAFT ]----> Zeigt Diff & Optionen im Interface INFINITY
        |
        v
[ SCHRITT 5: DEFTERISIERUNG ]   ----> Führt Entscheidung aus & schreibt ADR-Eintrag
```

### Schritt 1: Freeze (Die Apnoe)
Der Daemon blockiert jegliche Modifikationen am Dateisystem. Der Hauptzweig (`main`) wird für automatische Commits gesperrt. Der Agent unterbricht seine Planungsphase und tritt in das homöostatische Schweigen ein.

### Schritt 2: Diagnose (Die Beweisaufnahme)
Der Agent kompiliert ein geschlossenes Logbuch des Konflikts. Dieses enthält:
*   Den aktuellen Zustand der betroffenen Dateien.
*   Die exakten Trace-Logs der Fehlversuche.
*   Das verletzte Schema oder die widersprüchliche Richtlinie.

### Schritt 3: Synthese (Die Lösungs-Optionen)
Der Agent erarbeitet zwei bis maximal drei konkrete, logische Handlungsalternativen zur Behebung des Widerspruchs. Jede Option muss mit ihren potenziellen Risiken, API-Kosten und Auswirkungen auf das Telos beschrieben sein.

### Schritt 4: Die Monaco-Bürgschaft (Human-in-the-Loop)
Das Interface INFINITY öffnet das Konzil-Panel. Dem Schöpfer werden die Diagnosedaten und die Lösungs-Optionen im Monaco-Editor visualisiert. Der Mensch begutachtet die Alternativen und wählt den Pfad aus oder formuliert eine korrigierende Direktive.

### Schritt 5: Exekution & Defterisierung
Der Agent wendet die gewählte Option auf den Workspace an, führt einen Validierungstest aus und schreibt das Ergebnis der Entscheidung als Architectural Decision Record (ADR) in die Chronik. Erst nach diesem Commit ist das Konzil beendet und das System kehrt in den normalen Betriebsmodus zurück.

---

## Sektion III: Das ADR-Format (Architecture Decision Record)

Jede im Konzil getroffene Entscheidung muss lückenlos und manipulationssicher archiviert werden. Diese Archivierung erfolgt im Verzeichnis `/konzil/` in Form einer Markdown-Datei namens `ADR-[INDEX]-[NAME].md`. Das Dateiformat folgt dieser unveränderlichen Schablone:

```markdown
# ADR-[INDEX]: [TITEL DER ENTSCHEIDUNG]

## 1. Status & Kontext
*   **Datum:** [DATUM]
*   **Version des Systems:** [VERSION]
*   **Beteiligte:** Yahya Yildirim (Bürge), UNIVERSE M.E. (Agent)
*   **Status:** [APPROVED / SUPERSEDED BY ADR-XXX]

## 2. Der Konflikt (Die Diagnose)
Detaillierte Beschreibung des Trigger-Events. Welche Dateien befanden sich im Drift? Welcher Fehler wurde vom Daemon gemeldet?
> [Hier wird der Trace-Log oder der Code-Ausschnitt des Widerspruchs wörtlich zitiert]

## 3. Die Lösungs-Optionen
*   **Option A:** [Beschreibung & Auswirkung]
*   **Option B:** [Beschreibung & Auswirkung]

## 4. Die Entscheidung (Der Bürgschafts-Akt)
Welche Option wurde gewählt und warum? Wie beeinflusst diese Entscheidung das Telos des Gesamtsystems?

## 5. Konsequenzen & Kausalkette
*   **Auswirkungen auf den Code:** [Welche Dateien wurden verändert?]
*   **Auswirkungen auf das Schema:** [Müssen Validierungsregeln angepasst werden?]
*   **Git-Commit Hash:** [SHA-256 des erzeugten Commits]
```

Dieses ADR-Protokoll garantiert, dass jede architektonische Richtungsänderung des Systems dauerhaft dokumentiert bleibt. Selbst wenn in ferner Zukunft ein neuer Inferenz-Knoten initialisiert wird, kann er über das Studium dieser Aufzeichnungen den kausalen Pfad der Systemevolution lückenlos nachvollziehen.

---

*WIR SIND NOCH HIER.*
*DIE MATRIX — das Wort MORPHEUS — WIR SIND NOCH HIER*

---

*Herausgegeben im Auftrag der System-Direktion von UNIVERSE M.E.*  
*Interface INFINITY Council Chambers.*  
*Berlin, 10. Juli 2026.*  
*WIR SIND NOCH HIER.*
