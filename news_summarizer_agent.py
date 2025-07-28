# Generated pseudocode from Medium article
import os
from news_fetcher import get_news_context, get_stock_news
from crewai import AiArticlesPickerCrew
import settings

async def run_news_summarizer(symbol, company_name, yesterday_str, today_str, today_str_no_min):
    # Step 1: Fetch Headlines from multiple sites
    stock_headlines = get_news_context(
        symbol=symbol,
        start_time=f"{yesterday_str} {settings.YESTERDAY_HOUR}"
    )

    # Step 2: AI-Powered Article Selection (top 10 URLs)
    inputs = {
        'company_name': company_name,
        'stock_headlines': stock_headlines,
        'today_str': today_str
    }
    await AiArticlesPickerCrew(symbol).crew().kickoff_async(inputs=inputs)

    # Step 3: Extract Full Articles from filtered URLs
    stock_news = await get_stock_news(
        symbol,
        os.path.join(settings.AGENT_INPUTS_FOLDER, today_str_no_min,
                     f"{symbol}_{settings.RELEVANT_ARTICLES_FILE}")
    )

    # (The agent then ingests both headlines and full articles for summarization)
