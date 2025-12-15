import subprocess
import sys

from tools.functional_detector import detect as functional_detect
from tools.static_detector import detect as static_detect
from tools.performance_detector import measure, detect_performance
from tools.reliability_detector import detect_exception, analyze_logs
from tools.environment_detector import detect_environment

from tools.decision_engine import decide
from tools.explainer import explain
from tools.suggest import llm_explain

from app.service import crash, slow_function


def run():
    raw_result = {}

    print("========== FUNCTIONAL CHECK ==========")
    raw_result["function"] = functional_detect()
    print(raw_result["function"])

    print("\n========== STATIC ANALYSIS ==========")
    raw_result["static"] = static_detect()
    print(raw_result["static"])

    print("\n========== PERFORMANCE CHECK ==========")
    metrics, _ = measure(slow_function, 3000)
    raw_result["performance"] = detect_performance(metrics)
    print(raw_result["performance"])

    print("\n========== LINT CHECK ==========")
    lint = subprocess.run(
        [sys.executable, "-m", "flake8", "app", "tests"],
        check=False,
        text=True,
        capture_output=True,
    )
    raw_result["lint"] = {
        "status": "FAIL" if lint.returncode != 0 else "PASS",
        "output": (lint.stdout or "") + (lint.stderr or ""),
    }

    print("\n========== SECURITY CHECK ==========")
    sec = subprocess.run(
        [sys.executable, "-m", "bandit", "-r", "app"],
        check=False,
        text=True,
        capture_output=True,
    )
    raw_result["security"] = {
        "status": "FAIL" if sec.returncode != 0 else "PASS",
        "output": (sec.stdout or "") + (sec.stderr or ""),
    }

    print("\n========== RELIABILITY CHECK ==========")
    raw_result["reliability"] = {
        "exception": detect_exception(crash),
        "logs": analyze_logs(),
    }
    print(raw_result["reliability"])

    print("\n========== ENVIRONMENT CHECK ==========")
    raw_result["environment"] = detect_environment()
    print(raw_result["environment"])

    # ---------- STEP 8 ----------
    final_decision = decide(raw_result)
    print("\n========== FINAL DECISION ==========")
    print(final_decision)

    # ---------- STEP 9 ----------
    explanation = explain(final_decision)
    print("\n========== RULE-BASED EXPLANATION ==========")
    print(explanation)

    # ---------- STEP 10 (OPTIONAL, SAFE) ----------
    print("\n========== AI EXPLANATION (OLLAMA) ==========")
    try:
        ai_explanation = llm_explain(final_decision, explanation)
        print(ai_explanation)
    except Exception as e:
        print("AI explanation unavailable. Falling back to rule-based explanation.")
        print(f"Reason: {e}")

    return {
        "raw": raw_result,
        "final_decision": final_decision,
        "explanation": explanation,
    }


if __name__ == "__main__":
    run()
