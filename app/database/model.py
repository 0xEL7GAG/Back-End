from sqlmodel import SQLModel

class Hr(SQLModel, table=True):
    __tablename__ = "hr"
    id: str
    name: str
    salary: str
    jobTitle: str