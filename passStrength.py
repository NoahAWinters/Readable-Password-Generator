import string


def validate_password(password):
    if (len(password) < 8):
        return False
    has_lowercase = any(
        [1 if c in string.ascii_lowercase else 0 for c in password])
    has_uppercase = any(
        [1 if c in string.ascii_uppercase else 0 for c in password])
    has_number = any(
        [1 if c in string.digits else 0 for c in password])
    has_symbol = any(
        [1 if c in string.punctuation else 0 for c in password])
