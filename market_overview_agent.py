# Generated pseudocode from Medium article
from crewai import process_stock_symbol_async
from fetchers import HistoricalMarketFetcher
from analysts import MarketConditionsAnalyst
import settings

async def run_market_overview():
    # Step 1: Collect Market Data
    vix_data = HistoricalMarketFetcher().get_vix(days=30)
    global_market_data = HistoricalMarketFetcher().get_global_market(days=30)

    # Step 2: Run Full Analysis on Market Symbol (SPY)
    market_analyst = MarketConditionsAnalyst()
    market_agent, market_task = market_analyst.get_agent_and_task()

    await process_stock_symbol_async(
        settings.STOCK_MARKET_OVERVIEW_SYMBOL,
        vix_data=vix_data,
        global_market_data=global_market_data,
        additional_agents=[market_agent],
        additional_tasks=[market_task]
    )
