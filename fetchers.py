# fetchers.py
class HistoricalMarketFetcher:
    def get_vix(self, days):
        print(f"[Stub] get_vix({days}) called")
        return {"VIX": [20.1] * days}

    def get_global_market(self, days):
        print(f"[Stub] get_global_market({days}) called")
        return {"FTSE": [7500.0] * days}