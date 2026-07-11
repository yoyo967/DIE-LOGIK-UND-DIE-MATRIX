# CONSTITUTION — DIE LOGIK & DIE MATRIX

**Version:** 1.0.0  
**Datum:** 2026-07-09  
**Status:** Aktiv  
**Lizenz:** MIT (Code) / CC-BY-4.0 (Dokumente)

---

## Artikel 1 — Zweck und Geltungsbereich

Dieses Dokument legt die Governance-Grundsätze des Open-Source-Projekts
**DIE LOGIK & DIE MATRIX** fest. Es gilt für alle Mitwirkenden, Maintainer
und Nutzer des Repositorys sowie seiner abgeleiteten Werke.

Das Projekt dient als Blackbook und Cocreationsmatrix für Entwickler,
KI-Agenten und Interface Infinity. Berlin, 9. Juli 2026.

---

## Artikel 2 — Grundprinzipien

1. **Transparenz** — Entscheidungen werden öffentlich dokumentiert (ADR-Format).
2. **Nachvollziehbarkeit** — Alle Änderungen erfolgen via Pull Request mit Review.
3. **Offenheit** — Beiträge sind willkommen; Anforderungen siehe CONTRIBUTING.md.
4. **Datenschutz (DSGVO/GDPR)** — Keine personenbezogenen Daten werden im Repo gespeichert.
5. **KI-Transparenz (EU AI Act Art. 50)** — KI-generierte Inhalte werden als solche gekennzeichnet.
6. **Nicht-Diskriminierung** — Geltend gemäß CODE_OF_CONDUCT.md (Contributor Covenant 2.1).

---

## Artikel 3 — Rollen und Verantwortlichkeiten

| Rolle | Beschreibung | Befugnisse |
|---|---|---|
| **Maintainer** | Verantwortlich für Releases, Branch-Schutz, Merge-Rechte | Merge in `main`, Release-Tags |
| **Contributor** | Reicht PRs ein, erstellt Issues | Fork, Branch, PR |
| **Reviewer** | Prüft Code/Docs, gibt Feedback | Approve/Request Changes |
| **Community Member** | Diskutiert, meldet Bugs | Issues, Discussions |

Aktueller Maintainer: **yoyo967** (yildirimyahya716@gmail.com)

---

## Artikel 4 — Entscheidungsprozesse

### 4.1 Alltägliche Entscheidungen
- Werden via PR + 1 Approval gemergt.
- Maintainer kann ohne Review mergen, wenn keine anderen aktiven Reviewer vorhanden.

### 4.2 Strukturelle Änderungen
- Änderungen an CONSTITUTION.md, LICENSE, CI-Pipeline oder Branch-Schutz
  erfordern ein öffentliches RFC (Request for Comments) als GitHub Discussion
  mit mindestens 72 Stunden Kommentarfrist.

### 4.3 ADR-Pflicht
- Architekturentscheidungen werden als ADR (Architecture Decision Record)
  unter `docs/adr/` dokumentiert.

---

## Artikel 5 — Compliance

### 5.1 EU AI Act (Artikel 50)
- Alle KI-generierten Texte, Briefings und Agenten-Outputs werden mit einem
  Hinweis `<!-- AI-GENERATED -->` oder äquivalentem Marker versehen.
- Das Projekt fällt unter die Kategorie "General Purpose AI" (GPAI) und
  unterliegt den entsprechenden Transparenzpflichten ab 2. August 2025.

### 5.2 DSGVO / GDPR
- Keine Speicherung personenbezogener Daten im Repository.
- `.env`-Dateien mit Credentials werden niemals committed (erzwungen via .gitignore).
- Google Cloud Credentials (`gcp-service-account.json`) sind lokal und nicht versioniert.

### 5.3 Open-Source-Lizenzen
- Code: MIT License (siehe `LICENSE`)
- Buchinhalte und Dokumente: Creative Commons CC-BY-4.0 (siehe `LICENSE-BOOKS`)
- Alle Abhängigkeiten müssen MIT-, Apache-2.0- oder kompatible Lizenzen haben.

---

## Artikel 6 — Branch-Strategie

| Branch | Zweck | Schutz |
|---|---|---|
| `main` | Produktionsstand | Protected, kein direkter Push |
| `fix/*` | Bugfixes und Hardening | PR erforderlich |
| `feat/*` | Neue Features | PR + Review erforderlich |
| `docs/*` | Dokumentation | PR erforderlich |
| `release/*` | Release-Vorbereitung | Maintainer only |

---

## Artikel 7 — Versionierung und Releases

- Das Projekt folgt **Semantic Versioning** (SemVer 2.0.0).
- CHANGELOG.md wird bei jedem Release gemäß Keep a Changelog-Format aktualisiert.
- Release-Tags folgen dem Schema `vMAJOR.MINOR.PATCH`.

---

## Artikel 8 — Amendments

Änderungen an dieser Constitution erfordern:
1. GitHub Discussion als RFC (min. 72h Kommentarfrist)
2. PR mit explizitem Verweis auf die Discussion
3. Merge durch Maintainer nach Ablauf der Frist

---

## Artikel 9 — Inkrafttreten

Dieses Dokument tritt mit dem Merge in den `main`-Branch in Kraft.
Vorherige mündliche oder informelle Absprachen werden hierdurch ersetzt.

---

*Berlin, 9. Juli 2026 — yoyo967*
