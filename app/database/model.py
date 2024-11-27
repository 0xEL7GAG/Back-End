from typing import List, Optional
from sqlalchemy import JSON
from sqlmodel import Relationship, SQLModel, Field

class Hr(SQLModel, table=True):
    __tablename__ = "hr"
    id: str = Field(primary_key=True)
    name: str
    salary: str
    jobTitle: str
    check_in: int  # Check-in time
    check_out: int  # Check-out time
    start_over_time: int  # Start of overtime
    finish_over_time: int  # End of overtime
    attendens: int  # Attendance count
    number_of_over_time: int  # Number of overtime hours


class Tasks(SQLModel, table=True):
    __tablename__ = "tasks"  
    id: int = Field(primary_key=True, unique=True, index=True)
    task_name: str
    deadline: str
    calendar: str


class Meetings(SQLModel, table=True):
    __tablename__ = "meetings"  # Table name
    id: int = Field(primary_key=True, unique=True, index=True)  # Unique ID
    name: str  # Meeting name
    during_time: str  # Duration or time of the meeting
    calendar: str  # Calendar reference

class Events(SQLModel, table=True):
    __tablename__ = "events"  # Table name
    id: int = Field(primary_key=True, unique=True, index=True)  # Unique ID
    name: str  # Event name
    during_time: str  # Duration or time of the event
    calendar: str  # Calendar reference





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

    # Relationship with User_Request
    requests: List["User_Request"] = Relationship(back_populates="employee")



class User_Request(SQLModel, table=True):
    __tablename__ = "user_request"
    id: str = Field(primary_key=True)
    
    # Use foreign key to reference Employees' 'id' (which should be unique and a primary key)
    employee_id: str = Field(foreign_key="employees.id")  # Reference the 'id' field in Employees table
    
    # Optional: If you want to store the employee name and job title, don't make them foreign keys.
    # You can store them directly or use the related employee record for the name/title.
    name: str
    jopTitle: str

    requestType: str
    createdAt: str
    status: str

    # Relationship (Optional, if you want to easily access the employee from the request)
    employee: "Employees" = Relationship(back_populates="requests")
