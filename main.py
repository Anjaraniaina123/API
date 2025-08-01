from fastapi import FastAPI,HTTPException
from typing import List
from starlette.responses import Response, JSONResponse
from starlette.responses import Response, JSONResponse
from pydantic import BaseModel

app = FastAPI()

class EventModel(BaseModel):
    author : str
    title : str
    content : str
    création_datetime : int




# Q1 création de route GET/ping
@app.get("/ping")
async def root():
    return {"message": "pong en text brute"}


# Q2- création de route GET/home
@app.get("/home")
async def say_welcome():
    with open("welcome.html","r", encoding = "utf-8") as file: 
        html_content = file.read()

    return Response(content=html_content, status_code = 200, media_type= "text/html")


# Q3- configuration d'une application
@app.get("/{full_path:path}")
async def root(full_path: str):
    with open("not_found.html", "r", encoding= "utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code = 404, media_type="text:html")


# Q4 - création de POST/posts


events_store: List[EventModel] = []


def serialized_stored_events():
    events_converted = []
    for event in events_store:
        events_converted.append(event.model_dump())
    return events_converted

@app.post("/posts")
def new_events(event_payload: List[EventModel]):
    events_store.extend(event_payload)
    return {"posts": serialized_stored_events()}
