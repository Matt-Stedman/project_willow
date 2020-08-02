import yfinance as yf
from pathlib import Path
import toml

# Globals
history = "6mo"  # valid periods = 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
frequency = "5m"  # valid intervals =  1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

with open(Path("src/stock_choices.toml")) as stock_choices_file:
    stock_choices = toml.load(stock_choices_file)

selection_set = stock_choices["requests"]["lse"]["personal"]

for key_stock, name_stock in selection_set.items():

    stock = yf.Ticker(f"{key_stock}.L")
    historical = stock.history()
    toml.dump(
        o={"ticker": key_stock, "name": name_stock, "historical": historical},
        f=f"stocks/{key_stock}.toml",
    )

