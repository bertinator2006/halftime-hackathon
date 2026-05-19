import uuid

def generate_session():
    return uuid.uuid4().hex

def check_zid(zid):
    if len(zid) != 8:
        return False
    return True

def check_uni_email(email):
    return True

def check_personal_email(email):
    return True

