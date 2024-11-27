from pydantic import BaseModel

class HrQ(BaseModel):
    id: str
    name: str
    salary: str
    jobTitle: str