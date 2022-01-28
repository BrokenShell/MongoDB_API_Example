from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data import MongoDB

API = FastAPI(
    title="MongoDB API",
    version="0.0.2",
    docs_url="/",
    description="Example MongoDB API",
)

API.db = MongoDB("TestDatabase", "TestCollection")

API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/version")
async def version():
    return {"result": API.version}


@API.post("/create")
async def create(data: dict):
    """ Creates a new record """
    return {"result": API.db.create(data)}


@API.post("/read")
async def read(data: dict):
    """ Returns records based on query """
    return {"result": API.db.read(data)}


@API.post("/update")
async def update(query: dict, update_data: dict):
    """ Returns the count of the updated records """
    return {"result": API.db.update(query, update_data)}


@API.post("/search")
async def search(user_search: str):
    """ Returns all records that match the user_search """
    return {"result": API.db.search(user_search)}
