STOCK_MARKET_OVERVIEW_SYMBOL = "SPY"
YESTERDAY_HOUR = "18:00"
AGENT_INPUTS_FOLDER = "./inputs"
RELEVANT_ARTICLES_FILE = "relevant_urls.txt"
SOCIAL_FETCH_LIMIT = 500

TECHNICAL_INDICATOR_DEFAULTS = {
    "SMA": [5, 20],
    "EMA": [12, 26],
    "RSI": 14,
    "MACD": {"fast": 12, "slow": 26, "signal": 9},
    "CCI": 20,
    "Bollinger": {"window": 20, "std": 2},
    "ATR": 14,
    "MFI": 14,
    "OBV": None
}