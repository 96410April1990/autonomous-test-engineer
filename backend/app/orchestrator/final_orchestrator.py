from app.orchestrator.production_orchestrator import ( ProductionQAOrchestrator )
from app.services.execution_service import ( ExecutionService )
from app.reporting.qa_report_generator import ( QAReportGenerator )

class FinalQAOrchestrator:
    def __init__(self):
        self.generator = (ProductionQAOrchestrator())
        self.executor = (ExecutionService())
        self.reporter = (QAReportGenerator())

    def run(self, requirement):
        result = (self.generator.run(requirement))
        files = (result["files_created"])
        execution_results = []
        for file in files:
            execution_results.append(self.executor.execute(file))
        total = 0
        passed = 0
        failed = 0
        failures = []

        for item in execution_results:
            total += item.total_tests
            passed += item.passed
            failed += item.failed

            failures.extend(item.failures)

        return self.reporter.generate(result["feature"], files, type("Execution",(),{"passed": passed,"failed": failed})(), failures)
        
