# Agentic AI Stock Research/Prediction System

**What**  
An AI agent-based pipeline for market overview, news & social sentiment, technical & fundamental analysis, and a final “Trader” recommendation.

**Structure**  

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


**Getting Started**  

1. `python3 -m venv venv && source venv/bin/activate`  
2. `pip install -r requirements.txt`  
3. Run a smoke test:  
   ```bash
   python - <<'PYCODE'
   import asyncio
   from market_overview_agent import run_market_overview
   asyncio.run(run_market_overview())
   PYCODE

# Or run this for a simpler process:
python main.py AAPL "Apple Inc"  # Change to any ticker #
