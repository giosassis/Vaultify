import random
import string

def generate_pass_id():
    prefix = "psswd"
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}-{suffix}"