class User:
    def __init__(
        self, name: str, last_name: str, email: str, hashed_password: str, role_id: int
    ):
        if "@" not in email:
            raise ValueError("Invalid email")

        self.name = name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hashed_password
        self.role_id = role_id
