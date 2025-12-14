import traceback

def detect_exception(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        return {
            "failure_type": "reliability",
            "status": "PASS",
            "message": "No crash detected"
        }
    except Exception as e:
        return {
            "failure_type": "reliability",
            "status": "FAIL",
            "error_type": type(e).__name__,
            "error_message": str(e),
            "traceback": traceback.format_exc().splitlines()[:10]
        }


def analyze_logs(log_file="app.log", threshold=5):
    errors = []

    with open(log_file, "r") as f:
        for line in f:
            if "ERROR" in line or "CRITICAL" in line:
                errors.append(line)

    return {
        "failure_type": "reliability",
        "error_count": len(errors),
        "status": "FAIL" if len(errors) > threshold else "PASS",
        "sample_errors": errors[:5]
    }
