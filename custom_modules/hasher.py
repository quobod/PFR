import bcrypt


def hash_password(arg):
    return bcrypt.hashpw(arg.encode('utf8'), bcrypt.gensalt(16))


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf8'), hashed)
