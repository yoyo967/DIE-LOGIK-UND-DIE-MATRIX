# 10. Sicherheitsarchitektur & Human-in-the-Loop

Die Architektur von Sovereign beruht auf dem unumstößlichen Gesetz, dass künstliche Intelligenz niemals die endgültige Entscheidungsgewalt über die vertraglichen und finanziellen Realitäten eines Menschen besitzen darf. Sicherheits- und Freigabemechanismen sind daher fest in den Core-Workflows verankert.

---

## 10.1 Zero-Trust Sandbox & Key Storage

Alle kritischen Benutzerdaten (Bankzugangsdaten, Passwörter, persönliche Dokumente) unterliegen einer Zero-Knowledge-Architektur:

*   **Android Keystore System:** Sensible API-Token und OAuth2-Credentials für den Mail- und Bankzugang werden auf dem Endgerät des Nutzers im hardware-gestützten Keystore verschlüsselt abgelegt. Das Backend (GCP Cloud Run) erhält niemals dauerhaften Zugriff auf diese Keys.
*   **Isolierte Agenten-Laufzeiten:** Die Agenten-Knoten (Negotiation, Switching, Claim) laufen in isolierten Docker-Containern innerhalb von Google Cloud Run. Sie besitzen keine persistenten Festplatten und kommunizieren ausschließlich über signierte Pub/Sub-Nachrichten mit dem API-Gateway.

---

## 10.2 Human-in-the-Loop (HITL) & Approval-Flows

Kritische Aktionen (z. B. das Absenden einer Kündigung, der Wechsel eines Stromanbieters oder eine Zahlungsausführung) erfordern zwingend die menschliche Autorisierung.

```
 [ AGENT ENGINE ] ──► [ PROPOSAL CREATED ] ──► [ FCM PUSH TO APP ]
                                                      │
                                                      v (Review Gate)
 [ SUCCESS / EX ] ◄── [ SIGNED TRANS (IBAN) ] ◄── [ SWIPE TO APPROVE ]
```

### Der Freigabe-Ablauf:
1.  **Vorschlagserstellung:** Der Agent generiert das Dokument oder den Wechselantrag und speichert ihn im Status `PENDING_APPROVAL` in Firestore.
2.  **Push-Notifikation:** Der Firebase Cloud Messaging Service (FCM) sendet eine hochpriorisierte Push-Notifikation an das verknüpfte Android-Gerät des Nutzers.
3.  **UI-Validierung:** Die Sovereign-App zeigt dem Nutzer den exakten Entwurf (z. B. das Anschreiben an den Anbieter oder das Tarif-Delta) im *Approval Screen* an. Eventuelle Risiken werden durch eine Ampel-Metrik hervorgehoben.
4.  **SwipeToApprove:** Der Nutzer bestätigt die Aktion durch die Compose-Geste `SwipeToApprove`. Diese Geste erfordert auf OS-Ebene eine biometrische Verifizierung (Fingerabdruck oder Face Unlock).
5.  **Signierte Transaktion:** Erst nach erfolgreicher Verifizierung wird der Task-Status auf `APPROVED` gesetzt und an die Execution-Queue übermittelt.

---

## 10.3 Algorithmic Senate (Security Senate)

Sovereign implementiert einen programmatischen Prüfrahmen für alle KI-generierten Outputs, um Halluzinationen und fehlerhafte Formulierungen zu blockieren:

*   **Der Senate Score:** Bevor ein Schreiben oder Antrag dem Nutzer zur Freigabe vorgelegt wird, prüft eine unabhängige Gemini-Instanz (der "Senate") die Qualität des Texts auf einer Skala von 1–10.
*   **Prüfparameter:**
    *   *Compliance:* Entspricht der Text den gesetzlichen Grundlagen (z. B. BGB-Fristen, DSGVO)?
    *   *Brand Voice:* Passt die Tonalität zur Tonalitäts-Richtlinie des Nutzers?
    *   *Accuracy:* Enthält das Dokument halluzinierte Fakten oder Platzhalter (z. B. `[Name hier einfügen]`)?
*   **Blockierung:** Fällt der Senate Score unter **8.0**, wird die Aktion automatisch blockiert, der Task auf `FAILED` gesetzt und zur Neugenerierung an den Agenten zurückgegeben. Der Nutzer wird nicht mit unfertigen Entwürfen belästigt.
