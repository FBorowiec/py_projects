import requests
import json


class RequestHandler:
    def __init__(self):
        self.sources = ["countries", "provinces", "cities"]
        self.countries_json = self.request_json_data(self.sources[0])
        self.province_json = self.request_json_data(self.sources[1])
        self.cities_json = self.request_json_data(self.sources[2])

    def request_json_data(self, source):
        r = requests.get(
            "https://www.trackcorona.live/api/" + source,
            headers={
                "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
            },
        )
        c = r.content
        return json.loads(c)
