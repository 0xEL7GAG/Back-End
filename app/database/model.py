from typing import List, Optional
from sqlalchemy import JSON
from sqlmodel import Relationship, SQLModel, Field

class Hr(SQLModel, table=True):
    __tablename__ = "hr"
    id: str = Field(primary_key=True)
    name: str
    salary: str
    jobTitle: str
    check_in: int
    check_out: int
    start_over_time: int
    finish_over_time: int
    attendens: int
    number_of_over_time: int


class Tasks(SQLModel, table=True):
    __tablename__ = "tasks"  
    id: int = Field(primary_key=True, unique=True, index=True)
    task_name: str
    deadline: str


class Meetings(SQLModel, table=True):
    __tablename__ = "meetings"  # Table name
    id: int = Field(primary_key=True, unique=True, index=True)  # Unique ID
    name: str  # Meeting name
    during_time: str  # Duration or time of the meeting

class Events(SQLModel, table=True):
    __tablename__ = "events"  # Table name
    id: int = Field(primary_key=True, unique=True, index=True)  # Unique ID
    name: str  # Event name
    during_time: str  # Duration or time of the event

class Employees(SQLModel, table=True):
    __tablename__ = "employees"
    id: str = Field(primary_key=True)
    name: str
    jopTitle: str
    salary: int
    projects: Optional[List[str]] = Field(default=None, sa_type=JSON)
    checkIn: int
    checkOut: int
    StartOverTime: int
    FinishOverTime: int
    Attendence: int
    numberOfOverTime: int

    requests: List["User_Request"] = Relationship(back_populates="employee")



class User_Request(SQLModel, table=True):
    __tablename__ = "user_request"
    id:int = Field(default=None, primary_key=True)
    employee_id: str = Field(foreign_key="employees.id")
    requestType: str
    createdAt: str
    status: str
    employee: "Employees" = Relationship(back_populates="requests")
