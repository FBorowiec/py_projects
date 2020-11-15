from request_handler import RequestHandler
from parser import Parser
from map_generator import MapCreator

if __name__ == "__main__":
    parser = Parser()

    rh = RequestHandler()
    coronavirus_countries_data = rh.countries_json
    coronavirus_province_data = rh.province_json
    coronavirus_cities_data = rh.cities_json

    mc = MapCreator()
    fg1 = mc.create_feature_group(
        coronavirus_countries_data, name="Coronavirus countries data", color="red"
    )
    fg2 = mc.create_feature_group(
        coronavirus_province_data, name="Coronavirus province data", color="blue"
    )
    fg3 = mc.create_feature_group(
        coronavirus_cities_data, name="Coronavirus cities data", color="orange"
    )

    mc.generate_map(parser.output_path, fg1, fg2, fg3)
