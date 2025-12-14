import subprocess, sys

def run():
    print("Running lint...")
    subprocess.run([sys.executable, "-m", "flake8", "app", "tests"])
    print("sec check")
    subprocess.run([sys.executable,"-m", "bandit","-r","app"])
    print("Running tests...")
    subprocess.run([sys.executable, "-m", "pytest", "-q", "--disable-warnings"])

if __name__ == "__main__":
    run()