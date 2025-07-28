# technical_indicator_summarizer_agent.py
from ti_fetcher import get_ti_context
import settings

async def run_technical_indicator_summarizer(symbol):
    # Step 1: Fetch Historical Data + Compute Indicators
    ti_data = get_ti_context(
        symbol=symbol,
        indicator_params=settings.TECHNICAL_INDICATOR_DEFAULTS
    )
    # Step 2: Return for downstream summarization
    return ti_data