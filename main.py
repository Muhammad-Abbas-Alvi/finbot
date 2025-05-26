from fastapi import FastAPI, Depends
from app.chat import process_chat
from app.finance_api import get_stock_info
from app.auth import authenticate_user
from app.schemas import ChatRequest, ChatResponse, StockRequest, StockResponse

app = FastAPI(title="FinBot")

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, token: str = Depends(authenticate_user)):
    return process_chat(request)

@app.post("/stock-info", response_model=StockResponse)
def stock_endpoint(request: StockRequest, token: str = Depends(authenticate_user)):
    return get_stock_info(request)
