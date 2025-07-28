# Orchestrator
import asyncio
from market_overview_agent import run_market_overview
from news_summarizer_agent import run_news_summarizer
from sentiment_summarizer_agent import run_sentiment_summarizer
from technical_indicator_summarizer_agent import run_technical_indicator_summarizer
from timegpt_analyst_agent import run_timegpt_analyst
from fundamental_analysis_agent import run_fundamental_analysis
from day_trader_advisor_agent import run_day_trader_advisor

async def main(symbol, company_name):
    # Phase 1
    await run_market_overview()

    # Phase 2
    await asyncio.gather(
        run_news_summarizer(symbol, company_name, "2025-07-27", "2025-07-28", "2025-07-28T"),
        run_sentiment_summarizer(symbol),
        run_technical_indicator_summarizer(symbol),
        run_timegpt_analyst(symbol, company_name),
        run_fundamental_analysis(symbol)
    )

    # Phase 3
    result = await run_day_trader_advisor(symbol, company_name)
    print(result)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <SYMBOL> <COMPANY_NAME>")
        sys.exit(1)
    sym, name = sys.argv[1], sys.argv[2]
    asyncio.run(main(sym, name))