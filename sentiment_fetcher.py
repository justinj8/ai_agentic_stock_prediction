# sentiment_fetcher.py
def get_stocktwits_context(symbol, limit, since):
    print(f"[Stub] get_stocktwits_context({symbol!r}, limit={limit}, since={since!r}) called")
    # Return dummy posts
    return [
        {"user":"alice", "text":"Bullish on this!"},
        {"user":"bob",   "text":"Bear in mind risks."}
    ]