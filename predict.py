import joblib

model = joblib.load(
    "models/crime_model.pkl"
)

sample = [[
    25,   # Victim Age
    5,    # Month
    22    # Hour (10 PM)
]]

prediction = model.predict(sample)

print(
    "Predicted Crime:",
    prediction
)