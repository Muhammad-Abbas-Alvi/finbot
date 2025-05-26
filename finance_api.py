import yfinance as yf
from app.schemas import StockRequest, StockResponse

def get_stock_info(request: StockRequest) -> StockResponse:
    ticker = yf.Ticker(request.symbol)
    info = ticker.info
    return StockResponse(
        symbol=request.symbol,
        current_price=info.get("currentPrice"),
        market_cap=info.get("marketCap"),
        pe_ratio=info.get("trailingPE")
    )
