from sqlmodel import create_engine, Session, SQLModel, select, delete
from fastapi import FastAPI, Depends, HTTPException
from app.database.model import Employees, Events, Hr, Meetings, Profile, Tasks
from app.models.hr import EmployeesQ, EventsQ, HrQ, MeetingsQ, ProfileQ, TasksQ
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")

app = FastAPI()

engine = create_engine(DB_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

@app.on_event(event_type="startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/api/hr", tags=["Hr"])
def get_all_hr_info(session: Session = Depends(get_session)):
    statment = select(Hr)
    result = session.exec(statment).all()
    return {"message": result}

@app.post("/api/hr", tags=["Hr"])
def create_new_hr(hr: HrQ, session: Session = Depends(get_session)):
    statment = select(Hr).where(Hr.id == hr.id)
    result = session.exec(statment)

    if result:
        return {"message": "This hr already exist"}
    
    new_hr = Hr(id=hr.id, name=hr.name, salary=hr.salary, jobTitle=hr.jobTitle)
    session.add(new_hr)
    session.commit()
    return {"message": "New Hr created"}

@app.get("/api/hr/{id}", tags=["Hr"])
def get_hr_by_id(id: str, session: Session = Depends(get_session)):
    statment = select(Hr).where(Hr.id == id)
    result = session.exec(statment).first()

    if not result:
        return {"message": "This hr not found"}
    
    return {"message": result}

@app.delete("/api/hr/{hr_id}", tags=["Hr"])
def delete_exist_hr(hr_id: str, session: Session = Depends(get_session)):
    statment = select(Hr).where(Hr.id == hr_id)
    result = session.exec(statment)

    if not result:
        return {"message": "This hr not found"}
    
    session.delete(result)
    session.commit()

    return {"message": "Hr deleted succeful"}



# Tasks

@app.get("/api/tasks", tags=["Tasks"])
def get_all_tasks(session: Session = Depends(get_session)):
    statement = select(Tasks)
    result = session.exec(statement).all()
    return {"tasks": result}

@app.post("/api/tasks", tags=["Tasks"])
def create_task(task: TasksQ, session: Session = Depends(get_session)):
    statement = select(Tasks).where(Tasks.id == task.id)
    result = session.exec(statement).first()

    if result:
        return {"message": "Task with this ID already exists"}

    new_task = Tasks(id=task.id, task_name=task.task_name, deadline=task.deadline, calendar=task.calendar)
    session.add(new_task)
    session.commit()
    return {"message": "Task created successfully"}

@app.get("/api/tasks/{id}", tags=["Tasks"])
def get_task_by_id(id: int, session: Session = Depends(get_session)):
    statement = select(Tasks).where(Tasks.id == id)
    result = session.exec(statement).first()

    if not result:
        return {"message": "Task not found"}
    return {"task": result}

@app.delete("/api/tasks/{id}", tags=["Tasks"])
def delete_task(id: int, session: Session = Depends(get_session)):
    statement = select(Tasks).where(Tasks.id == id)
    result = session.exec(statement).first()

    if not result:
        return {"message": "Task not found"}

    session.delete(result)
    session.commit()
    return {"message": "Task deleted successfully"}


# Meetings

@app.get("/api/meetings", tags=["Meetings"])
def get_all_meetings(session: Session = Depends(get_session)):
    statement = select(Meetings)
    result = session.exec(statement).all()
    return {"meetings": result}

@app.post("/api/meetings", tags=["Meetings"])
def create_meeting(meeting: MeetingsQ, session: Session = Depends(get_session)):
    statement = select(Meetings).where(Meetings.id == meeting.id)
    result = session.exec(statement).first()

    if result:
        return {"message": "Meeting with this ID already exists"}

    new_meeting = Meetings(id=meeting.id, name=meeting.name, during_time=meeting.during_time, calendar=meeting.calendar)
    session.add(new_meeting)
    session.commit()
    return {"message": "Meeting created successfully"}

@app.get("/api/meetings/{id}", tags=["Meetings"])
def get_meeting_by_id(id: int, session: Session = Depends(get_session)):
    statement = select(Meetings).where(Meetings.id == id)
    result = session.exec(statement).first()

    if not result:
        return {"message": "Meeting not found"}
    return {"meeting": result}

@app.delete("/api/meetings/{id}", tags=["Meetings"])
def delete_meeting(id: int, session: Session = Depends(get_session)):
    statement = select(Meetings).where(Meetings.id == id)
    result = session.exec(statement).first()

    if not result:
        return {"message": "Meeting not found"}

    session.delete(result)
    session.commit()
    return {"message": "Meeting deleted successfully"}



#Events

@app.get("/api/events", tags=["Events"])
def get_all_events(session: Session = Depends(get_session)):
    statement = select(Events)
    result = session.exec(statement).all()
    return {"events": result}

@app.post("/api/events", tags=["Events"])
def create_event(event: EventsQ, session: Session = Depends(get_session)):
    statement = select(Events).where(Events.id == event.id)
    result = session.exec(statement).first()

    if result:
        return {"message": "Event with this ID already exists"}

    new_event = Events(id=event.id, name=event.name, during_time=event.during_time, calendar=event.calendar)
    session.add(new_event)
    session.commit()
    return {"message": "Event created successfully"}

@app.get("/api/events/{id}", tags=["Events"])
def get_event_by_id(id: int, session: Session = Depends(get_session)):
    statement = select(Events).where(Events.id == id)
    result = session.exec(statement).first()

    if not result:
        return {"message": "Event not found"}
    return {"event": result}

@app.delete("/api/events/{id}", tags=["Events"])
def delete_event(id: int, session: Session = Depends(get_session)):
    statement = select(Events).where(Events.id == id)
    result = session.exec(statement).first()

    if not result:
        return {"message": "Event not found"}

    session.delete(result)
    session.commit()
    return {"message": "Event deleted successfully"}


@app.get("/api/employees", tags=["Employees"])
def get_all_employees(session: Session = Depends(get_session)):
    statment = select(Employees)
    result = session.exec(statment).all()
    return {"message": result}

@app.get("/api/employees/{id}", tags=["Employees"])
def get_employee_by_id(id: str, session: Session = Depends(get_session)):
    statment = select(Employees).where(Employees.id == id)
    result = session.exec(statment).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="This is user is not exists")
    
    return {"message": result}

@app.post("/api/employees", tags=["Employees"])
def create_new_employee(emp: EmployeesQ, session: Session = Depends(get_session)):
    statment = select(Employees).where(Employees.id == emp.id)
    result = session.exec(statment)
    
    if result:
        raise HTTPException(status_code=406, detail="This user already exists")
    
    new_emp = Employees(id=emp.id, name=emp.name, jopTitle=emp.jopTitle, salary=emp.salary, projects=emp.projects, checkIn=emp.checkIn, checkOut=emp.checkOut, StartOverTime=emp.StartOverTime, FinishOverTime=emp.FinishOverTime, Attendence=emp.Attendence, numberOfOverTime=emp.numberOfOverTime)
    session.add(new_emp)
    session.commit()
    
    return {"message": "New emplyeee created"}