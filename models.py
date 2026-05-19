from sqlalchemy import Column, Integer, String, JSON, bool
from database import Base

class AttendanceForm(Base):
    __tablename__ = "attendance_forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    fields = Column(JSON)

class Student(Base):
    __tablename__ = "students"

    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    zid = Column(String)
    email = Column(String)
    school_email = Column(String)
    start_year = Column(Integer)
    end_year = Column(Integer)
    arc_clubs_joined = Column(JSON)
    password = Column(String)

class Group(Base):
    __tablename__ = "groups"
    name = Column(String)
    members = Column(JSON)  # List of student IDs
    

class AttendanceForm(Base):
    __tablename__ = "attendance_forms"
    title = Column(String)
    fields = Column(JSON)
    responses = Column(JSON)

class FormField(Base):
    name = Column(String)
    label = Column(String)
    field_type = Column(String)  # e.g., "text", "number", "email", etc.
    required = Column(bool)
    prefill = Column(bool)  # Optional prefill value for the field
 
    
