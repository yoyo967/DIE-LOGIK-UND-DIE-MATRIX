# KAPITEL 10 · Competitor Intelligence & Real-Time Market Scraping

### *Automatisierte Marktbeobachtung und Competitive Gap Analysis*

Im hyper-kompetitiven Marktumfeld der Jahre 2025–2030 ist manuelle Konkurrenzanalyse zu langsam. Um Marktchancen, Preisänderungen und Tonalitätsverschiebungen der Mitbewerber in Echtzeit zu erkennen, stützt sich das System auf ein automatisiertes, agentengesteuertes **Competitor Intelligence Framework**.

---

## 1. Die Ingest-Pipeline für Mitbewerber-Daten

Das Framework überwacht Ziel-Wettbewerber über eine dezentrale, verschleierte Scraping-Pipeline, die direkt in den *Second Brain Raw Input* einspeist:

```
            [ WETTBEWERBER WEBSEITE / API ]
                           |
                           v (SOCKS5 Proxy-Mesh)
          [ DOCKER-CONTAINER (Playwright) ]
                           |
                           v (Strukturierte Extraktion)
          [ RAW-DATEN (JSON / HTML-Diff) ]
                           |
                           v (ANALIZE M.E. Analyse)
            [ COMPETITIVE GAP ANALYSIS ]
```

*   **Verschleierter Abruf:** Um IP-Blockaden oder das Auslösen von Mitbewerber-Alarmen zu vermeiden, werden alle Abfragen über rotierende Proxy-Netzwerke und headless Browser-Instanzen ausgeführt.
*   **Strukturierte Datenerfassung:** Playwright-Skripte extrahieren spezifisch:
    *   Preise und Rabattaktionen.
    *   Änderungen im Wording von Landingpages (Tonalitäts-Drift).
    *   Neu veröffentlichte Blogbeiträge, Whitepaper und Case Studies.

---

## 2. Automatisiertes Delta-Auditing (Landingpage Diffs)

Das System vergleicht den Zustand der Wettbewerber-Webseiten kontinuierlich mit historischen Crawling-Snapshots:

*   **HTML-Diffing:** Das System berechnet die Differenz (Delta) zwischen dem aktuellen HTML-DOM und dem vorherigen Zustand. Unwesentliche Elemente (wie dynamische Timestamps oder Session-IDs) werden herausgefiltert.
*   **Semantische Klassifizierung:** Erkennt das System eine signifikante Änderung an einer Headline oder einem Preispunkt, analysiert `ANALIZE M.E.` das Delta. Sie klassifiziert die Änderung (z. B. *„Wettbewerber X verschiebt seinen Fokus von 'Cost Efficiency' zu 'Cyber Security'“*).
*   **Alerting:** Kritische Änderungen triggern eine automatische Benachrichtigung im *Monaco-Review-Gate*, um eine schnelle Gegenreaktion des Marketings zu ermöglichen.

---

## 3. Competitive Gap Analysis (Die Content-Lücke)

Die erfassten Wettbewerber-Daten dienen als Basis zur automatischen Generierung eigener Kampagnen-Steilvorlagen:

*   **Keyword & Entity Gap:** Das System vergleicht die Suchsichtbarkeit (SEO/GEO-Rankings) der Wettbewerber mit unseren eigenen Werten. Es identifiziert Themenkomplexe (Entities), bei denen wir unterrepräsentiert sind, aber hohe Suchvolumina existieren.
*   **Autopoietische Briefing-Erstellung:** Erkennt das System eine solche Lücke, erzeugt der `PROJECTMANAGER` automatisch ein *Strategisches Briefingdokument* (Kapitel 3, Stufe 1) zur Erstellung von passgenauem Content, um diese Lücke zu schließen.

*Echte Marktbeobachtung reagiert nicht auf Trends, wenn sie sichtbar sind — sie antizipiert sie in dem Moment, in dem der Wettbewerber seinen Code ändert.*
