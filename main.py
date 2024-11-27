from sqlmodel import create_engine, Session, SQLModel, select, delete
from fastapi import FastAPI, Depends
from app.database.model import Hr
from app.models.hr import HrQ
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