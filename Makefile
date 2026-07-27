PYTHON ?= python3

.PHONY: check compile validate

check: compile validate

compile:
	PYTHONPYCACHEPREFIX="$${TMPDIR:-/tmp}/redraft-pyc" \
		$(PYTHON) -m py_compile \
		scripts/validate_workspace.py \
		.codex/hooks/stop_validate_workspace.py

validate:
	$(PYTHON) scripts/validate_workspace.py
