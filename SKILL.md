---
name: plan-model-orchestrator
description: Plan with one model, implement with another, verify with the planner. Use when the user wants plan mode on a specific model (e.g. Sonnet 5.5 Max as planner/orchestrator) while implementation runs on the session model.
version: 1.0.0
metadata:
  hermes:
    tags: [plan-mode, model-routing, orchestrator, planning]
---

# Plan-Model Orchestrator

Plan on model A, implement on model B, verify on A.

## How it works

1. **Plan** — write the plan per the `plan` skill (`.hermes/plans/`,
   bite-sized TDD tasks). The plan file's frontmatter pins the planner:
   `planner_model: cu/claude-sonnet-5-5-max`.
2. **Implement** — each task spawns via `delegate_task` (inherits the
   session model) or `hermes chat -q -m <implementer> --skills plan`.
3. **Verify** — after all tasks pass, re-read the plan + diffs as the
   planner and either approve or file fix-up tasks. Loop until clean.

Default planner is `cc/claude-sonnet-5-5` (override in
`config.json`). Copy `config.example.json` to `config.json` to pin
both models.

## Commands

- `/plan-orchestrated <task>` — plan with the planner model, save plan.
- `/verify-plan` — planner re-reads plan + implementation, approves or
  files fix-ups.

## Notes

- Planner model must exist on your provider (`/v1/models` on OmniRoute
  lists `cu/claude-sonnet-5-5-*` variants).
- `ponytail:` single planner/verify loop; add multi-reviewer quorum when
  one pass misses defects.
