import psutil


def detect_environment():
    issues = []

    cpu_times = psutil.cpu_times_percent(interval=1)
    load_1, load_5, load_15 = psutil.getloadavg()

    cpu_user = cpu_times.user
    cpu_system = cpu_times.system
    cpu_idle = cpu_times.idle
    cpu_steal = getattr(cpu_times, "steal", 0.0)

    if cpu_user > 80:
        issues.append(f"High user CPU usage: {cpu_user}%")

    if cpu_idle < 20:
        issues.append(f"Low CPU idle time: {cpu_idle}%")

    if cpu_steal > 5:
        issues.append(f"High CPU steal time: {cpu_steal}% (VM contention)")

    cpu_count = psutil.cpu_count()
    if load_1 > cpu_count:
        issues.append(
            f"High system load: load_1={load_1}, cpu_count={cpu_count}"
        )

    return {
        "failure_type": "environmental",
        "status": "FAIL" if issues else "PASS",
        "issues": issues,
        "metrics": {
            "cpu_user": cpu_user,
            "cpu_system": cpu_system,
            "cpu_idle": cpu_idle,
            "cpu_steal": cpu_steal,
            "system_load_1": load_1,
            "cpu_count": cpu_count,
        }
    }


if __name__ == "__main__":
    print(detect_environment())
