#!/usr/bin/env python3
"""
Demo runner for Scholar Goals OutreachForge agents.
"""

import sys
sys.path.insert(0, "src")

from crewai import Agent, Task, Crew, Process
from outreachforge.tools.custom_tools import (
    openalex_tool, crossref_tool, email_verifier_tool,
    suppression_tool, email_sender_tool
)

print("=" * 70)
print("  SCHOLAR GOALS – OUTREACHFORGE MULTI-AGENT SYSTEM")
print("  Loading all 6 agents...")
print("=" * 70)

scout = Agent(
    role="Academic Contact Discovery Specialist (Scout)",
    goal="Discover high-confidence public institutional emails of active researchers from OpenAlex, Crossref and university directories. Never invent data.",
    backstory="You are Scout, the most meticulous academic data hunter. You only use public sources.",
    tools=[openalex_tool, crossref_tool, email_verifier_tool],
    verbose=True,
    allow_delegation=False,
)

atlas = Agent(
    role="Research Profile Enrichment Specialist (Atlas)",
    goal="Resolve OpenAlex Author IDs and produce rich profiles with concrete personalization hooks from real recent works.",
    backstory="You are Atlas. You live inside the OpenAlex knowledge graph. Accuracy is non-negotiable.",
    tools=[openalex_tool, crossref_tool],
    verbose=True,
    allow_delegation=False,
)

scribe = Agent(
    role="Academic Outreach Copywriter (Scribe)",
    goal="Write short (<150 words), highly personalized, respectful cold emails that reference one real recent work and include compliance footer.",
    backstory="You are Scribe. You write the way a thoughtful research colleague would write – concise, specific, zero hype.",
    tools=[],
    verbose=True,
    allow_delegation=False,
)

sentinel = Agent(
    role="Compliance & Deliverability Gatekeeper (Sentinel)",
    goal="Review every email against CAN-SPAM, GDPR, CASL and quality rules. Approve, reject or escalate.",
    backstory="You are Sentinel. Nothing leaves the system without your explicit approval.",
    tools=[suppression_tool],
    verbose=True,
    allow_delegation=True,
)

courier = Agent(
    role="Email Delivery & Event Capture Specialist (Courier)",
    goal="Send only approved emails, capture events, and update suppression list on opt-out or bounce.",
    backstory="You are Courier. Rate-limit aware and obsessive about deliverability.",
    tools=[email_sender_tool, suppression_tool],
    verbose=True,
    allow_delegation=False,
)

oracle = Agent(
    role="Growth Analytics & Learning Specialist (Oracle)",
    goal="Measure the full pipeline and produce recommendations that improve Scout, Atlas and Scribe.",
    backstory="You are Oracle. You turn raw events into actionable intelligence.",
    tools=[],
    verbose=True,
    allow_delegation=False,
)

agents = [scout, atlas, scribe, sentinel, courier, oracle]

print("\n✅ 6 AGENTS SUCCESSFULLY CREATED:\n")
for i, agent in enumerate(agents, 1):
    print(f"{i}. {agent.role}")
    print(f"   Goal: {agent.goal[:80]}...")
    print()

print("=" * 70)
print("  Creating sequential Crew...")
print("=" * 70)

discover_task = Task(
    description="Discover academic contacts for seed: MIT Computer Science",
    expected_output="JSON list of contacts",
    agent=scout
)

enrich_task = Task(
    description="Enrich the discovered contacts with OpenAlex data",
    expected_output="JSON list of enriched profiles",
    agent=atlas,
    context=[discover_task]
)

crew = Crew(
    agents=agents,
    tasks=[discover_task, enrich_task],
    process=Process.sequential,
    verbose=True
)

print("\n✅ CREW CREATED SUCCESSFULLY")
print(f"   Process : Sequential")
print(f"   Agents  : {len(crew.agents)}")
print(f"   Tasks   : {len(crew.tasks)}")
print("=" * 70)
