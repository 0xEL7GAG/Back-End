from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

fullDate = f"{datetime.now().day}-{datetime.now().month}-{datetime.now().year}"

class HrQ(BaseModel):
    id: str
    name: str
    salary: str
    jobTitle: str


class TasksQ(BaseModel):
    id: int
    task_name: str
    deadline: str
    calendar: str


class MeetingsQ(BaseModel):
    id: int
    name: str
    during_time: str
    calendar: str

class EventsQ(BaseModel):
    id: int
    name: str
    during_time: str
    calendar: str


class EmployeesQ(BaseModel):
    id: str
    name: str
    jopTitle: str
    salary:int
    projects:list | None = None
    checkIn: int=0 
    checkOut: int=0 
    StartOverTime: int=0 
    FinishOverTime: int=0
    Attendence:int =0
    numberOfOverTime:int=0

class EmployeesUQ(BaseModel):
    id: str
    name: str
    jopTitle: str
    salary: float
    projects: Optional[List[str]] = []
    checkIn: Optional[int] = None
    checkOut: Optional[int] = None
    StartOverTime: Optional[int] = None
    FinishOverTime: Optional[int] = None
    Attendence: Optional[int] = None
    numberOfOverTime: Optional[int] = None
     
class User_RequestQ(BaseModel):
    employee_id: str 
    name: str | None = None
    jopTitle: str | None = None
    requestType: str
    createdAt:str = fullDate
    status: str

