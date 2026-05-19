from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Base, engine
from data_classes import Student
import backend
import uvicorn
from error_classes import ServerException

Base.metadata.create_all(bind=engine)
app = FastAPI()

events = {}
submissions = {}

host_name = "0.0.0.0"
server_port = 8000

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/api")
def read_root():
    return {"message" : "Hello, FastAPI!"}

@app.get("/api/user/{session}")
def get_user(session: str):
    try:
        return backend.studentGetDetails(session)
    except ServerException as error:
        raise HTTPException(status_code=error.error_code, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal server error") from error

@app.post("/api/user/register")
def register_user(student: Student):
    try:
        backend.studentRegister(student)
        return {"message": "User registered successfully"}
    except ServerException as error:
        raise HTTPException(status_code=error.error_code, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal server error") from error

@app.post("/api/user/login")
def login_user(username: str, password: str):
    try:
        session = backend.studentLogin(username, password)
        return {"message": "Login successful", "session": session}
    except ServerException as error:
        raise HTTPException(status_code=error.error_code, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal server error") from error

@app.put("/api/user/update")
def update_user(session: str, toChange: dict):
    try:
        backend.studentUpdateDetails(session, **toChange)
        return {"message": "User details updated successfully"}
    except ServerException as error:
        raise HTTPException(status_code=error.error_code, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal server error") from error

@app.post("/api/group/register")
def register_group(name: str, members: list, password: str):
    try:
        backend.groupRegister(name, members, password)
        return {"message": "Group registered successfully"}
    except ServerException as error:
        raise HTTPException(status_code=error.error_code, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal server error") from error

@app.post("/api/group/login")
def login_group(groupId: str, password: str):
    try:
        backend.groupLogin(groupId, password)
        return {"message": "Group login successful"}
    except ServerException as error:
        raise HTTPException(status_code=error.error_code, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal server error") from error

if __name__ == "__main__":
    uvicorn.run(app, host=host_name, port=server_port)
    

