import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

crime = pd.read_csv("data/cleaned.csv")

X = crime[
    [
        "Victim Age",
        "month",
        "hour"
    ]
]

y = crime["Crime Code"]


model = RandomForestClassifier(
    n_estimators=20,
    max_depth=5,
    random_state=42
)

model.fit(X, y)

# create models folder if missing
os.makedirs(
    "models",
    exist_ok=True
)

joblib.dump(
    model,
    "models/crime_model.pkl",
    compress=3
)

print("model saved")