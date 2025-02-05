import random
import string

def generate_user_id():
    prefix = "usr"
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}-{suffix}"