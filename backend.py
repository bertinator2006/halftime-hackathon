import json
import db_actions
from data_classes import Student
from error_classes import ServerException, InvalidInputException
# Student Functions
# This one registers a student and adds them to the database
# Returns nothing
def studentRegister(student: Student):
    db_actions.new_student(
        firstname=student.first_name,
        lastname=student.last_name,
        age=student.age,
        zid=student.zid,
        email=student.email,
        schoolemail=student.school_email,
        degree=student.degree,
        dstart=student.start_year,
        dend=student.end_year,
        clubsjoined=student.arc_clubs_joined,
        password=student.password
    )
    return

# Tries to log a user in
# Adds a current session on success
# Returns true on success and false on a failure
def studentLogin(username, password):
	user = db_actions.get_student_by_username(username)

	if user and user.password == password:
		return db_actions.new_student_session(user)
	else:
		raise InvalidInputException("Invalid password")

# Takes a zId as input and returns the details for that following zId
def studentGetDetails(zId):
    student = db_actions.get_student_details(zId)

    detailsDict = {
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age,
        "zid": student.zid,
        "email": student.email,
        "school_email": student.school_email,
        "degree": student.degree,
        "start_year": student.start_year,
        "end_year": student.end_year,
        "arc_clubs_joined": student.arc_clubs_joined
    }
    studentJSON = json.dumps(detailsDict)

    return studentJSON

# Given a dictonary of arugments to change and their new values, tries to change them
# Returns true on success and False on a failure
def studentUpdateDetails(session, **toChange):
    try:
        db_actions.update_student_details(session, toChange)
    except ValueError:
        return False
    
    return True

def studentFillForm():
    return

# Group functions
def groupRegister(name, members, password):
    db_actions.new_group(name, members, password)
    return

def groupAddStudent(groupId, zId):
    db_actions.group_add_member(groupId, zId)
    return

def groupRemoveStudent(groupId, Zid):
    db_actions.group_remove_member(groupId, Zid)
    return


def groupLogin(groupId, password):
    db_actions.group_login(groupId, password)
    return

def groupNewAtttendanceForm():

    return

def groupCheckForm():
    return