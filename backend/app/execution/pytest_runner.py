import subprocess
import time

class PytestRunner:
    def execute(self, test_path: str):
        start = time.time()
        process = subprocess.run(["pytest", test_path, "-v"], capture_output=True, text=True)
        duration = (time.time() - start)

        return { "output": process.stdout + process.stderr, "duration": duration }