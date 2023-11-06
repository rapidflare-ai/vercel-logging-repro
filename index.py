from datetime import datetime
import uuid
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    username: str


origins = [
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

rootLogger = logging.getLogger()

# 3. Create and configure a console handler for all environments
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set log level to INFO for this handler
console_formatter = logging.Formatter('%(levelname)-5.5s: %(asctime)s %(filename)s:%(lineno)d - %(message)s',
                                        datefmt='%Y-%m-%d,%H:%M:%S')
console_handler.setFormatter(console_formatter)
rootLogger.addHandler(console_handler)    
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)

@app.post("/qa")
def qa(request: ChatRequest) -> str:
    logger.info(f'[/qa] - question: {request.question} from {request.username}')
    response = f'{request.username} asked {request.question}'
    return response

