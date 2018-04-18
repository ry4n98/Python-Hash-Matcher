import hashlib

def generate(val):
    h = hashlib.sha256()
    h.update(str(val))
    return h.hexdigest()
