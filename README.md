# Scholar Goals – OutreachForge Multi-Agent System

**Status: Agents created and ready**

This is a real CrewAI multi-agent crew with six specialized agents:

| Codename  | Role                                      | File location                  |
|-----------|-------------------------------------------|--------------------------------|
| Scout     | Academic Contact Discovery Specialist     | config/agents.yaml + crew.py   |
| Atlas     | Research Profile Enrichment Specialist    | config/agents.yaml + crew.py   |
| Scribe    | Academic Outreach Copywriter              | config/agents.yaml + crew.py   |
| Sentinel  | Compliance & Deliverability Gatekeeper   | config/agents.yaml + crew.py   |
| Courier   | Email Delivery & Event Capture            | config/agents.yaml + crew.py   |
| Oracle    | Growth Analytics & Learning               | config/agents.yaml + crew.py   |

## Project Structure

```
outreachforge/
├── src/outreachforge/
│   ├── config/
│   │   ├── agents.yaml      ← All 6 agent definitions (role, goal, backstory)
│   │   └── tasks.yaml       ← All 6 tasks with context chaining
│   ├── tools/
│   │   └── custom_tools.py  ← Stub tools (OpenAlex, Crossref, Email, Suppression)
│   ├── crew.py              ← Full Crew definition with @agent / @task / @crew
│   └── main.py              ← Entry point to run a pilot
└── README.md
```

## How to Run

```bash
pip install crewai crewai-tools
python -m outreachforge.main
```

## Current State

- All 6 agents are fully defined with roles, goals and backstories.
- Tasks are chained (Scout → Atlas → Scribe → Sentinel → Courier → Oracle).
- Custom tool stubs are in place.
- Sequential process is configured.
