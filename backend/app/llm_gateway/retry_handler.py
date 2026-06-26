import time

class RetryHandler:

    def execute(self, function, retries=3):
        attempt = 0
        while attempt < retries:
            try:
                return function()
            except Exception:
                attempt += 1
                time.sleep(attempt * 5)
        raise Exception("LLM failed after retries.")