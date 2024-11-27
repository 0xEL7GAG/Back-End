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


class ProfileQ(BaseModel):
    id: str  # Must match an existing Hr.id
    check_in: int
    check_out: int
    start_over_time: int
    finish_over_time: int
    attendens: int
    number_of_over_time: int
