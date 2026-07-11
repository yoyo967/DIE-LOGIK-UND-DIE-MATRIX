.PHONY: run test lint fmt audit security tf-init tf-apply install help docs

# Standardziel
help:
	@echo "Verfügbare Makefile-Targets:"
	@echo "  install   - Abhängigkeiten installieren"
	@echo "  run       - FastAPI lokal starten"
	@echo "  test      - Unit-Tests ausführen"
	@echo "  lint      - Ruff Linting"
	@echo "  fmt       - Ruff Auto-Format"
	@echo "  audit     - pip-audit Security-Check"
	@echo "  security  - Bandit Security-Scan"
	@echo "  tf-init   - Terraform initialisieren"
	@echo "  tf-apply  - Terraform apply (GCP)"
	@echo "  docs      - ADR-Verzeichnis auflisten"

install:
	pip install -r requirements.txt
	pip install pytest pytest-asyncio httpx ruff pip-audit bandit

run:
	uvicorn apps.local-bridge.main:app --host 127.0.0.1 --port 8000

test:
	pytest tests/ -v --tb=short

lint:
	ruff check apps/

fmt:
	ruff format apps/

audit:
	pip-audit -r requirements.txt --desc

security:
	bandit -r apps/ -ll -q

tf-init:
	cd gcp-infra && terraform init

tf-apply:
	cd gcp-infra && terraform apply -var="project_id=universe-me-infinity"

docs:
	@echo "Architecture Decision Records:"
	@ls docs/adr/ 2>/dev/null || echo "Kein docs/adr/ Verzeichnis gefunden"
