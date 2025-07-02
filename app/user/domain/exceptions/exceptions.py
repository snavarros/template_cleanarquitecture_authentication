class WeakPasswordError(Exception):
    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("Password does not meet security requirements.")


class EmailAlreadyExistsError(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"The email '{email}' is already in use."
        super().__init__(self.message)
