import os

class ArtifactManager:
    def __init__(self):
        self.base_path = "generated_tests"

    def save_files(self, files):
        os.makedirs(self.base_path, exist_ok=True)
        saved = []
        for file in files:
            path = os.path.join(self.base_path, file["file_name"])
            with open(path, "w") as f:
                f.write(file["code"])
            saved.append(path)

        return saved
    