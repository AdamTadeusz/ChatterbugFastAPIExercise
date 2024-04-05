import string
import secrets

def generate_password(length: int=20, capitals: bool=True, digits: bool=True, symbols: bool=True):
    # password length must be between 8 and 60 characters in length
    length = max(8, length)
    length = min(60, length)

    alphabet = string.ascii_lowercase
    if (capitals):
        alphabet += string.ascii_uppercase
    if (digits):
        alphabet += string.digits
    if (symbols):
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password