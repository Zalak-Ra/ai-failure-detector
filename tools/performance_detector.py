import time
import psutil
import os


def measure(func, *args, **kwargs):
    process = psutil.Process(os.getpid())

    cpu_before = process.cpu_percent(interval=None)
    mem_before = process.memory_info().rss

    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    cpu_after = process.cpu_percent(interval=None)
    mem_after = process.memory_info().rss

    metrics = {
        "execution_time_sec": round(end - start, 6),
        "cpu_delta_percent": cpu_after - cpu_before,
        "memory_delta_mb": round((mem_after - mem_before) / (1024 * 1024), 3),
    }

    return metrics, result


def detect_performance(metrics):
    issues = []

    if metrics["execution_time_sec"] > 0.5:
        issues.append("Slow execution")

    if metrics["cpu_delta_percent"] > 80:
        issues.append("High CPU usage")

    if metrics["memory_delta_mb"] > 50:
        issues.append("High memory usage")

    return {
        "failure_type": "performance",
        "status": "FAIL" if issues else "PASS",
        "issues": issues,
        "metrics": metrics
    }
