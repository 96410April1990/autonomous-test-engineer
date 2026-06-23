from app.execution.pytest_runner import ( PytestRunner )
from app.execution.result_parser import ( ResultParser )

class ExecutionService:

    def __init__(self):
        self.runner = PytestRunner()
        self.parser = ResultParser()

    def execute(self, test_path: str):
        result = self.runner.execute(test_path)
        return self.parser.parse(result["output"], result["duration"])
    
    