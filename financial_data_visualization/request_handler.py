import requests
import json

from os import getcwd, path


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
