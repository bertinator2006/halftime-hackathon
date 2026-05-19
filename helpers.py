import uuid
from data_classes import Student, get_student_data

def generate_session(entity):
    session = uuid.uuid4().hex
    entity.sessions.append(session)
    return session

def find_student_by_username(username) -> Student:
    students = get_student_data()
    for student in students:
        if student.zid == username or student.email == username or student.school_email == username:
            return student
    return None

def check_zid(zid):
    if len(zid) != 8:
        return False
    return True

def check_uni_email(email):
    return True

def check_personal_email(email):
    return True

    
