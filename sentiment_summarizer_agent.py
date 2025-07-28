# sentiment_summarizer_agent.py
from sentiment_fetcher import get_stocktwits_context
from utils import get_yesterday_18_est
import settings

async def run_sentiment_summarizer(symbol):
    # Step 1: Fetch Social Media Data (500 posts since 6 PM yesterday)
    posts = get_stocktwits_context(
        symbol=symbol,
        limit=settings.SOCIAL_FETCH_LIMIT,
        since=get_yesterday_18_est()
    )
    # Step 2: (Agent would process `posts`)
    return posts