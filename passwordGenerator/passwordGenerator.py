import string
import secrets

# Returns a password between 8 and 60 characters in length. If length is invalid, length is set to default of 20
def generate_password(length: int=20, capitals: bool=True, digits: bool=True, symbols: bool=True):
    # password length must be between 8 and 60 characters in length
    if (length < 8 or length > 60): length = 20

    alphabet = string.ascii_lowercase
    if (capitals):
        alphabet += string.ascii_uppercase
    if (digits):
        alphabet += string.digits
    if (symbols):
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password