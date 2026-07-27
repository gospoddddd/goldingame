#!/usr/bin/env python3
"""Run the Redraft workspace validator from a Codex Stop hook."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate_workspace.py"


def read_event() -> dict[str, object]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        parsed = json.loads(raw)
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        return {}


def main() -> int:
    event = read_event()
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=12,
    )

    if result.returncode == 0:
        print(json.dumps({"continue": True}))
        return 0

    message = (result.stdout + result.stderr).strip()
    if event.get("stop_hook_active"):
        print(
            json.dumps(
                {
                    "continue": True,
                    "systemMessage": (
                        "Redraft workspace validation is still failing: " + message
                    ),
                }
            )
        )
        return 0

    print(
        json.dumps(
            {
                "decision": "block",
                "reason": (
                    "Fix the Redraft workspace validation errors before finishing:\n"
                    + message
                ),
            }
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
