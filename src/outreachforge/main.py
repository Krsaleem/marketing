#!/usr/bin/env python
"""
Entry point for Scholar Goals OutreachForge multi-agent system.
"""

from outreachforge.crew import OutreachForgeCrew


def run():
    inputs = {
        "seeds": [
            "Massachusetts Institute of Technology Computer Science",
            "Stanford University Artificial Intelligence",
            "University of California Berkeley Electrical Engineering"
        ]
    }

    print("=" * 60)
    print("Scholar Goals – OutreachForge Multi-Agent System")
    print("Agents: Scout → Atlas → Scribe → Sentinel → Courier → Oracle")
    print("=" * 60)

    result = OutreachForgeCrew().crew().kickoff(inputs=inputs)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)
    print(result)
    return result


if __name__ == "__main__":
    run()
