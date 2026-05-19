from datetime import datetime
from data_classes import Student, get_student_data, get_attendance_form_data



# Functions
def add_student(first_name, last_name, age, zid, email, school_email, degree, course, start_year, end_year, degree_type):
    #TODO: Add validation for the input data
    data = get_student_data()
    student = Student(first_name, last_name, age, zid, email, school_email, degree, course, start_year, end_year, degree_type)
    data.append(student)


def login(username, password):
    result = 0

    # zid check
    result += check_zid(username)
    result += check_name(username)
    result += check_e(password)

    
    
    if 

def check_zid(zid) {
    

    
f (zid)}