import subprocess


def llm_explain(final_decision, explanation, model="tinyllama"):
    """
    Converts rule-based explanation into a clean,
    human-readable report using a local Ollama model.
    """

    prompt = f"""
You are writing a clear system failure report for a human user.

Write in plain English.
Do NOT mention JSON.
Do NOT show raw data.
Do NOT repeat tool names unless necessary.

Structure your response like this:

1. Overall Status
2. What went wrong
3. Why it happened
4. What to do next

System status: {final_decision.get("final_status")}

Rule-based explanation:
{explanation}
"""

    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout.strip()
