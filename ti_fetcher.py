# ti_fetcher.py
def get_ti_context(symbol, indicator_params):
    print(f"[Stub] get_ti_context({symbol!r}, {indicator_params!r}) called")
    # Return dummy indicator series
    return {
        "SMA_5": [100, 101, 102],
        "SMA_20": [98, 99, 100],
        "RSI_14": [30, 35, 40],
        "MACD": [1.2, 1.3, 1.4]
    }