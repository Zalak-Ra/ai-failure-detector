import subprocess, sys

def run(cmd):
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

def detect():
    results = []

    tools = {
        "flake8": [sys.executable, "-m", "flake8", "app"],
        "pylint": [sys.executable, "-m", "pylint", "app"],
        "mypy":   [sys.executable, "-m", "mypy", "app"],
        "bandit": [sys.executable, "-m", "bandit", "-r", "app"],
    }

    for name, cmd in tools.items():
        res = run(cmd)
        if res.returncode != 0:
            results.append({
                "tool": name,
                "issues": res.stdout.splitlines()[:10]
            })

    return {
        "failure_type": "static_analysis",
        "issues_found": len(results) > 0,
        "details": results
    }

if __name__ == "__main__":
    print(detect())
