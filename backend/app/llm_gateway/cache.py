import hashlib

class PromptCache:
    def __init__(self):
        self.store = {}

    def key(self, prompt):
        return hashlib.md5(prompt.encode()).hexdigest()
    
    def get(self, prompt):
        return self.store.get(self.key(prompt))
    
    def save(self, prompt, response):
        self.store[self.key(prompt)] = response

        