from sqlmodel import create_engine, Session, SQLModel, select
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