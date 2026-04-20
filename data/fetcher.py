import yfinance as yf
import pandas as pd

TICKERS = [
    "SPY", "QQQ", "EFA",
    "TLT", "IEF", "SHY",
    "GLD", "USO",
    "EURUSD=X", "JPYUSD=X"
]

def fetch_prices(start: str, end: str) -> pd.DataFrame:
    raw = yf.download(TICKERS, start=start, end=end, auto_adjust=True)
    return raw["Close"]