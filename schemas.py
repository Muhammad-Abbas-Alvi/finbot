from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

class StockRequest(BaseModel):
    symbol: str

class StockResponse(BaseModel):
    symbol: str
    current_price: float | None = None
    market_cap: float | None = None
    pe_ratio: float | None = None
