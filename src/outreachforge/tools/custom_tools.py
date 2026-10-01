"""
Stub custom tools for Scholar Goals OutreachForge.
Replace the placeholder implementations with real OpenAlex / Crossref / email / suppression logic.
"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class OpenAlexSearchInput(BaseModel):
    query: str = Field(..., description="Search query or OpenAlex filter")


class OpenAlexTool(BaseTool):
    name: str = "OpenAlex Search"
    description: str = (
        "Search OpenAlex for authors, works, institutions or topics. "
        "Use for discovery and enrichment."
    )
    args_schema: Type[BaseModel] = OpenAlexSearchInput

    def _run(self, query: str) -> str:
        # TODO: replace with real https://api.openalex.org calls
        return f"[STUB] OpenAlex results for: {query}"


class CrossrefTool(BaseTool):
    name: str = "Crossref Lookup"
    description: str = "Lookup DOI or work metadata from Crossref."

    def _run(self, doi_or_query: str) -> str:
        # TODO: real Crossref API
        return f"[STUB] Crossref data for: {doi_or_query}"


class EmailVerifierTool(BaseTool):
    name: str = "Email Verifier"
    description: str = "Check if an email address is deliverable and institutional."

    def _run(self, email: str) -> str:
        # TODO: real verification service
        return f"[STUB] Verification result for {email}: deliverable=True, institutional=True"


class SuppressionListTool(BaseTool):
    name: str = "Suppression List Manager"
    description: str = "Check or update the global suppression / opt-out list."

    def _run(self, action: str, email: str = "") -> str:
        # TODO: real Redis/Postgres suppression list
        return f"[STUB] Suppression action={action} email={email}"


class EmailSenderTool(BaseTool):
    name: str = "Transactional Email Sender"
    description: str = "Send an approved email via the transactional provider and return event id."

    def _run(self, to_email: str, subject: str, body: str) -> str:
        # TODO: real Postmark / SES / etc.
        return f"[STUB] Email queued to {to_email}. event_id=stub-123"


# Export all tools so agents can import them
openalex_tool = OpenAlexTool()
crossref_tool = CrossrefTool()
email_verifier_tool = EmailVerifierTool()
suppression_tool = SuppressionListTool()
email_sender_tool = EmailSenderTool()
