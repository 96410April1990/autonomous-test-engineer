from app.agents.requirement_analyzer_agent import ( RequirementAnalyzerAgent )
from app.agents.test_architect_agent import ( TestArchitectAgent )
from app.llm.batch_generator import ( BatchPlayWrightGenerator )
from app.artifacts.artifact_manager import ( ArtifactManager )

class ProductionQAOrchestrator:
    def __init__(self):
        self.requirement_agent = (RequirementAnalyzerAgent())
        self.test_agent = (TestArchitectAgent())
        self.generator = (BatchPlayWrightGenerator())
        self.artifacts = (ArtifactManager())

    def run(self, requirement:str):
        analysis = (self.requirement_agent.analyze(requirement))
        tests = (self.test_agent.generate_tests(analysis.json()))
        test_cases = tests.test_cases
        # if not test_cases:
        #     raise Exception(f"Invalid Test Architect response: {tests}")
        generated = (self.generator.generate(test_cases))
        saved_files = (self.artifacts.save_files(generated["files"]))

        return { "feature": analysis.feature_name, "files_created": saved_files }
    
