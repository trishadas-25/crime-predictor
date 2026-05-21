import pandas as pd
import folium
from folium.plugins import HeatMap

crime = pd.read_csv(
    "data/final.csv"
)

crime = crime.dropna()

m = folium.Map(
    location=[20.59,78.96],
    zoom_start=5
)

HeatMap(
    crime[
        ["Latitude","Longitude"]
    ].values.tolist()
).add_to(m)

m.save(
    "assets/heatmap.html"
)

print("heatmap created")