from datetime import datetime
import uuid
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging

from models import ChatRequest
from models.apiv2_types import ChatRequestV2, ConversationFeedback, FeedbackRequest, FeedbackResponse
from models import ChatResponse
from chat import Conversation
from chat.conversation_v2 import Conversation_V2
from models.apiv2_types import ChatResponseV2
from utils.config import Config, DeploymentCloud, DeploymentEnv
from uuid import uuid4

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

logger = logging.getLogger()

@app.post("/qa")
def qa(request: str) -> str:
    logger.info(f'[/qa] - question: {request}')    
    response = f'You posted: {request}';
    return response

