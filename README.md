# plan-model-orchestrator

Plan with one model, implement with another, verify with the planner.

## Use

Planner defaults to Sonnet 5.5 Max (`cu/claude-sonnet-5-5-max` on
OmniRoute); implementer inherits your session model.

```bash
cp config.example.json config.json   # optional: pin models
python3 plan-models.py config.json
# planner=cu/claude-sonnet-5-5-max implementer=session-default
```

Load `SKILL.md` as a Hermes skill for `/plan-orchestrated` + `/verify-plan`.
