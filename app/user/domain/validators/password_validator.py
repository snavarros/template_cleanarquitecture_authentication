import re


def validate_password_strength(password: str) -> list[str]:
    errors = []

    if len(password) < 8:
        errors.append("Must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("Must include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Must include at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        errors.append("Must include at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Must include at least one special character.")

    return errors
