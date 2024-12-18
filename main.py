from typing import List
from sqlmodel import create_engine, Session, SQLModel, select, delete
from fastapi import FastAPI, Depends, HTTPException
from app.database.model import Employees, Events, Hr, Meetings , Tasks, User_Request
from app.models.hr import EmployeesQ, EmployeesUQ, EventsQ, HrQ, HrUQ, MeetingsQ , TasksQ, User_RequestQ
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
    result = session.exec(statment).first()

    if result:
        return {"message": "This hr already exist"}
    
    new_hr = Hr(id=hr.id, name=hr.name, salary=hr.salary, jobTitle=hr.jobTitle, check_in=hr.check_in, check_out=hr.check_out, start_over_time=hr.check_out, finish_over_time=hr.finish_over_time, attendens=hr.attendens, number_of_over_time=hr.number_of_over_time)
    session.add(new_hr)
    session.commit()
    return {"message": "New Hr created"}

# @app.put("/api/hr/{id}", tags=["Hr"])
# def update_hr_by_id(id: str, hr: HrUQ, session: Session = Depends(get_session)):
#     statment = select(Hr).where(Hr.id == id)
#     result = session.exec(statment).first()
    
#     if not result:
#         return {"message": "This hr not found"}
    
#     if result.name:
#         result.name = hr.name
#     if result.jobTitle:
#         result.jobTitle = hr.jobTitle   
#     if result.salary != 0:
#         result.salary = hr.salary
#     if result.check_in != 0:
#         result.check_in = hr.check_in
#     if result.check_out != 0:
#         result.check_out = hr.check_out
#     if result.start_over_time != 0:
#         result.start_over_time = hr.start_over_time
#     if result.finish_over_time != 0:
#         result.finish_over_time = hr.finish_over_time
#     if result.attendens != 0:
#         result.attendens = hr.attendens
#     if result.number_of_over_time != 0:
#         result.number_of_over_time = hr.number_of_over_time
    
#     session.add(result)
#     session.commit()
#     session.refresh(result)
    
#     return {"message": "Hr updated succeffuly"}

@app.put("/api/hr/{id}", tags=["Hr"])
def update_hr_by_id(id: str, hr: HrUQ, session: Session = Depends(get_session)):
    statement = select(Hr).where(Hr.id == id)
    result = session.exec(statement).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="HR not found")
    
    for field, value in hr.dict(exclude_unset=True).items():
        setattr(result, field, value)
    
    session.add(result)
    session.commit()
    session.refresh(result)
    
    return {"message": "HR updated successfully"}

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
    result = session.exec(statment).first()

    if not result:
        return {"message": "This hr not found"}
    
    session.delete(result)
    session.commit()

    return {"message": "Hr deleted succeffuly"}



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

    new_task = Tasks(id=task.id, task_name=task.task_name, deadline=task.deadline)
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

    new_meeting = Meetings(id=meeting.id, name=meeting.name, during_time=meeting.during_time)
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

    new_event = Events(id=event.id, name=event.name, during_time=event.during_time)
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
    
    if not result:
        # raise HTTPException(status_code=406, detail=result)
          return  result
    new_emp = Employees(id=emp.id, name=emp.name, jopTitle=emp.jopTitle, salary=emp.salary, projects=emp.projects, checkIn=emp.checkIn, checkOut=emp.checkOut, StartOverTime=emp.StartOverTime, FinishOverTime=emp.FinishOverTime, Attendence=emp.Attendence, numberOfOverTime=emp.numberOfOverTime)
    session.add(new_emp)
    session.commit()
    
    return {"message": "New emplyeee created"}

@app.put("/api/employees/{id}", response_model=EmployeesUQ, tags=["Employees"])
def update_exist_user(id: str, emp: EmployeesUQ, session: Session = Depends(get_session)):
    statement = select(Employees).where(Employees.id == id)
    result = session.exec(statement).first()

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    if emp.projects:
        result.projects = emp.projects
    if emp.checkIn != 0:
        result.checkIn = emp.checkIn
    if emp.checkOut != 0:
        result.checkOut = emp.checkOut
    if emp.StartOverTime != 0:
        result.StartOverTime = emp.StartOverTime
    if emp.FinishOverTime != 0:
        result.FinishOverTime = emp.FinishOverTime
    if emp.Attendence != 0:
        result.Attendence = emp.Attendence
    if emp.numberOfOverTime != 0:
        result.numberOfOverTime = emp.numberOfOverTime

    session.add(result)
    session.commit()
    session.refresh(result)

    return result

@app.delete("/api/employees/{id}", tags=["Employees"])
def delete_exist_emp(id: str, session: Session = Depends(get_session)):
    statment = select(Employees).where(Employees.id == id)
    result = session.exec(statment).first()
    
    if not result:
        return {"message": "not found"}
    
    session.delete(result)
    session.commit()
    
    return {"message": "deleted"}

@app.get("/api/user_request", tags=["User_Request"])
def get_all_requests(session: Session = Depends(get_session)):
    
    statement = (
        select(
            User_Request.id,
            User_Request.requestType,
            User_Request.createdAt,
            User_Request.status,
            Employees.name,
            Employees.jopTitle
        )
        .join(Employees, Employees.id == User_Request.employee_id)
    )
    result = session.exec(statement).all()

    return [
        {
            "request_id": row[0],
            "requestType": row[1],
            "createdAt": row[2],
            "status": row[3],
            "employeeName": row[4],
            "jobTitle": row[5],
        }
        for row in result
    ]




@app.post("/api/user_request", tags=["User_Request"])
def create_new_request(user_request: User_RequestQ, session: Session = Depends(get_session)):
    data = session.get(Employees, user_request.employee_id)
    new_request = User_Request(employee_id=user_request.employee_id, requestType=user_request.requestType, createdAt=user_request.createdAt, status=user_request.status, employee=data)
    session.add(new_request)
    session.commit()
    session.refresh(new_request)
    
    return {"message": "New request created for user with this data", "user": new_request.employee}

@app.get("/api/user_request/{id}", tags=["User_Request"])
def get_request_by_emp_id(id: str, session: Session = Depends(get_session)):
    statment = select(User_Request).where(User_Request.employee_id == id)
    result = session.exec(statment).all()
    
    return result