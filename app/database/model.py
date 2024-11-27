from sqlmodel import SQLModel, Field

class Hr(SQLModel, table=True):
    __tablename__ = "hr"
    id: str = Field(primary_key=True)
    name: str
    salary: str
    jobTitle: str