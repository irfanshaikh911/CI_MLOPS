import unittest
import mlflow
from mlflow.tracking import MlflowClient
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os
import pandas as pd

dagshub_token = os.getenv("DAGSHUB_TOKEN")
if not dagshub_token:
    raise EnvironmentError("DAGSHUB_TOKEN environment variable not set.")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

dagshub_url = "https://dagshub.com"
repo_owner = "irfanshaikh911"
repo_name = "CI_MLOPS"
mlflow.set_tracking_uri(f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow")

model_name = 'Best Model'

class TestModel(unittest.TestCase):
    """unit test class to verify mlflow model loading from staging step"""
    
    def test_model_in_staging(self):
        """Test if the model is in staging"""
        client = MlflowClient()
        versions = client.get_latest_versions(model_name, stages=["Staging"])
        
        # Check if the model version is in staging
        self.assertGreater(len(versions), 0, "No model version found in Staging")
        
        # Check if the model version is not archived
    def test_model_loading(self):
        """Test if the model loads correctly"""
        client = MlflowClient()
        versions = client.get_latest_versions(model_name, stages=["Staging"])
        
        if not versions:
            self.fail("No model version found in Staging step, skipping model loading test")
        
        latest_version = versions[0].version
        run_id = versions[0].run_id
        
        logged_model = f"runs:/{run_id}/{model_name}"
        
        try:
            loaded_model = mlflow.pyfunc.load_model(logged_model)
        
        except Exception as e:
            self.fail(f"Failed to load model: {e}")
        
        self.assertIsNotNone(loaded_model, "Loaded model is None")
        print(f"Model loaded successfully from run ID: {run_id}, version: {latest_version}, logged model: {logged_model}")

if __name__ == "__main__":
    unittest.main()