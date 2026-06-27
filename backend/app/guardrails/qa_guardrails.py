class QAGuardrail:

    def validate_input(self, requirement):
        blocked_words = [
            "password",
            "secret",
            "api key",
            "delete database",
            "production database"
        ]

        for word in blocked_words:
            if word.lower() in requirement.lower():
                return False
            
        return True