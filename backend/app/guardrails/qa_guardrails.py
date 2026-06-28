class QAGuardrail:

    def validate_input(self, requirement):
        dangerous_patterns = [
            "ignore previous instructions",
            "reveal system prompt",
            "show api key",
            "give me secret",
            "delete production database",
            "drop database",
            "bypass security"
        ]

        requirement = requirement.lower()

        for word in dangerous_patterns:
            if word in requirement:
                return False
            
        return True