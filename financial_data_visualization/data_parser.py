import pandas as pd

from datetime import datetime


class DataParser:
    def __init__(self, data):
        self.data = data
        self.days_list = []
        self.headers = ["Day", "Open", "High", "Low", "Close", "Volume"]

    def get_daily_series(self):
        for day, values in self.data["Time Series (Daily)"].items():
            day_data = []
            for key, val in values.items():
                if key == "1. open":
                    open_value = float(val)
                if key == "2. high":
                    high = float(val)
                if key == "3. low":
                    low = float(val)
                if key == "4. close":
                    close = float(val)
                if key == "5. volume":
                    volume = float(val)

            day_data = [
                datetime.strptime(day, "%Y-%m-%d"),
                open_value,
                high,
                low,
                close,
                volume,
            ]

            self.days_list.append(day_data)

        return pd.DataFrame(self.days_list, columns=self.headers)
