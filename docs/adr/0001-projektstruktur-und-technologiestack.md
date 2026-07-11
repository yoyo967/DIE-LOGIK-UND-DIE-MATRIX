# ADR-0001: Projektstruktur und Technologiestack

**Datum:** 2026-07-09  
**Status:** Akzeptiert  
**Entscheider:** yoyo967  
**Reviewer:** Community (offen)

---

## Kontext

Das Projekt DIE LOGIK & DIE MATRIX benötigt eine klare, dokumentierte
Grundlage für seinen Technologiestack und seine Verzeichnisstruktur,
um neue Mitwirkende onboarden zu können und CI/CD-Pipelines aufzubauen.

## Entscheidung

Folgende Technologien und Struktur werden als Standard festgelegt:

### Sprachen
- **Python 3.11+** — Primäre Implementierungssprache (FastAPI, Agenten-Logic)
- **HCL (Terraform)** — Infrastruktur-as-Code für GCP
- **Markdown** — Dokumentation, Bücher, Governance-Dokumente

### Infrastruktur
- **Google Cloud Platform (GCP)** — europe-west3 (Frankfurt)
- **Terraform** — IaC-Tooling für GCP-Ressourcen
- **FastAPI** — REST-API-Framework für KI-Agenten

### Verzeichnisstruktur
```
/
├── .agents/          # KI-Agenten-Konfigurationen
├── .github/          # CI/CD, Templates, Dependabot
├── apps/             # FastAPI-Applikationen
├── books/            # Buchinhalte (CC-BY-4.0)
├── docs/adr/         # Architecture Decision Records
├── gcp-infra/        # Terraform-Konfigurationen
├── tests/            # Unit- und Integrationstests
└── *.md              # Governance, Community-Dokumente
```

### CI/CD
- GitHub Actions für Lint, Test, Security-Scan
- Ruff für Python-Linting (nicht-blockierend in Phase 1)
- Bandit für Security-Scanning
- pytest für Unit-Tests

## Konsequenzen

### Positiv
- Klare Trennung von Code, Infrastruktur und Dokumentation
- GCP europe-west3 erfüllt DSGVO-Anforderungen (Datenspeicherung in der EU)
- FastAPI ermöglicht schnelles Prototyping von KI-Agenten-APIs
- Terraform-State kann in GCS-Bucket versioniert werden

### Negativ / Trade-offs
- Python-Linting-Regeln müssen noch vollständig konfiguriert werden
- Terraform-State-Backend noch nicht in Remote (GCS) migriert
- Kein Multi-Cloud-Support in Phase 1

### Neutral
- Alternative: AWS + CDK wurde evaluiert, aber GCP wegen Kostenstruktur bevorzugt
- Alternative: Django wurde evaluiert, aber FastAPI wegen Performance bevorzugt

## Verwandte ADRs

- ADR-0002 (geplant): Lizenzstrategie und Dual-Licensing
- ADR-0003 (geplant): KI-Agenten-Architektur und EU AI Act Compliance

---

*Erstellt: 2026-07-09 — yoyo967*
