import json

from request_handler import RequestHandler
from data_parser import DataParser
from data_visualizer import DataVisualizer

if __name__ == "__main__":

    companies = ("AMZN", "GOOG", "MSFT", "AAPL")
    companies_data = []

    rh = RequestHandler()
    for company in companies:
        company_query = rh.get_query(company)
        response = rh.get_response(company_query)
        dp = DataParser(response)
        df = dp.get_daily_series()
        companies_data.append(df)

    dv = DataVisualizer(companies_data)
    dv.plot_data()
