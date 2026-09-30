#!/usr/bin/env python3
"""Resolve planner/implementer models for plan-model-orchestrator.

Usage: plan-models.py [config.json]
Prints: planner=<model> implementer=<model|session-default>
"""
import json
import sys

DEFAULT_PLANNER = "cc/claude-sonnet-5-5"


def main(path=None):
    planner, implementer = DEFAULT_PLANNER, None
    if path:
        try:
            cfg = json.load(open(path))
            planner = cfg.get("planner", {}).get("model", planner)
            implementer = cfg.get("implementer", {}).get("model")
        except (OSError, json.JSONDecodeError) as e:
            print(f"warn: ignoring bad config: {e}", file=sys.stderr)
    print(f"planner={planner} implementer={implementer or 'session-default'}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
    # ponytail: no validation against /v1/models; add when typos waste runs.
