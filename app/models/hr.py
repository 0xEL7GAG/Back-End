from pydantic import BaseModel

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
     
class User_RequestQ(BaseModel):
    id: str 
    employee_id: str 
    name: str
    jopTitle: str
    requestType: str
    createdAt: str
    status: str

