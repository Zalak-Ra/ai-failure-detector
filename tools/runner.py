import subprocess
import sys

from tools.functional_detector import detect as functional_detect
from tools.static_detector import detect as static_detect
from tools.performance_detector import measure, detect_performance

from app.service import slow_function


def run():
    print("========== FUNCTIONAL CHECK ==========")
    functional_report = functional_detect()
    print(functional_report)

    print("\n========== STATIC ANALYSIS ==========")
    static_report = static_detect()
    print(static_report)

    print("\n========== PERFORMANCE CHECK ==========")
    metrics, _ = measure(slow_function, 3000)
    performance_report = detect_performance(metrics)
    print(performance_report)

    print("\n========== LINT CHECK ==========")
    subprocess.run(
        [sys.executable, "-m", "flake8", "app", "tests"],
        check=False
    )

    print("\n========== SECURITY CHECK ==========")
    subprocess.run(
        [sys.executable, "-m", "bandit", "-r", "app"],
        check=False
    )

    print("\n========== TEST EXECUTION ==========")
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--disable-warnings"],
        check=False
    )


if __name__ == "__main__":
    run()
