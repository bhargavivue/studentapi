from fastapi import FastAPI,  HTTPException
from app.api.Students import Students
app = FastAPI()
s1=Students()

@app.get("/allstudents")
def allstudents():
    list_students=s1.getAllStudents()
    return list_students