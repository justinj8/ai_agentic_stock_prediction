# timegpt_client.py

def get_timegpt_forecast():
    print("[Stub] get_timegpt_forecast() called")
    # Return dummy forecast records for multiple symbols
    return [
        {"symbol": "AAPL", "pred": 145.67},
        {"symbol": "MSFT", "pred": 299.12}
    ]

def format_timegpt_forecast(forecasts, symbol, company_name):
    print(f"[Stub] format_timegpt_forecast for {symbol}")
    # Find matching symbol forecast
    for rec in forecasts:
        if rec["symbol"] == symbol:
            return {"symbol": symbol, "forecast": rec["pred"], "company": company_name}
    # Default fallback
    return {"symbol": symbol, "forecast": None, "company": company_name}