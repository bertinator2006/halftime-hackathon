from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime


class Student(BaseModel):
   first_name: str = ""
   last_name: str = ""
   age: int = 0
   zid: str
   email: str = ""
   school_email: str = ""
   degree: str = ""
   start_year: int = 0
   end_year: int = 0
   arc_clubs_joined: List = Field(default_factory=list)
   password: str
   sessions: List[str] = Field(default_factory=list)

   def is_session(self, session_id: str) -> bool:
       return session_id in self.sessions


class FormField(BaseModel):
   name: str
   label: str
   field_type: str
   required: bool = True
   prefill: bool = False

   def convert_to_json(self) -> Dict:
       return {
           "name": self.name,
           "label": self.label,
           "field_type": self.field_type,
           "required": self.required,
           "prefill": self.prefill
       }

class AttendanceForm(BaseModel):
   title: str = "Default Attendance Form Title"
   fields: List[FormField]
   responses: List

class Group(BaseModel):
   name: str
   members: List[str] = Field(default_factory=list)
   sessions: List[str] = Field(default_factory=list)
   password: str
        