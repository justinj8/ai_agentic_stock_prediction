# Agentic AI Stock Research/Prediction System

## Overview
An asynchronous, agent‑based pipeline that gathers market data, financial news, social sentiment, technical indicators, and fundamental metrics to produce a consolidated day‑trading recommendation.

## Features
- **Market overview** – pulls volatility (VIX) and global market data for the benchmark symbol `SPY`.
- **News summarization** – collects recent headlines, filters articles and extracts full text for analysis.
- **Social sentiment** – fetches StockTwits posts to gauge trader sentiment.
- **Technical indicators** – computes moving averages, RSI, MACD and other indicators from historical prices.
- **Time‑series forecasting** – retrieves TimeGPT forecasts for tracked tickers.
- **Fundamental analysis** – summarizes valuation metrics such as P/E, P/B and dividend yield.
- **Day trader advisor** – synthesizes all summaries into a final recommendation.

## Repository Structure
<pre>
agentic_ai_system/
├── crewai.py
├── fetchers.py
├── news_fetcher.py
├── sentiment_fetcher.py
├── ti_fetcher.py
├── timegpt_client.py
├── fundamental_fetcher.py
├── file_utils.py
├── tasks_config.py
├── settings.py
├── market_overview_agent.py
├── news_summarizer_agent.py
├── sentiment_summarizer_agent.py
├── technical_indicator_summarizer_agent.py
├── timegpt_analyst_agent.py
├── fundamental_analysis_agent.py
├── day_trader_advisor_agent.py
└── main.py
</pre>

## Getting Started
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv && source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run a quick smoke test:
   ```bash
   python - <<'PYCODE'
   import asyncio
   from market_overview_agent import run_market_overview
   asyncio.run(run_market_overview())
   PYCODE
   ```
4. Execute the full pipeline for a specific stock:
   ```bash
   python main.py AAPL "Apple Inc"
   ```
   Replace the ticker and company name with any symbol you wish to analyze.

## Project Status
The modules currently contain stub implementations to illustrate an agentic workflow. They print placeholder data rather than calling real APIs. Extending the fetchers and agents with live data sources, richer error handling, persistent outputs, and tests will make the system production ready.

## Contributing
Contributions are welcome. Please include docstrings and tests with any new feature or fix.
