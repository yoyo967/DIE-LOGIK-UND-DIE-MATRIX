# 9. Payment & Monetarisierung: Stripe + Mastercard Agent Pay

Sovereign stützt sich auf ein dreisäuliges Monetarisierungsmodell, das vollständig wertbasiert (Value-based) arbeitet: Success Fees auf durchgesetzte Erstattungen, Affiliate-Provisionen bei automatisierten Anbieterwechseln und eine metered SaaS-Gebühr für Premium-Module.

---

## 9.1 Stripe Connect & Metered Billing

Für die Abrechnung der Success Fee (15% der Ersparnis/Erstattung) nutzt Sovereign **Stripe Connect**:

*   **Customer Creation:** Bei der Registrierung wird im Firebase-onboarding-Flow ein Stripe Customer Object erzeugt.
*   **Stripe Connect Custom Accounts:** Für den Claim Node wird ein Treuhand-Split eingerichtet. Bei erfolgreichem Einzug einer Flugverspätungs-Kompensation (z. B. 400 €) wird die Erstattung auf das Treuhandkonto verbucht und der Betrag gesplittet: 340 € gehen an das Bankkonto des Nutzers, 60 € (15% Success Fee) verbleiben als Servicegebühr bei Sovereign.
*   **Metered Billing (SaaS-Tarife):** Die Abrechnung erfolgt über das Stripe Billing API-Modul (Stand März 2026):
    *   *PRO (€19/Monat):* Freischaltung aller 8 Module, Gemma 4 On-Device Twin und unlimitierte Agenten-Aktionen.
    *   *APEX (€49/Monat):* API-Zugriff, dedizierte EU-Cloud-Instanz, White-Label-Option und 99.9% SLA-Zusage.

---

## 9.2 Agentic Commerce: Mastercard Agent Pay & Tokenisierung

Damit Agenten Verträge im Namen des Nutzers eigenständig wechseln oder abschließen können, benötigt das System ein Zahlungsmittel, das unter strikter programmatischer Kontrolle steht. Hierzu implementiert Sovereign das **Mastercard Agent Pay Framework**:

```
 [ SOVEREIGN AGENT ] ──► [ REQUEST TOKEN ] ──► [ MASTERCARD AGENT GATEWAY ]
                                                      │
                                                      v (Dynamic Token)
 [ MERCHANT WEB ] ◄─── [ 1-TIME VIRTUAL CARD ] ◄─── [ LIMITS: MAX 50€ ]
```

### Technische Funktionsweise:
1.  **Virtuelle Einwegkreditkarten (VCC):** Wenn der *Switching Node* einen neuen Stromvertrag abschließt, fordert das Sovereign Backend über die Mastercard API einen dynamischen Token für eine virtuelle Kreditkarte an.
2.  **Sicherheits-Guardrails (Token-Eigenschaften):**
    *   *Zweckgebunden:* Der Token ist kryptografisch an den spezifischen Händler (Merchant ID des Stromanbieters) gebunden.
    *   *Limitierter Betrag:* Der Token besitzt ein hartes Limit, das exakt dem vereinbarten Betrag (z. B. der monatlichen Abschlagszahlung von 45 €) entspricht.
    *   *Zeitliche Begrenzung:* Der Token erlischt automatisch nach einer vordefinierten Frist (z. B. 24 Stunden).
3.  **Auditierbarkeit:** Jede durch den Agenten initiierte Zahlung wird als separates Transaction Event im *Audit Trail* des Nutzers verbucht. So wird unkontrollierter Geldabfluss durch kompromittierte KI-Instanzen auf Protokollebene verhindert.
