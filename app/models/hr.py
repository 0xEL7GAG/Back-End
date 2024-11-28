from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

fullDate = f"{datetime.now().day}-{datetime.now().month}-{datetime.now().year}"

class HrQ(BaseModel):
    id: str
    name: str
    salary: str
    jobTitle: str
    check_in: int = 0
    check_out: int = 0
    start_over_time: int = 0
    finish_over_time: int = 0
    attendens: int = 0
    number_of_over_time: int = 0

class HrUQ(BaseModel):
    id: str
    name: str
    salary: str
    jobTitle: str
    check_in: Optional[int] = None
    check_out: Optional[int] = None
    start_over_time: Optional[int] = None
    finish_over_time: Optional[int] = None
    attendens: Optional[int] = None
    number_of_over_time: Optional[int] = None

class TasksQ(BaseModel):
    id: int
    task_name: str
    deadline: str


class MeetingsQ(BaseModel):
    id: int
    name: str
    during_time: str

class EventsQ(BaseModel):
    id: int
    name: str
    during_time: str


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
    requestType: str
    createdAt:str = fullDate
    status: str