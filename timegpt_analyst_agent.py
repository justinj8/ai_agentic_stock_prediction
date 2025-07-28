# Generated pseudocode from Medium article
from timegpt_client import get_timegpt_forecast, format_timegpt_forecast

async def run_timegpt_analyst(symbol, company_name):
    # Step 1: Fetch TimeGPT forecasts for all tracked stocks
    timegpt_forecasts = get_timegpt_forecast()

    # Step 2: Extract & analyze the forecast for our symbol
    forecast = format_timegpt_forecast(timegpt_forecasts, symbol, company_name)
    return forecast
