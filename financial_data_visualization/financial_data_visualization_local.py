import json

from request_handler import RequestHandler
from data_parser import DataParser
from data_visualizer import DataVisualizer

if __name__ == "__main__":

    companies = ("AMZN", "GOOG", "MSFT", "AAPL")
    companies_data = []

    for company in companies:
        with open("financial_data_visualization/" + company + ".json", "r") as my_file:
            data = my_file.read()
        response = json.loads(data)

        dp = DataParser(response)
        df = dp.get_daily_series()
        companies_data.append(df)

    dv = DataVisualizer(companies_data)
    dv.plot_data()
