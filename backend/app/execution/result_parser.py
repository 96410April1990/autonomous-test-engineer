import re
from app.models.execution_result import ( ExecutionResult, TestFailure )

class ResultParser:
    def parse(self, output: str, duration: float):
        passed = self.extract_number(output, "passed")
        failed = self.extract_number(output, "failed")
        total = passed + failed
        failures = []
        
        return ExecutionResult(total_tests=total, passed=passed, failed=failed, duration=duration, failures=failures)
    
    def extract_number(self, text, word):
        match=re.search(rf"(\d+)\s+{word}", text)
        if match:
            return int(match.group(1))
        
        return 0