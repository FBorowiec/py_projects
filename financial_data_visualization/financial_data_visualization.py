import json
import requests
import pandas as pd


class RequestHandler:
    def __init__(self):
        self.url = "https://alpha-vantage.p.rapidapi.com/query"
        self.headers = {
            "x-rapidapi-key": "",
            "x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
        }

    def get_query(self, company):
        return {
            "function": "TIME_SERIES_DAILY",
            "symbol": company,
            "outputsize": "compact",
            "datatype": "json",
        }

    def get_response(self, query):
        response = requests.get(self.url, headers=self.headers, params=query)
        response.raise_for_status()

        return json.loads(response.text)


class DataParser:
    def __init__(self, data):
        self.data = data
        self.days_list = []
        self.headers = ["Open", "High", "Low", "Close", "Volume"]

    def get_daily_series(self):
        for day, values in self.data["Time Series (Daily)"].items():
            day_data = []
            for key, val in values.items():
                if key == "1. open":
                    sopen = val
                if key == "2. high":
                    high = val
                if key == "3. low":
                    low = val
                if key == "4. close":
                    close = val
                if key == "5. volume":
                    volume = val

            day_data = [sopen, high, low, close, volume]

            self.days_list.append(day_data)

        return pd.DataFrame(self.days_list, columns=self.headers)


if __name__ == "__main__":

    if False:
        rh = RequestHandler()
        companies = ("AMZN", "GOOG", "MSFT", "APPL")
        company_query = rh.get_query(companies[0])
        response = rh.get_response(company_query)
    else:
        with open("financial_data_visualization/AMZN.json", "r") as my_file:
            data = my_file.read()
        response = json.loads(data)

    dp = DataParser(response)
    df = dp.get_daily_series()
    print(df)
