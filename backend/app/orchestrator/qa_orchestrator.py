from app.agents.requirement_analyzer_agent import ( RequirementAnalyzerAgent )
from app.agents.test_architect_agent import ( TestArchitectAgent )
from app.agents.playwright_generator_agent import ( PlaywrightGeneratorAgent )
from app.services.execution_service import ( ExecutionService )
from app.models.execution_report import ( ExecutionReport )

class QAOrchestrator:

    def __init__(self):
        self.requirement_agent = (RequirementAnalyzerAgent())
        self.test_agent = (TestArchitectAgent())
        self.code_agent = (PlaywrightGeneratorAgent())
        self.executor = (ExecutionService())

    def run(self, requirement_text:str):
        requirement = (self.requirement_agent.analyze(requirement_text))
        tests = (self.test_agent.generate_tests(requirement.json()))

        generated_code = []

        for test in tests.test_cases:
            code = (self.code_agent.generate_code(test.json()))
            generated_code.append(code)

        #Execution will be connected when files are stored
        return ExecutionReport(feature=requirement.feature_name, tests_generated=len(tests.test_cases), tests_passed=0, tests_failed=0, issues_found=[])
    
    