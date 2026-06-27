class JiraTool:

    def get_requirement(self, ticket):
        return f"""
        Requirement from Jira ticket: {ticket}

        Requirement:
        User should login successfully.

        Negative:
        Invalid password rejected.
        """
