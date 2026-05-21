import pandas as pd
from sklearn.preprocessing import LabelEncoder

# load data
crime = pd.read_csv("data/crime.csv")

# remove missing values
crime = crime.dropna()

# convert date
crime["Date Reported"] = pd.to_datetime(
    crime["Date Reported"],
    dayfirst=True,
    errors="coerce"
)
# extract month/day
crime["month"] = crime["Date Reported"].dt.month
crime["day"] = crime["Date Reported"].dt.day

# hour from occurrence time
crime["Time of Occurrence"] = pd.to_datetime(
    crime["Time of Occurrence"],
    dayfirst=True,
    errors="coerce"
)

crime["hour"] = (
    crime["Time of Occurrence"].dt.hour
)

# encode target
encoder = LabelEncoder()

crime["Crime Description"] = encoder.fit_transform(
    crime["Crime Description"]
)

crime.to_csv(
    "data/cleaned.csv",
    index=False
)

print("cleaning done")