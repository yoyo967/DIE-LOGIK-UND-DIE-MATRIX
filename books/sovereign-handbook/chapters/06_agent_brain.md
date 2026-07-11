# 6. Agent-Orchestrierung: Der Sovereign Brain

### 6.1 Orchestrator-Architektur

Der Orchestrator ist das kognitive Zentrum des Systems. Er überwacht alle eingehenden Signale aus der *Sensing-Schicht* (E-Mail-Postfächer, Banktransaktionen über PSD2 und Kalendereinträge), übersetzt diese semantisch mithilfe von Gemini 2.5 Flash und stößt proaktiv entsprechende Agent-Tasks an.

```
                          ┌──────────────────┐
                          │   Cloud Scheduler│
                          │   (Cron Triggers)│
                          └────────┬─────────┘
                                   │
                          ┌────────▼─────────┐
                          │   SENSING LAYER  │
                          │ • Gmail API Scan │
                          │ • PSD2 Txn Scan  │
                          │ • Calendar Check │
                          └────────┬─────────┘
                                   │
                    Pub/Sub: agent-tasks
                                   │
                          ┌────────▼─────────┐
                          │   ORCHESTRATOR   │
                          │   (Vertex AI)    │
                          └────────┬─────────┘
                                   │
         +-------------------------+-------------------------+
         v (Klassifikation)        v (Klassifikation)        v (Klassifikation)
  [ Negotiation ]           [ Switching ]             [ Claim ]
  - DSL/Strom-Tarife        - Jährlicher Wechsel      - Flugverspätungen
  - Kündigungs-Generierung  - Vergleichsportal-API    - EU261 Entschädigung
```

---

### 6.2 Task-Klassifikation und Routing-Loop

Jedes erfasste Ereignis wird über ein Pub/Sub-Topic `agent-tasks` an den Orchestrator übermittelt. Der Orchestrator evaluiert das Ereignis anhand eines strukturierten JSON-Outputs von Gemini:

```json
{
  "eventId": "evt_893247923",
  "eventType": "EMAIL_RECEIVED",
  "summary": "Preiserhöhung um 5,50 €/Monat von Vodafone DSL ab Q3 2026",
  "detectedContract": "vodafone_dsl_0821",
  "recommendedAction": "NEGOTIATE_CONTRACT",
  "targetNode": "negotiation_node",
  "confidenceScore": 0.98,
  "requiresApproval": true
}
```

Wenn das Vertrauensniveau (confidenceScore) über **0.85** liegt, delegiert der Orchestrator die Aufgabe an den zuständigen Sub-Agenten. Wenn die Aktion finanzielle oder vertragliche Auswirkungen hat, wird eine Freigabe-Anforderung im *Monaco-Review-Gate* registriert und ein FCM-Push-Signal an das Endgerät des Users abgesetzt.

---

### 6.3 Status-Zustandsmaschine (State Machine)

Der Lebenszyklus jedes Agent-Tasks wird in Firestore über die Zustandsmenge `TaskStatus` abgebildet:

*   `CREATED`: Task initialisiert und in der Queue registriert.
*   `SCANNING`: Erfassung von Zusatzinformationen (z. B. Vertragsdatenbank, Bonitätsprüfung).
*   `PROPOSED`: Vorschlag für Vertragsänderung/Wechsel/Entschädigung erzeugt.
*   `PENDING_APPROVAL`: Wartezeit auf die physische Freigabe des Users (HITL).
*   `APPROVED`: Freigabe erhalten; Ausführungsphase eingeleitet.
*   `EXECUTING`: Der Node interagiert mit Drittsystemen (z. B. E-Mail-Versand, API-Aufrufe).
*   `COMPLETED`: Aktion erfolgreich abgeschlossen und verbuchte Einsparungen erfasst.
*   `FAILED`: Fataler Fehler im Inferenz- oder Kommunikations-Substrat (Rollback eingeleitet).
