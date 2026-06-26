from app.models.execution_report import ( ExecutionReport )

class QAReportGenerator:
    def generate(self, feature, generated_files, execution_result, failures):
        return ExecutionReport(feature=feature, tests_generated=len(generated_files), tests_passed=(execution_result.passed), tests_failed=(execution_result.failed), issues_found=failures)
    