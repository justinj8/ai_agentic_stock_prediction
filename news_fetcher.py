# news_fetcher.py
def get_news_context(symbol, start_time):
    print(f"[Stub] get_news_context({symbol!r}, {start_time!r}) called")
    # Return dummy headlines
    return [
        {"headline": f"{symbol} hits new high", "url": "https://example.com/1"},
        {"headline": f"{symbol} earnings call", "url": "https://example.com/2"},
    ]

async def get_stock_news(symbol, filepath):
    print(f"[Stub] get_stock_news({symbol!r}, {filepath!r}) called")
    # Return dummy full-article texts
    return ["Full article text 1", "Full article text 2"]