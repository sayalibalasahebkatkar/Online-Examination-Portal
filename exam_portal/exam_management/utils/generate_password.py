import secrets
import string

def generate_strong_password(self, length=12):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password