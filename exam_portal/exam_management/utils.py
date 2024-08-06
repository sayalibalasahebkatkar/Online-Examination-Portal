import jwt
from datetime import datetime, timedelta
from django.conf import settings

SECRET_KEY = 'your_secret_key'

def generate_access_token(user,flag=True):
    payload = {
        'user_id': user.id,
        'exp': datetime.now() + timedelta(hours=12),
        'iat': datetime.now(),
        'is_student':flag
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id'],payload['is_student']
    except jwt.ExpiredSignatureError:
        return 'expired'
    except jwt.InvalidTokenError:
        return 'invalid'
