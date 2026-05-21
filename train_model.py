import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

crime = pd.read_csv("data/cleaned.csv")

# Features
X = crime[[
    "Victim Age",
    "month",
    "hour"
]]

# Target
y = crime["Crime Description"]

# Split
xtrain, xtest, ytrain, ytest = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier()

model.fit(xtrain, ytrain)

joblib.dump(
    model,
    "models/crime_model.pkl"
)

print("model saved")