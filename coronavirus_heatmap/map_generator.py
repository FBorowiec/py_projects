import folium
import numpy as np
from os import path


class MapCreator:
    def circle_size(self, number_of_cases, factor=5):
        size = int(np.power(np.log(number_of_cases), 2) / factor)
        return size

    def create_feature_group(self, coronavirus_data, name, color):
        fg = folium.FeatureGroup(name=name)
        for province in coronavirus_data["data"]:
            popup = (
                province["location"]
                + ", "
                + province["country_code"].upper()
                + ",\n"
                + "Confirmed cases: "
                + str(province["confirmed"])
                + ",\n"
                + "Recovered: "
                + str(province["recovered"])
                + ",\n"
                + "Dead: "
                + str(province["dead"])
            )
            if province["confirmed"] > 0:
                fg.add_child(
                    folium.CircleMarker(
                        location=[
                            float(province["latitude"]),
                            float(province["longitude"]),
                        ],
                        radius=self.circle_size(province["confirmed"]),
                        popup=popup,
                        fill_color=color,
                        color="grey",
                        fill_opacity=0.7,
                    )
                )

        return fg

    def generate_map(self, output_path, *args):
        map = folium.Map(
            location=[45.464152, 9.191731], zoom_start=6, tiles="Stamen Terrain"
        )

        for arg in args:
            map.add_child(arg)

        map.add_child(folium.LayerControl())
        map.save(path.join(path.expanduser(output_path), "heatmap.html"))
