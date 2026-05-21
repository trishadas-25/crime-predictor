# AI-Powered Crime Prediction and Geographic Heatmap System

## 1. Project Overview

### Project Title

AI-Powered Crime Prediction and Geographic Heatmap System

### Project Type

Intermediate Machine Learning + Data Science + Geographic Visualization Project

### Deployment Platform

Streamlit Community Cloud

### Live Application

[https://crime-predictor-trisha.streamlit.app/](https://crime-predictor-trisha.streamlit.app/)

### GitHub Repository

[https://github.com/trishadas-25/crime-predictor](https://github.com/trishadas-25/crime-predictor)



## 2. Introduction

Crime analysis and prediction has become an important application of Artificial Intelligence and Data Science. Large crime datasets contain patterns related to locations, time, demographics, and crime categories. By analyzing these patterns, predictive systems can assist authorities and users in understanding potential risk areas.

This project combines Machine Learning, data preprocessing, geospatial visualization, and web deployment to build an AI-powered system capable of:

* Predicting probable crime patterns
* Visualizing crime hotspots across India
* Providing AI-generated safety insights
* Displaying geographic crime concentration using heatmaps

The system was designed as an end-to-end deployable application rather than a standalone notebook model.



# 3. Objectives

The primary objectives of this project are:

1. Analyze Indian crime datasets.
2. Clean and preprocess real-world data.
3. Train a machine learning model.
4. Generate predictions from user inputs.
5. Visualize crime density geographically.
6. Provide AI-driven safety suggestions.
7. Deploy a fully interactive application.



# 4. Technology Stack

## Programming Language

Python

## Libraries Used

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Joblib

### Visualization

* Matplotlib
* Seaborn
* Folium
* Streamlit-Folium

### Geographical Processing

* Geopy

### Web Interface

* Streamlit

### Deployment

* GitHub
* Streamlit Community Cloud



# 5. Project Architecture

User Input
↓
Streamlit Interface
↓
Preprocessing
↓
Trained Random Forest Model
↓
Crime Prediction
↓
Risk Score Generation
↓
AI Safety Suggestions
↓
Dynamic Heatmap Visualization



# 6. Dataset Information

The project uses an Indian crime dataset containing records related to:

* Date Reported
* Victim Age
* Crime Category
* Crime Domain
* City
* Location Information

Additional city coordinates were generated using geocoding.

Coordinate conversion enabled creation of geographic heatmaps.



# 7. Data Preprocessing

Real-world datasets contain inconsistencies and missing values.

Preprocessing steps:

### Step 1

Missing values removed.

### Step 2

Date conversion.

### Step 3

Extracted:

* Month
* Hour

### Step 4

Encoded target labels.

### Step 5

Generated cleaned dataset.

Output:
cleaned.csv



# 8. Machine Learning Model

Algorithm Used:
RandomForestClassifier

Features:

* Victim Age
* Month
* Hour

Target:
Crime Code

Reason for selecting Random Forest:

* Handles nonlinear relationships
* Works well with structured data
* Resistant to overfitting
* Good prediction performance

Model optimization:

n_estimators = 20
max_depth = 5

Model saved using:

joblib

Output:
crime_model.pkl



# 9. Geographic Heatmap System

Heatmaps were generated using Folium.

Workflow:

City Name
↓
Geocoding
↓
Latitude + Longitude
↓
Heatmap

Color interpretation:

Red:
High concentration

Yellow:
Medium concentration

Blue:
Low concentration

Map configured specifically for India.



# 10. AI Safety Suggestions

Instead of displaying only predictions, AI-generated recommendations were added.

Examples:

High Risk:
Avoid isolated routes.
Prefer crowded areas.
Share live location.

Medium Risk:
Stay alert.
Avoid poorly lit places.

Low Risk:
Remain aware of surroundings.

This feature improves practical usability.



# 11. User Interface

Developed using Streamlit.

User Inputs:

* Victim Age Slider
* Month Selection
* Hour Selection
* Crime Domain Filter

Outputs:

* Predicted Crime
* Risk Score
* Safety Suggestions
* Dynamic Heatmap



# 12. Deployment Process

Deployment pipeline:

Local Development
↓
GitHub Repository
↓
Streamlit Cloud
↓
Public URL

Challenges solved:

* Large model file issue
* Git history cleanup
* deployment configuration issues
* dependency handling
* cloud compatibility



# 13. Results

Successfully implemented:

✓ Data preprocessing
✓ ML model training
✓ Crime prediction
✓ Heatmap visualization
✓ Safety insights
✓ Interactive interface
✓ Cloud deployment



# 14. Future Improvements

Potential future upgrades:

1. Crime trend forecasting
2. Exact location coordinates
3. Deep Learning models
4. Real-time API integration
5. NLP-based crime description analysis
6. Dashboard analytics
7. Time-series forecasting



# 15. Conclusion

This project demonstrates how Artificial Intelligence and Data Science can be integrated with geographic visualization and web technologies to create practical real-world systems.

The system successfully combines prediction, analytics, heatmaps, and AI safety recommendations into a deployable application.

The project also demonstrates the complete lifecycle of an AI product:

Data Collection → Cleaning → Model Training → Visualization → Deployment
