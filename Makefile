# Project: DMLS-Project
# Hardware: RTX 3050 (6GB VRAM)

PYTHON = venv/bin/python3
PIP = venv/bin/pip

.PHONY: help venv install run plot reports clean test

help:
	@echo "Available commands:"
	@echo "  make venv     : Create virtual environment"
	@echo "  make install  : Install dependencies"
	@echo "  make run      : Run the federated learning experiment"
	@echo "  make plot     : Generate result charts"
	@echo "  make reports  : Show report file locations"
	@echo "  make clean    : Remove checkpoints and logs"
	@echo "  make all      : Install, run, and plot"

venv:
	python3 -m venv venv

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) src/main.py

plot:
	$(PYTHON) src/plot_results.py

reports:
	@echo "Reports available in docs/:"
	@ls docs/report_*

clean:
	rm -rf checkpoints/*
	rm -rf results/*
	find . -type d -name "__pycache__" -exec rm -rf {} +

all: install run plot
