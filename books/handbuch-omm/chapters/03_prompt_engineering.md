# KAPITEL 2 · Prompt Engineering

### *Die Kernkompetenz des KI-Zeitalters*

Prompt Engineering ist nicht das Schreiben von Anweisungen. Es ist das **Denken in Systemen** — du entwirfst die Architektur eines Gesprächs, das einen präzisen, reproduzierbaren, exzellenten Output erzeugt.

---

### Das 6-Element Framework (Google/Vertex + Extended)

```
[1] PERSONA      → Wer ist die KI in dieser Session?
[2] KONTEXT      → Was ist der Hintergrund, die Situation?
[3] INSTRUKTION  → Was genau soll getan werden?
[4] CONSTRAINTS  → Was darf nicht passieren? (DSGVO, Ton, Format)
[5] OUTPUT       → Wie soll das Ergebnis aussehen?
[6] RECAP        → Wiederhole die kritischen Punkte am Ende
```

**Beispiel — Vollständig ausgeführter Prompt:**

```
[PERSONA] Du bist ein erfahrener CMO mit 12 Jahren B2B-SaaS-Erfahrung
im DACH-Markt. Du denkst strategisch, nicht taktisch.

[KONTEXT] Wir launchen in Q3 2026 ein neues SaaS-Tool für 
HR-Abteilungen in mittelständischen Unternehmen (50–500 MA).
Wettbewerber: Personio, HiBob. USP: Agentic AI für Onboarding.
Budget: 80K EUR für Q3.

[INSTRUKTION] Erstelle ein strategisches Kampagnen-Briefingdokument
mit: 1) Zielgruppendefinition, 2) Kernbotschaft, 3) Kanalstrategie,
4) KPI-Framework, 5) Risiken.

[CONSTRAINTS] EU AI Act compliant. DSGVO-konform. Keine ungesicherten
Behauptungen. Kein Fachjargon ohne Erklärung. Deutsch.

[OUTPUT] Markdown-Format. Klare Überschriften. Max. 800 Wörter.
Entscheidungsreif für Präsentation vor Geschäftsführung.

[RECAP] Stelle sicher: DACH-Fokus, Q3 2026, DSGVO-Konformität,
max. 800 Wörter, Markdown.
```

---

### Die 4 Qualitätsstufen eines Prompts

| Stufe | Merkmal | Ergebnis |
| :--- | :--- | :--- |
| **Level 1** | Vage Anfrage ("Schreib einen Blogpost") | Generischer, austauschbarer Output |
| **Level 2** | Thema + Format definiert | Verwendbarer, aber mittelmäßiger Output |
| **Level 3** | Alle 6 Elemente + Chain-of-Thought | Hochwertiger, spezifischer Output |
| **Level 4** | Level 3 + Few-Shot + Iteration + Review | Exzellenter, publishreifer Output |

**Ziel:** Immer Level 4. Die Differenz zwischen Level 2 und Level 4 ist die Differenz zwischen einer durchschnittlichen und einer exzellenten OMM.

---

### Erweiterte Techniken

*   **Chain-of-Thought** — Reduziert Halluzinationen nachweislich:  
    `„Erkläre Schritt für Schritt dein Vorgehen, bevor du den Output lieferst.“`
*   **Few-Shot** — 2–3 Beispiele im Prompt erhöhen Qualität dramatisch:  
    `„Hier sind zwei Beispiele für exzellente Kampagnenbriefings: [Beispiel 1] [Beispiel 2]. Erstelle nun ein ähnliches für…“`
*   **Iterationsprotokoll** — Erster Draft ist nie final:
    *   Draft 1: Struktur verstehen
    *   Draft 2: Lücken füllen, Schwächen adressieren
    *   Draft 3: Finalisierung, Tonalität, Präzision
    *   Review: `„Was würde ein kritischer Experte an diesem Text bemängeln?“`
