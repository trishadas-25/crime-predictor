from geopy.geocoders import Nominatim
import pandas as pd
import time

crime = pd.read_csv("data/cleaned.csv")

geolocator = Nominatim(user_agent="crime_app")

unique_cities = crime["City"].dropna().unique()

city_map = {}

for city in unique_cities:

    try:
        location = geolocator.geocode(
            city + ", India"
        )

        if location:
            city_map[city] = [
                location.latitude,
                location.longitude
            ]

    except:
        pass

    time.sleep(1)

crime["Latitude"] = crime["City"].map(
    lambda x: city_map.get(x,[None,None])[0]
)

crime["Longitude"] = crime["City"].map(
    lambda x: city_map.get(x,[None,None])[1]
)

crime.to_csv(
    "data/final.csv",
    index=False
)

print("coordinates added")