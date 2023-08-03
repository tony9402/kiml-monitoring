import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import dashboard, submit
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)
app.include_router(submit.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        app=app, host=os.environ["API_HOST"], port=int(os.environ["API_PORT"])
    )  # noqa: E501
