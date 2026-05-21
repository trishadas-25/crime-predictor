import streamlit as st
import joblib
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.set_page_config(
    page_title="AI Crime Predictor",
    layout="wide"
)

model = joblib.load(
    "models/crime_model.pkl"
)

st.title("🚨 AI Crime Prediction + Safety Insights")

st.write(
    "Predict crime patterns and visualize hotspots across India"
)

# inputs

age = st.slider(
    "Victim Age",
    1,
    80,
    25
)

month = st.selectbox(
    "Select Month",
    list(range(1,13))
)

hour = st.slider(
    "Select Hour",
    0,
    23,
    22
)

sample = pd.DataFrame(
    [[age,month,hour]],
    columns=[
        "Victim Age",
        "month",
        "hour"
    ]
)

# prediction

if st.button("Predict Crime"):

    prediction = model.predict(sample)[0]

    risk=min(
        (hour*3)+(age//2),
        100
    )

    if risk>80:

        advice="""
🚨 HIGH RISK

Avoid isolated routes
Prefer crowded places
Share live location
"""

    elif risk>50:

        advice="""
⚠ MEDIUM RISK

Stay alert
Avoid dark areas
"""

    else:

        advice="""
✅ LOW RISK

Area appears relatively safer
"""

    st.success(
        f"Predicted Crime Code: {prediction}"
    )

    st.info(
        f"Risk Score: {risk}/100"
    )

    st.warning(
        advice
    )

#heatmap

st.divider()

st.subheader(
    "🗺 India Crime Heatmap"
)

crime=pd.read_csv(
    "data/final.csv"
)

crime=crime.dropna()

crime_types=sorted(
    crime["Crime Domain"]
    .dropna()
    .unique()
)

selected_crime=st.selectbox(
    "Filter Crime Domain",
    crime_types
)

filtered=crime[
    (crime["month"]==month)
    &
    (crime["Crime Domain"]==selected_crime)
]

st.write(
    "Records found:",
    len(filtered)
)

if len(filtered)>0:

    m=folium.Map(
        location=[22.5,79],
        zoom_start=5,
        min_zoom=5,
        max_bounds=True
    )

    india_bounds=[
        [6,68],
        [37,98]
    ]

    m.fit_bounds(
        india_bounds
    )

    HeatMap(
        filtered[
            ["Latitude","Longitude"]
        ].values.tolist(),
        radius=20,
        blur=15
    ).add_to(m)

    st_folium(
        m,
        width=1000,
        height=600
    )

else:

    st.error(
        "No records found"
    )