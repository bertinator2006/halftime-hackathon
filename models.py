from sqlalchemy import Column, Integer, String, JSON
from database import Base

class AttendanceForm(Base):
    __tablename__ = "attendance_forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    fields = Column(JSON)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer)
    data = Column(JSON)

class 