import streamlit as st
import pandas as pd
import mlflow
import os

# Set up MLflow tracking
dagshub_url = "https://dagshub.com"
repo_owner = "irfanshaikh911"
repo_name = "CI_MLOPS"
mlflow.set_tracking_uri(f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow")

def load_model():
    client = mlflow.tracking.MlflowClient()
    versions = client.get_latest_versions("Best Model", stages=["Production"])
    if not versions:
        st.error("No model found in the 'Production' stage.")
        return None
    run_id = versions[0].run_id
    return mlflow.pyfunc.load_model(f"runs:/{run_id}/Best Model")

# Load the model
model = load_model()

# Streamlit UI
st.title("Water Potability Prediction")
st.write("Enter the water quality parameters below to predict potability and add the data to the dataset.")

# Input fields
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
hardness = st.number_input("Hardness", min_value=0.0, value=100.0, step=0.1)
solids = st.number_input("Solids", min_value=0.0, value=20000.0, step=1.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0, step=0.1)
sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0, step=1.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0, step=1.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0, step=0.1)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=60.0, step=1.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0, step=0.1)

# Predict button
if st.button("Predict"):
    if model is None:
        st.error("Model is not loaded. Please check the MLflow configuration.")
    else:
        # Create a DataFrame for the input
        input_data = pd.DataFrame({
            "ph": [ph],
            "Hardness": [hardness],
            "Solids": [solids],
            "Chloramines": [chloramines],
            "Sulfate": [sulfate],
            "Conductivity": [conductivity],
            "Organic_carbon": [organic_carbon],
            "Trihalomethanes": [trihalomethanes],
            "Turbidity": [turbidity]
        })

        # Make prediction
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.success("The water is **potable** (safe to drink).")
        else:
            st.error("The water is **not potable** (not safe to drink).")

        # Append input data to the dataset
        dataset_path = "data/raw/train.csv"
        os.makedirs(os.path.dirname(dataset_path), exist_ok=True)
        if os.path.exists(dataset_path):
            existing_data = pd.read_csv(dataset_path)
            updated_data = pd.concat([existing_data, input_data], ignore_index=True)
        else:
            updated_data = input_data

        updated_data.to_csv(dataset_path, index=False)
        st.write("The input data has been added to the dataset for future training.")