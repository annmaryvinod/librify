PYTHON ?= python3
BACKEND_DIR := backend
VENV_DIR := $(BACKEND_DIR)/.venv
VENV_BIN := $(VENV_DIR)/bin

.PHONY: help backend-venv backend-install backend-run migrate revision db-up db-down lint test

help:
	@echo "Common commands:"
	@echo "  make db-up            # start Postgres via docker compose"
	@echo "  make db-down          # stop Postgres container"
	@echo "  make backend-venv     # create backend virtualenv"
	@echo "  make backend-install  # install backend deps"
	@echo "  make backend-run      # start FastAPI with uvicorn"
	@echo "  make migrate          # run Alembic migrations"
	@echo "  make revision message='msg' # create Alembic revision"

backend-venv:
	cd $(BACKEND_DIR) && $(PYTHON) -m venv .venv

backend-install: backend-venv
	cd $(BACKEND_DIR) && . .venv/bin/activate && pip install -r requirements.txt

backend-run:
	cd $(BACKEND_DIR) && . .venv/bin/activate && uvicorn app.main:app --reload

migrate:
	cd $(BACKEND_DIR) && . .venv/bin/activate && alembic upgrade head

revision:
	cd $(BACKEND_DIR) && . .venv/bin/activate && alembic revision --autogenerate -m "$(message)"

db-up:
	docker compose up -d db

db-down:
	docker compose down

