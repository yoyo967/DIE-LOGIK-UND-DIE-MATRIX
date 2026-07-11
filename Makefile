.PHONY: run test lint audit tf-init tf-apply install

install:
	pip install -r requirements.txt
	pip install pytest pytest-asyncio httpx ruff pip-audit

run:
	uvicorn apps.local-bridge.main:app --host 127.0.0.1 --port 8000

test:
	pytest tests/ -v --tb=short

lint:
	ruff check apps/

audit:
	pip-audit -r requirements.txt --desc

tf-init:
	cd gcp-infra && terraform init

tf-apply:
	cd gcp-infra && terraform apply -var="project_id=universe-me-infinity"
