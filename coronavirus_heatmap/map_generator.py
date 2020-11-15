import folium
from os import path


class MapCreator:
    def create_feature_group(self, coronavirus_data, name, color):
        fg = folium.FeatureGroup(name=name)
        for province in coronavirus_data["data"]:
            popup = (
                province["location"]
                + ", "
                + province["country_code"].upper()
                + "\n"
                + "Confirmed cases: "
                + str(province["confirmed"])
                + "\n"
                + "Recovered: "
                + str(province["recovered"])
                + "\n"
                + "Dead: "
                + str(province["dead"])
            )
            fg.add_child(
                folium.Marker(
                    location=[
                        float(province["latitude"]),
                        float(province["longitude"]),
                    ],
                    popup=popup,
                    icon=folium.Icon(color=color),
                )
            )

        return fg

    def generate_map(self, output_path, *args):
        map = folium.Map(
            location=[45.464152, 9.191731], zoom_start=6, tiles="Stamen Terrain"
        )

        for arg in args:
            map.add_child(arg)

        map.save(path.join(path.expanduser(output_path), "heatmap.html"))
