import os

class RAGService:
    def __init__(self):
        self.path = "knowledge"

    def retrieve(self, query):
        context = []
        for file in os.listdir(self.path):
            full_path = os.path.join(self.path, file)
            with open(full_path, "r") as f:
                content = f.read()
                if any(word.lower() in content.lower() for word in query.split()):
                    context.append(content)

        return "\n".join(context)
    

        