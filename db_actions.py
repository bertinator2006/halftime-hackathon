from database import SessionLocal
from models import DbStudent, DbGroup, DbAttendanceForm   
import helpers
from error_classes import NotFoundException

def get_last_id():
    db = SessionLocal()
    try:
        last_student = db.query(DbStudent).order_by(DbStudent.id.desc()).first()
        last_group = db.query(DbGroup).order_by(DbGroup.id.desc()).first()
        last_form = db.query(DbAttendanceForm).order_by(DbAttendanceForm.id.desc()).first()
        last_id = max(
            last_student.id if last_student else 0,
            last_group.id if last_group else 0,
            last_form.id if last_form else 0
        )
        return last_id
    except Exception as e:
        raise e
    finally:
        db.close()

def generate_id():
    return get_last_id() + 1


# get student by "username"
def get_student_by_username(username):
    db = SessionLocal()
    try:
        students = db.query(DbStudent).all() # Gets all students from the database
        # Check if the username matches zid, email, or school_email
        student = students.filter(DbStudent.zid == username).first()
        if student is None:
            student = students.filter(DbStudent.email == username).first()
        if student is None:
            student = students.filter(DbStudent.school_email == username).first()
        if student is None:
            raise NotFoundException(item_id=username)
        return student
    except Exception as e:
        raise e
    finally:
        db.close()

# get group by "group name"
def get_group_by_groupname(group_name):
    db = SessionLocal()
    try:
        group = db.query(DbGroup).filter(DbGroup.name == group_name).first()
        if group is None:
            raise NotFoundException(item_id=group_name)
        return group
    except Exception as e:
        raise e
    finally:
        db.close()

# check if a certain user session exists (you are given just the session id)
def check_valid_user_session(session):
    db = SessionLocal()
    try:
        students = db.query(DbStudent).all()
        return any(session in (student.sessions or []) for student in students)
    except Exception as e:
        raise e
    finally:
        db.close()
# check if a certain group session exists (you are given just the session id)
def check_valid_group_session(session):
    db = SessionLocal()
    try:
        groups = db.query(DbGroup).all()
        return any(session in (group.sessions or []) for group in groups)
    except Exception as e:
        raise e
    finally:
        db.close()

# new session for student
def new_student_session(id):
    db = SessionLocal()
    try:
        session = helpers.generate_session()
        student = db.query(DbStudent).filter(DbStudent.id == id).first()
        if student is None:
            raise NotFoundException(zid=id)
        student.sessions = (student.sessions or []) + [session]
        db.commit()
        return session
    except Exception as e:
        raise e
    finally:
        db.close()

# new session for group
def new_group_session(id):
    db = SessionLocal()
    try:
        session = helpers.generate_session()
        groups = db.query(DbGroup).filter(DbGroup.id == id).first()
        if groups is None:
            raise NotFoundException(item_id=id)
        groups.sessions = (groups.sessions or []) + [session]
        db.commit()
        return session
    except Exception as e:
        raise e
    finally:
        db.close()

# Create a new student
def new_student(firstname, lastname, age, zid, email, school_email, start_year, end_year, clubs_joined, password):
    db = SessionLocal()
    try:
        new_student = DbStudent(
            first_name=firstname,
            last_name=lastname,
            age=age,
            zid=zid,
            email=email,
            school_email=school_email,
            start_year=start_year,
            end_year=end_year,
            arc_clubs_joined=clubs_joined,
            password=password,
            id=generate_id(),
            sessions=[]
        )
        db.add(new_student)
        db.commit()
    except Exception as e:
        raise e
    finally: 
        db.close()

# name of a new group, list of members (zids), and password. For organisers
def new_group(name, members, password):
    db = SessionLocal()
    try:
        new_group = DbGroup(
            name=name,
            members=members,
            sessions=helpers.generate_session(),
            id=generate_id(), 
            password=password
        )
        
        db.add(new_group)
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()

def group_add_member(group_id, student_zid):
    db = SessionLocal()
    try:
        group = db.query(DbGroup).filter(DbGroup.id == group_id).first()
        if group is None:
            raise NotFoundException(item_id=group_id)
        student = db.query(DbStudent).filter(DbStudent.zid == student_zid).first()
        if student is None:
            raise NotFoundException(item_id=student_zid)
        group.members = (group.members or []) + [student_zid]
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()

def group_remove_member(group_id, student_zid):
    db = SessionLocal()
    try:
        group = db.query(DbGroup).filter(DbGroup.id == group_id).first()
        if group is None:
            raise NotFoundException(item_id=group_id)
        group.members = [member for member in (group.members or []) if member != student_zid]
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()

# get student details by zid
def get_student_details(zid):
    db = SessionLocal()
    try:
        student = db.query(DbStudent).filter(DbStudent.zid == zid).first()
        if student is None:
            raise NotFoundException(item_id=zid)
        return student
    except Exception as e:
        raise e
    finally:
        db.close()  

# update student details
def update_student_details(session, **kwargs):
    db = SessionLocal()
    try:
        students = db.query(DbStudent).all()
        student = next((s for s in students if session in (s.sessions or [])), None)
        if student is None:
            raise NotFoundException(item_id=session)
        #kwargs contains a dict of the fields to change
        #We go through each key value pair and update the student object accordingly
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        db.add(student)
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()
    return

# new attendance form
def new_attendance_form(title, responses, fields):
    db = SessionLocal()
    try:
        new_form = DbAttendanceForm(
            title=title, 
            responses=responses, 
            fields=fields
        )
        db.add(new_form)
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()
    return

# user fills form
def user_fills_form(zid, attendance_form_id): 
    db = SessionLocal()
    try:
        attendance_form = db.query(DbAttendanceForm).filter(DbAttendanceForm.id == attendance_form_id).first()
        if attendance_form is None:
            raise NotFoundException(item_id=attendance_form_id)
        # Here you would have logic to determine what the student's response is and add it to the attendance form's responses
        # For example, let's say we just add the student's zid to the responses to indicate they attended
        attendance_form.responses = (attendance_form.responses or []) + [zid]
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()
    return
    
# group check attedance for a particular form
# Returns a dictionary where the keys are the group members zids and the values are booleans indicating whether that member attended or not
def group_check_attendance_form(group_id, attendance_form_id):
    db = SessionLocal()
    try:
        attendance_form = db.query(DbAttendanceForm).filter(DbAttendanceForm.id == attendance_form_id).first()
        if attendance_form is None:
            raise NotFoundException(item_id=attendance_form_id)
        group = db.query(DbGroup).filter(DbGroup.id == group_id).first()
        if group is None:
            raise NotFoundException(item_id=group_id)
        
        # Create the attendance dictionary
        attended = {
            member: member in (attendance_form.responses or [])
            for member in group.members or []
        }

        return attended

    except Exception as e:
        raise e

    finally:
        db.close()
# logs out a user/group by removing the session from their sessions list
def logout(session):
    db = SessionLocal()
    try:
        students = db.query(DbStudent).all()
        for student in students:
            if session in (student.sessions or []):
                student.sessions = [s for s in (student.sessions or []) if s != session]
                db.add(student)
        groups = db.query(DbGroup).all()
        for group in groups:
            if session in (group.sessions or []):
                group.sessions = [s for s in (group.sessions or []) if s != session]
                db.add(group)
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()