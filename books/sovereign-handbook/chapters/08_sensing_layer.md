# 8. Sensing Layer: E-Mail & Bank-API Integration

Der Sensing Layer ist die sensorische Schnittstelle des Sovereign OS zur physischen und digitalen Lebensrealität des Nutzers. Seine Aufgabe ist das kontinuierliche und sichere Einlesen relevanter Datenpunkte.

---

## 8.1 E-Mail Sensing (Gmail API & IMAP OAuth2)

Um Verträge, Preiserhöhungen und Kündigungen automatisiert zu erkennen, benötigt das System Lesezugriff auf das E-Mail-Postfach des Nutzers.

### Technische Umsetzung:
1.  **OAuth2 Authentifizierung:** Sovereign nutzt den Google OAuth2 Flow für mobile Android-Clients. Es fordert ausschließlich den Scope `https://www.googleapis.com/auth/gmail.readonly` an.
2.  **Filter-basierter Sync:** Statt das gesamte Postfach herunterzuladen, filtert das Backend (Cloud Run) E-Mails über Such-Queries:
    *   `from:(vodafone OR telekom OR O2 OR "e.on" OR vattenfall OR check24 OR verivox)`
    *   `subject:(Preiserhöhung OR Kündigung OR Vertragsänderung OR Buchungsbestätigung OR Rechnung)`
3.  **Lokaler Text-Extraktor:** Der Mail-Body wird von HTML bereinigt, in reinen Text überführt und an die Gemini 2.5 Flash API gesendet, um relevante Entities (Vertragspartner, Kosten, Laufzeiten, Kündigungsfristen) zu extrahieren.

---

## 8.2 PSD2 Open Banking (finAPI / Tink)

Finanztransaktionen lügen nicht. Durch die Anbindung an die europäische PSD2-Schnittstelle (XS2A-Standard) kann Sovereign Verträge anhand realer Zahlungsströme identifizieren.

### Technische Umsetzung:
1.  **API-Provider:** Sovereign nutzt `finAPI` (bzw. Tink) als lizenzierten Kontoinformationsdienst (KID / AISP).
2.  **Zustimmungs-Flow:** Der Nutzer erteilt Sovereign in der Android-App die Erlaubnis, Kontoumsätze abzurufen. Diese Erlaubnis muss gesetzlich alle 180 Tage erneuert werden.
3.  **Transaktions-Scanning:** Das System analysiert einmal täglich die Kontobewegungen. Gemini identifiziert wiederkehrende Abbuchungen (z. B. monatliche Beiträge) und ordnet sie den jeweiligen Verträgen zu:
    *   *Muster:* Regelmäßige Abbuchung von 34,99 € mit Verwendungszweck `Vodafone Deutschland GmbH, Ref: DE-89324`.
    *   *Klassifikation:* DSL-Vertrag. Das System prüft, ob in den E-Mails ein entsprechender Vertrag existiert. Fehlt dieser, wird der Nutzer gebeten, das PDF hochzuladen (Zero-Knowledge-Storage).
4.  **Abo-Fallen-Detektion:** Transaktionen mit steigenden Beträgen oder ohne zugeordneten Vertrag werden als Anomalie markiert und dem Nutzer im Dashboard als Risiko gemeldet.
