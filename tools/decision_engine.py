def decide(error_dict):
    final_status = "PASS"
    reasons = []

    def get_status(block):
        if isinstance(block, dict):
            return block.get("status")
        return None

    hard_fail_keys = [
        "function",
        "reliability",
        "security",
        "tests",
    ]

    for key in hard_fail_keys:
        block = error_dict.get(key)
        if isinstance(block, dict):
            if block.get("status") == "FAIL":
                final_status = "FAIL"
                reasons.append(f"{key} failure")
    
    if final_status != "FAIL":
        warn_keys = [
            "environment",
            "performance",
            "static",
            "lint",
        ]

        for key in warn_keys:
            block = error_dict.get(key)
            if isinstance(block, dict):
                if block.get("status") == "FAIL":
                    final_status = "WARN"
                    reasons.append(f"{key} issue")

    return {
        "final_status": final_status,
        "reasons": reasons,
        "raw": error_dict,
    }
