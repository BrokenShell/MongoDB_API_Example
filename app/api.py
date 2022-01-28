from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data import MongoDB

API = FastAPI(
    title="MongoDB API",
    version="0.0.1",
    docs_url="/",
    description="Example MongoDB API",
)

API.db = MongoDB("TestCluster", "TestTable")

API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/version")
async def version():
    return {"version": API.version}


@API.post("/create")
async def create(data: dict):
    """ Creates a new record """
    API.db.create(data)
    return {"created": data}
