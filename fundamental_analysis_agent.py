# Generated pseudocode from Medium article
from fundamental_fetcher import get_fundamental_context
from crewai import Task
import tasks_config

async def run_fundamental_analysis(symbol):
    # Step 1: Collect fundamentals from FinViz, TipRanks, ValueInvesting.io
    fundamental_data = get_fundamental_context(symbol=symbol)

    # Step 2: Configure the expert analysis task
    fundamental_task = Task(
    config=tasks_config.fundamental_analysis_task,
    output_file='fundamental_analysis_summary_report.md'
    )
    # Agent consumes `fundamental_data` & produces a markdown report.
