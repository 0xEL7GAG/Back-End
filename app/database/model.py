from sqlmodel import Relationship, SQLModel, Field

class Hr(SQLModel, table=True):
    __tablename__ = "hr"
    id: str = Field(primary_key=True)
    name: str
    salary: str
    jobTitle: str


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


class Profile(SQLModel, table=True):
    __tablename__ = "profiles"  # Name of the table
    id: str = Field(primary_key=True, foreign_key="hr.id")  # Foreign key referencing Hr.id
    check_in: int  # Check-in time
    check_out: int  # Check-out time
    start_over_time: int  # Start of overtime
    finish_over_time: int  # End of overtime
    attendens: int  # Attendance count
    number_of_over_time: int  # Number of overtime hours

    # Relationship field (optional)
    hr: "Hr" = Relationship(back_populates="profile")

