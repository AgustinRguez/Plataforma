import bcrypt

def get_password_hash(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)
    return hashed.decode('utf-8')

def verify_password(password_verify: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password=password_verify.encode('utf-8'), hashed_password=hashed_password.encode('utf-8'))
