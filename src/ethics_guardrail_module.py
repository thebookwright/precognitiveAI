"""
ethics_guardrail_module.py

Applies ethical filters based on the Temporal Ethics Protocol (TEP).
Designed to review and potentially block foresight insights that cross ethical thresholds.
"""

def ethical_filter(insight: dict) -> bool:
    """
    Apply a basic ethical screening to the final insight.
    Returns True if ethically acceptable, False otherwise.
    """
    prohibited_terms = ["exploit", "manipulate", "gamble", "surveil"]
    content = str(insight).lower()
    for term in prohibited_terms:
        if term in content:
            print(f"⚠️ Ethical dissonance detected: '{term}' found.")
            return False
    return True

def apply_tep(insight: dict) -> dict:
    """
    Wraps the insight in an ethical review shell and annotates outcome.
    """
    if ethical_filter(insight):
        insight["tep_status"] = "cleared"
        print("✅ Insight cleared by Temporal Ethics Protocol.")
    else:
        insight["tep_status"] = "blocked"
        print("⛔ Insight blocked by Temporal Ethics Protocol.")
    return insight
