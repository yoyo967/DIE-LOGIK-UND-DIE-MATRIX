# CONTRIBUTING — DIE LOGIK & DIE MATRIX

> **"Wer dieses Repo betritt, betritt die Konstitution einer Frontier Firm.  
> Hier gelten Präzision, Kausalität und die Unveränderlichkeit der Chronik."**
> — MORPHEUS I AM, Prolog

---

## Willkommen in der Cocreationsmatrix

Dieses Repository ist die lebende DNA von **UNIVERSE M.E.** — einem Open-Source-Projekt, das KI-Infrastruktur, Agenten-Architektur und Dokumentation in einem einzigen, auditierbaren System vereint.

Jeder Beitrag wird Teil der unveränderlichen Chronik. Jeder Commit trägt einen SHA-Hash. Jede Entscheidung ist nachvollziehbar.

---

## Wie du beitragen kannst

### 1. Fork & Branch

```bash
# Repo forken (über GitHub UI)
git clone https://github.com/DEIN_USERNAME/DIE-LOGIK-UND-DIE-MATRIX.git
cd DIE-LOGIK-UND-DIE-MATRIX
git checkout -b feature/dein-beitrag
```

**Branch-Naming-Konventionen:**
- `feature/` — Neue Funktionen, Kapitel, Agenten
- `fix/` — Korrekturen in Dokumentation oder Code
- `docs/` — Reine Dokumentationsänderungen
- `compliance/` — EU AI Act / DSGVO / BSI A5 Updates
- `book/` — Buchkapitel (Undercover Blackbook / Sovereign / OMM)

### 2. Änderungen machen

- Halte dich an die bestehende Dateistruktur
- Markdown-Dateien: Präzise, kein Hype, keine unverifizierten Behauptungen
- Code: Python (FastAPI), HCL (Terraform), YAML
- Jede neue KI-Nutzung muss in `compliance/eu-ai-act-artikel50-log.md` eingetragen werden

### 3. Pull Request stellen

- PR-Titel: `[Typ]: Kurzbeschreibung` (z.B. `[book]: Kapitel 17 - Compliance Update`)
- Beschreibung: Was? Warum? Welches Problem löst du?
- Verknüpfe relevante Issues (`Closes #42`)
- Alle Diskussionen müssen resolved sein bevor Merge

### 4. Das Konzil-Protokoll

Große Architektur-Entscheidungen (ADRs) werden im `konzil-protokoll.md` dokumentiert.  
Nutze das Label `konzil` für Issues, die eine solche Entscheidung erfordern.

---

## Code of Conduct

Wir folgen dem **Pakt des offenen Wissens**:

- Respektvoller Umgang — keine persönlichen Angriffe
- Empirische Argumentation — Behauptungen müssen verifizierbar sein (Verifizierbarkeits-Codex)
- Keine Fiktion als Fakt — der AGENTS.md Verifizierbarkeits-Codex gilt für alle Beiträge
- Konstruktives Feedback — Kritik ist willkommen, Destruktion nicht

Verstöße können über GitHub Issues mit Label `compliance` gemeldet werden.

---

## Zielgruppen & Beitragstypen

| Zielgruppe | Typischer Beitrag | Label |
|-----------|-------------------|-------|
| Entwickler | Code, FastAPI, Terraform | `enhancement`, `agent` |
| Autoren | Buchkapitel, Dokumentation | `book`, `documentation` |
| Community | Übersetzungen, Diskussionen | `community`, `good first issue` |
| Compliance | EU AI Act Logs, DSGVO | `compliance` |
| Governance | Konzil-Entscheidungen | `konzil` |

---

## Quickstart für Contributor

```bash
# Dependencies installieren
pip install -r requirements.txt

# Local Bridge starten (opus-flow)
cd apps/local-bridge
python main.py
# → Läuft auf http://localhost:8000

# Health Check
curl http://localhost:8000/health
```

---

## Fragen & Kontakt

- **GitHub Discussions:** Für allgemeine Fragen und Community-Austausch
- **Issues:** Für konkrete Bugs, Feature Requests, Konzil-Entscheidungen
- **GDG Berlin:** Für lokale Community-Events

---

*WIR SIND NOCH HIER. — UNIVERSE M.E., Berlin, 2026*
