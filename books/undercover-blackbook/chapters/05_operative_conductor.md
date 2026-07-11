# Kapitel 4: Der operative Conductor (PROJECTMANAGER Agent)

Die Steuerung eines hochgradig verteilten, agentischen Schwarms erfordert eine dedizierte Instanz zur Ablaufplanung und Zustandskontrolle. Diese Rolle übernimmt der **PROJECTMANAGER**-Agent. Als operativer Conductor fungiert er als deterministische State-Machine, die das Bindeglied zwischen der strategischen Ausrichtung des `MASTERPLAN` und den direkten Systemeingriffen des `AGENTICUM G5` bildet. 

Er überwacht die Einhaltung der Arbeitsabläufe, verwaltet Ressourcen-Budgets und erzwingt strenge Qualitäts-Gatter vor jedem System-Commit.

---

## 1. Das Scheduler- und Dispatcher-Prinzip

In Multi-Agenten-Systemen führt unkoordinierter Zugriff auf Systemressourcen und Dateipfade zu Race-Conditions und Logikkonflikten. Der PROJECTMANAGER verhindert dies, indem er als zentraler Scheduler und Task-Dispatcher agiert:

```
                  [ STRATEGISCHE VORGABE (MASTERPLAN) ]
                                    |
                                    v
                  [ OPERATIVER CONDUCTOR (PROJECTMANAGER) ]
                     - Zustandskontrolle (State-Machine)
                     - Task-Scheduler / Gating
                                    |
            +-----------------------+-----------------------+
            |                                               |
            v                                               v
     [ task.md ]                                    [ loop-zyklus.md ]
  - Atomare Tasks                                - Phasen-Gatter (Planning,
  - Syntax-Check                                   Execution, Verification)
            |                                               |
            +-----------------------+-----------------------+
                                    |
                                    v
                     [ EXEKUTIVE AUSFÜHRUNG (G5) ]
```

Der PROJECTMANAGER schreibt selbst keinen Produktivcode. Seine Hauptaufgabe ist die Metasteuerung: Er liest die Systemzustände ein, weist Subagenten konkrete Teilaufgaben zu und überwacht deren fehlerfreie Abarbeitung.

---

## 2. Atomare Task-Granulierung und das task.md-Schema

Jede komplexe Systemänderung wird vom PROJECTMANAGER in eine Sequenz atomarer, nicht weiter teilbarer Arbeitsschritte zerlegt. Diese Schritte werden im zentralen Arbeits-Protokoll **`task.md`** hinterlegt.

Das System erzwingt dabei ein striktes Syntax-Schema:
*   `- [ ]` **Unvollständiger Task:** Der Task ist definiert, aber die Bearbeitung wurde noch nicht begonnen.
*   `- [/]` **In-Progress-Task:** Der Task wird aktuell von einem spezifischen Agenten-Thread bearbeitet.
*   `- [x]` **Abgeschlossener Task:** Der Task ist vollständig abgearbeitet und verifiziert.

### Das Sledge-Hammer-Validierungsprinzip
Der PROJECTMANAGER verbietet das manuelle oder willkürliche Abhaken von Tasks. Ein Task darf erst dann den Status `[x]` erhalten, wenn der ausführende Agent einen erfolgreichen Testlauf oder einen verifizierten Diff-Trace an den PROJECTMANAGER übermittelt hat. Schlägt ein automatisierter Test fehl, setzt der PROJECTMANAGER den Task sofort zurück und alarmiert das System.

---

## 3. Ressourcen-Gating und API-Quota-Schutz

Um einen ununterbrochenen Inferenzbetrieb auf Google Cloud / Vertex AI zu sichern, implementiert der PROJECTMANAGER ein aktives Ressourcen-Gating:

*   **Token-Budgetierung:** Das System überwacht kontinuierlich das verbrauchte Token-Volumen je Zeiteinheit (TPU-Rate-Limits / TPM - Tokens Per Minute).
*   **Abwehr von HTTP 429-Blockaden (Rate Limits):** Erkennt der PROJECTMANAGER eine drohende Quotenüberschreitung, drosselt er die Task-Zuweisungen an den Schwarm. Er schaltet eine Warteschlange vor (Queueing) und initiiert kontrollierte Wartezeiten (Exponential Backoff mit Jitter), um Systemblockaden proaktiv zu verhindern.
*   **Kostenüberwachung:** Der PROJECTMANAGER gleicht die Ausgaben für Inferenzläufe gegen ein definiertes Tagesbudget ab. Wird dieses Budget überschritten, suspendiert er unkritische Hintergrundprozesse und fordert eine Freigabe durch den Operator an.

---

## 4. Phasen-Gating im loop-zyklus.md

Der Fortschritt eines Projekts wird in getrennten, isolierten Phasen organisiert. Der PROJECTMANAGER erzwingt dieses Phasenmodell im Protokoll **`loop-zyklus.md`**:

1.  **Planning Phase (Planung):** Definition der Anforderungen und logischen Abhängigkeiten. Ein Übergang zur nächsten Phase ist gesperrt, bis der Architekt den Plan freigibt.
2.  **Research Phase (Recherche):** Analyse des bestehenden Codes und der Schnittstellen.
3.  **Execution Phase (Ausführung):** Generierung und Modifikation des Codes.
4.  **Verification Phase (Verifizierung):** Ausführung automatisierter Testreihen.

Der PROJECTMANAGER fungiert als unerbittlicher Gatekeeper: Er verweigert den Übergang zur nächsten Phase, solange die definierte Checkliste der aktuellen Phase nicht zu 100 % erfüllt ist. Dies verhindert, dass ungetesteter Code oder unvollständige Spezifikationen das System destabilisieren.

*Der PROJECTMANAGER transformiert chaotische Inferenzströme in eine disziplinierte, deterministische Ausführungsreihenfolge.*
