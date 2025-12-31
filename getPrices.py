import pandas as pd
import yfinance as yf
from pathlib import Path

tickers = ["SPY", "QQQ", "MSFT", "AAPL"]
START_DATE = "2020-01-01"
END_DATE = "2025-12-30"

data = yf.download(tickers, start=START_DATE, end=END_DATE, interval="1d", auto_adjust=False, group_by="column")
adj_close = data["Adj Close"].copy()
adj_close.head().round(2)

BASE_DIR = Path(__file__).resolve().parent
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)
prices_path = OUTPUTS_DIR / "prices.csv"
adj_close.to_csv(prices_path)
print("Saved to: ", prices_path)