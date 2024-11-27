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
    projects:list  | None = None
    checkIn: int
    checkOut: int
    StartOverTime: int
    FinishOverTime: int
    Attendence:int
    numberOfOverTime:int
