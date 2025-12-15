def explain(decision):
    final_status = decision.get("final_status")
    reasons = decision.get("reasons", [])
    raw = decision.get("raw", {})

    explanation = {
        "summary": "",
        "root_cause": "",
        "responsibility": "",
        "urgency": "",
        "recommendations": [],
    }

    # PASS
    if final_status == "PASS":
        explanation["summary"] = "System is healthy. No issues detected."
        explanation["root_cause"] = "All detectors passed."
        explanation["responsibility"] = "None"
        explanation["urgency"] = "None"
        explanation["recommendations"].append(
            "No action required. Continue normal monitoring."
        )
        return explanation

    # FAIL 
    if raw.get("reliability", {}).get("status") == "FAIL":
        explanation["summary"] = "System failed due to a reliability issue."
        explanation["root_cause"] = "Unhandled exception or repeated runtime errors."
        explanation["responsibility"] = "Developer"
        explanation["urgency"] = "Immediate"
        explanation["recommendations"].extend([
            "Inspect stack trace and logs for the crash.",
            "Fix the underlying bug causing the exception.",
            "Add tests to prevent regression."
        ])
        return explanation

    # FAIL — Functional
    if raw.get("function", {}).get("status") == "FAIL":
        explanation["summary"] = "System failed functional correctness checks."
        explanation["root_cause"] = "Test failures indicate incorrect program behavior."
        explanation["responsibility"] = "Developer"
        explanation["urgency"] = "Immediate"
        explanation["recommendations"].extend([
            "Review failed test cases.",
            "Fix incorrect logic in application code.",
            "Improve test coverage if needed."
        ])
        return explanation

    # FAIL — Security
    if raw.get("security", {}).get("status") == "FAIL":
        explanation["summary"] = "System failed due to security issues."
        explanation["root_cause"] = "Static security analysis detected vulnerabilities."
        explanation["responsibility"] = "Security / Developer"
        explanation["urgency"] = "High"
        explanation["recommendations"].extend([
            "Review security scan output.",
            "Fix or mitigate reported vulnerabilities.",
            "Re-run security checks after fixes."
        ])
        return explanation

    # WARN — Environmental
    if raw.get("environment", {}).get("status") == "FAIL":
        explanation["summary"] = "System warning due to environmental stress."
        explanation["root_cause"] = "High CPU load or resource contention detected."
        explanation["responsibility"] = "Infrastructure / DevOps"
        explanation["urgency"] = "Medium"
        explanation["recommendations"].extend([
            "Monitor system resource usage.",
            "Consider scaling resources or retrying later.",
            "No immediate code changes required."
        ])
        return explanation

    # WARN — Performance
    if raw.get("performance", {}).get("status") == "FAIL":
        explanation["summary"] = "System warning due to performance degradation."
        explanation["root_cause"] = "Slow execution or high resource usage detected."
        explanation["responsibility"] = "Developer"
        explanation["urgency"] = "Medium"
        explanation["recommendations"].extend([
            "Profile the slow functions.",
            "Optimize algorithms or data structures.",
            "Check if environment pressure contributed."
        ])
        return explanation

    # WARN — Static / Lint
    explanation["summary"] = "System warning due to code quality issues."
    explanation["root_cause"] = "Static analysis or linting warnings detected."
    explanation["responsibility"] = "Developer"
    explanation["urgency"] = "Low"
    explanation["recommendations"].extend([
        "Clean up lint and static analysis warnings.",
        "Improve code readability and maintainability.",
        "Address warnings gradually."
    ])

    return explanation
