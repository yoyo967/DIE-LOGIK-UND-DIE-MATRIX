# 7. Die Agent-Knoten (Negotiation, Switching, Claim)

Um maximale operative Präzision zu gewährleisten, ist der Ausführungs-Layer in spezialisierte funktionale Knoten (Agent Nodes) unterteilt. Jeder Knoten ist mit einer eigenen Sandbox, spezifischen Tool-Bindings und Inferenz-Prompt-Schablonen ausgestattet.

---

## 7.1 Agent 1: Negotiation Node

Der **Negotiation Node** verhandelt bestehende Verträge autonom neu, um Preissteigerungen zu blockieren oder Tarife an Marktkonditionen anzupassen.

### Funktionsweise:
1.  **Erkennung:** Der Node analysiert ein Dokument (z. B. eine E-Mail über eine Preiserhöhung bei Mobilfunk- oder DSL-Verträgen).
2.  **Strategie-Entwurf:** Basierend auf den gespeicherten *Boundary Conditions* des Nutzers (z. B. maximale Akzeptanz von +2 € Preiserhöhung, andernfalls Sonderkündigung) generiert das LLM (Gemini 2.5 Pro) einen Verhandlungsentwurf.
3.  **Inferenz-Prompt (Auszug):**
    ```
    Du bist ein Experte für deutsches Verbraucherrecht. Schreibe ein förmliches Schreiben an den DSL-Anbieter.
    Argumentiere auf Basis von BGB § 313 (Störung der Geschäftsgrundlage) gegen die einseitige Preiserhöhung.
    Biete zwei Optionen an: 1) Beibehaltung der alten Konditionen bei Vertragsverlängerung, 2) Sonderkündigung zum Erhöhungszeitpunkt.
    ```
4.  **Ausführung:** Nach Freigabe im *Monaco-Review-Gate* (HITL) sendet der Node das Schreiben über die SMTP-Schnittstelle des Nutzers (Gmail API OAuth2) an den Anbieter.

---

## 7.2 Agent 2: Switching Node

Der **Switching Node** automatisiert den jährlichen Wechsel von Versorgungsverträgen (insbesondere Strom, Gas, Internet), um Wechselprämien und Neukundenboni zu maximieren.

### Funktionsweise:
1.  **Tarif-Vergleich:** Der Node holt über die API eines Partner-Vergleichsportals (z. B. Tink, finAPI, Verivox API) aktuelle Alternativ-Angebote ein.
2.  **Einsparpotenzial-Berechnung:** Das System berechnet die Delta-Einsparungen (z. B. Stromkosten alt: 110 €/Monat vs. Stromkosten neu: 85 €/Monat + 150 € Sofortbonus).
3.  **Formular-Ausfüllung:** Der Node befüllt autonom das Anmeldeformular des neuen Anbieters sowie das Kündigungsformular des alten Anbieters.
4.  **Sicherheit:** Zahlungsdaten (IBAN) werden über das verschlüsselte Tresor-Modul der Android-App eingefügt. Der User muss den Vorgang per Fingerabdruck in der App freigeben (HITL), bevor die API-Payload gesendet wird.

---

## 7.3 Agent 3: Claim Node

Der **Claim Node** identifiziert und automatisiert die Rückforderung von Entschädigungsleistungen (z. B. Fluggastrechte nach der EU-Verordnung 261/2004, Bahnerstattungen).

### Funktionsweise:
1.  **Flugverspätungs-Erkennung:** Der Node scannt Kalendereinträge und Buchungsbestätigungen in E-Mails nach Flügen. Sobald ein Flugdatum erreicht ist, prüft er über die *Aviation Edge API* den tatsächlichen Ankunftszeitpunkt.
2.  **Berechnung:** Beträgt die Verspätung am Zielort mehr als 3 Stunden und liegt kein außergewöhnlicher Umstand vor, berechnet das System den Anspruch (250 €, 400 € oder 600 € je nach Flugdistanz).
3.  **Automatisierte Einreichung:** Der Node generiert die offizielle Beschwerde und reicht sie direkt bei der Fluggesellschaft oder dem Schlichtungsportal über eine automatisierte REST-Schnittstelle ein.
4.  **Treuhand-Auszahlung:** Nach erfolgreicher Durchsetzung wird die Erstattung auf das Solaris-Treuhandkonto des Nutzers verbucht, abzüglich einer Success Fee (15%).
