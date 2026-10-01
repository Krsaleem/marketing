"""
Scholar Goals – OutreachForge Multi-Agent Crew
Six production agents: Scout → Atlas → Scribe → Sentinel → Courier → Oracle
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from outreachforge.tools.custom_tools import (
    openalex_tool,
    crossref_tool,
    email_verifier_tool,
    suppression_tool,
    email_sender_tool,
)


@CrewBase
class OutreachForgeCrew:
    """Always-on academic outreach multi-agent system for Scholar Goals"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def scout(self) -> Agent:
        return Agent(
            config=self.agents_config["scout"],
            tools=[openalex_tool, crossref_tool, email_verifier_tool],
            verbose=True,
            memory=True,
            allow_delegation=False,
        )

    @agent
    def atlas(self) -> Agent:
        return Agent(
            config=self.agents_config["atlas"],
            tools=[openalex_tool, crossref_tool],
            verbose=True,
            memory=True,
            allow_delegation=False,
        )

    @agent
    def scribe(self) -> Agent:
        return Agent(
            config=self.agents_config["scribe"],
            tools=[],
            verbose=True,
            memory=True,
            allow_delegation=False,
        )

    @agent
    def sentinel(self) -> Agent:
        return Agent(
            config=self.agents_config["sentinel"],
            tools=[suppression_tool],
            verbose=True,
            memory=True,
            allow_delegation=True,
        )

    @agent
    def courier(self) -> Agent:
        return Agent(
            config=self.agents_config["courier"],
            tools=[email_sender_tool, suppression_tool],
            verbose=True,
            memory=True,
            allow_delegation=False,
        )

    @agent
    def oracle(self) -> Agent:
        return Agent(
            config=self.agents_config["oracle"],
            tools=[],
            verbose=True,
            memory=True,
            allow_delegation=False,
        )

    @task
    def discover_contacts(self) -> Task:
        return Task(config=self.tasks_config["discover_contacts"])

    @task
    def enrich_profiles(self) -> Task:
        return Task(config=self.tasks_config["enrich_profiles"])

    @task
    def write_emails(self) -> Task:
        return Task(config=self.tasks_config["write_emails"])

    @task
    def compliance_check(self) -> Task:
        return Task(config=self.tasks_config["compliance_check"])

    @task
    def send_emails(self) -> Task:
        return Task(config=self.tasks_config["send_emails"])

    @task
    def analyze_and_learn(self) -> Task:
        return Task(config=self.tasks_config["analyze_and_learn"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
        )
