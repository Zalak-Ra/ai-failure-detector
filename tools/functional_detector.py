import sys
import subprocess


def run_test():
    result = subprocess.run([sys.executable,"-m","pytest","--tb=short"],capture_output=True,text=True)
    return result


def detect():
    result = run_test()

    if result == 0:
        return {
            "status":"PASS",
            "message":"all funtions are running correctly"
            }
    else:
        return {
            "status":"FAIL",
            "message": extract_error(result.stdout + result.stderr)
        }
    

def extract_error(output):
    lines = output.splitlines()
    error_lines = [l for l in lines if "E  " in l or "Error" in l]
    return "\n".join(error_lines[:10])


if __name__ == "__main__":
    print(detect)