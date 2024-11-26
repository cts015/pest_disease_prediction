import streamlit as st
import pandas as pd
import pickle
import math

# Load the pre-trained model
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Predicting Codling Moth Population")

# Sidebar inputs for user preferences
st.sidebar.header("Vegetation and Meteorlogical Data")

lag0_NDVI = st.sidebar.number_input("This month's average NDVI")
lag1_NDVI = st.sidebar.number_input("Last month's average NDVI")
lag0_min_temp = st.sidebar.number_input("This month's average minimum temperature (F)")
lag1_min_temp = st.sidebar.number_input("Last month's average minimum temperature (F)")
lag0_max_temp = st.sidebar.number_input("This month's average maximum temperature (F)")
lag1_max_temp = st.sidebar.number_input("Last month's average maximum temperature (F)")
lag0_precipitation = st.sidebar.number_input("This month's average precipitation (in)")
lag1_precipitation = st.sidebar.number_input("Last month's average precipitation (in)")

# Encoding the inputs
input_data = pd.DataFrame({
    'lag0_monthly_mean_NDVI': [lag0_NDVI],
    'lag1_monthly_mean_NDVI': [lag1_NDVI],
    'lag0_mean_min_temp (F)': [lag0_min_temp],
    'lag1_mean_min_temp (F)': [lag1_min_temp],
    'lag0_monthly_mean_max_temp (F)': [lag0_max_temp],
    'lag1_monthly_mean_max_temp (F)': [lag1_max_temp],
    'lag0_monthly_mean_precipitation (in)': [lag0_precipitation],
    'lag1_monthly_mean_precipitation (in)': [lag1_precipitation]
})

# Align columns with the training data (required columns)
required_columns = model.feature_names_in_  # Get the feature columns from the model
for col in required_columns:
    if col not in input_data.columns:
        input_data[col] = 0
input_encoded = input_data[required_columns]

# Make the prediction
prediction = model.predict(input_encoded)[0]

#Transform the output
number_moths = math.exp(prediction)

# Display the prediction
st.subheader(f"Monthly average number of moths per trap per week: {number_moths}")
