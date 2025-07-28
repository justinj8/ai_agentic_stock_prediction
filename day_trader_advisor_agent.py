# day_trader_advisor_agent.py
from crewai import DayTraderAdvisorCrew
from file_utils import read_summary_file

async def run_day_trader_advisor(symbol, company_name):
    # Load individual summaries
    news_summary       = read_summary_file(symbol, "news_summary_report.md")
    sentiment_summary  = read_summary_file(symbol, "sentiment_summary_report.md")
    technical_summary  = read_summary_file(symbol, "technical_indicator_summary_report.md")
    timegpt_summary    = read_summary_file(symbol, "timegpt_summary_report.md")
    fundamental_summary= read_summary_file(symbol, "fundamental_analysis_summary_report.md")

    # Load market-level (SPY) summaries
    market_news_summary      = read_summary_file("SPY", "news_summary_report.md")
    market_sentiment_summary = read_summary_file("SPY", "sentiment_summary_report.md")
    market_technical_summary = read_summary_file("SPY", "technical_indicator_summary_report.md")
    market_timegpt_summary   = read_summary_file("SPY", "timegpt_summary_report.md")
    market_fundamental_summary = read_summary_file("SPY", "fundamental_analysis_summary_report.md")

    # Synthesize into advisor inputs
    inputs = {
        "company_name":           company_name,
        "news_summary":           news_summary,
        "sentiment_summary":      sentiment_summary,
        "technical_summary":      technical_summary,
        "timegpt_summary":        timegpt_summary,
        "fundamental_summary":    fundamental_summary,
        "market_news_summary":    market_news_summary,
        "market_sentiment_summary": market_sentiment_summary,
        "market_technical_summary": market_technical_summary,
        "market_timegpt_summary":   market_timegpt_summary,
        "market_fundamental_summary": market_fundamental_summary
    }

    # Run the final advisor agent
    result = await DayTraderAdvisorCrew(symbol).crew().kickoff_async(inputs=inputs)
    return result