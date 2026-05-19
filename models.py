from sqlalchemy import Boolean, Column, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

from database import Base


class DbAttendanceForm(Base):
    __tablename__ = "attendance_forms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    responses = Column(JSON, default=list)
    fields = Column(JSON, default=list)


class DbStudent(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    zid = Column(String)
    email = Column(String)
    degree = Column(String)
    school_email = Column(String)
    start_year = Column(Integer)
    end_year = Column(Integer)
    arc_clubs_joined = Column(JSON)
    password = Column(String)
    sessions = Column(JSON, default=list)


class DbGroup(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    members = Column(JSON)  # List of student IDs
    sessions = Column(JSON, default=list)
    password = Column(String)

