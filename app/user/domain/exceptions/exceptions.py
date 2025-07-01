class WeakPasswordError(Exception):
    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("Password does not meet security requirements.")
