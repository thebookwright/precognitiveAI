"""
test_simulator.py

Basic test of the FFFBF simulation logic and ethical filtering module.
"""

from src.ff_f_f_bf_simulator import run_fffbf_simulation
from src.ethics_guardrail_module import apply_tep

def test_simulation_and_tep():
    seed_state = {"confidence": 0.9, "alignment": 0.95}
    insight = run_fffbf_simulation(seed_state)
    final_result = apply_tep(insight)

    assert "tep_status" in final_result
    assert final_result["tep_status"] in ["cleared", "blocked"]

    print("Test completed. Result:", final_result["tep_status"])

if __name__ == "__main__":
    test_simulation_and_tep()
