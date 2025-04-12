import mlflow
from mlflow.tracking import MlflowClient
import os

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

def promote_model_to_production():
    """Promote the model from Staging to Production"""
    client = MlflowClient()
    
    stagging_versions = client.get_latest_versions(model_name, stages=["Staging"])
    if not stagging_versions:
        print("No model version found in Staging step")
        return
    
    latest_staging_version = stagging_versions[0]
    staging_version_number = latest_staging_version.version
    
    production_versions = client.get_latest_versions(model_name, stages=["Production"])
    
    if production_versions:
        current_production_version = production_versions[0]
        production_version_number = current_production_version.version
        
        client.transition_model_version_stage(
            name=model_name,
            version=production_version_number,
            stage="Archived",
            archive_existing_versions=True
        )
        print(f"Archived current production version: {production_version_number}")
    
    else:
        print("No model currently in Production stage")
        
    client.transition_model_version_stage(
        name=model_name,
        version=staging_version_number,
        stage="Production",
        archive_existing_versions=False,
    )
    print(f"Promoted model version {staging_version_number} to Production stage")
    print(f"Model version {staging_version_number} is now in Production stage")

if __name__ == "__main__":
    promote_model_to_production()
            
    
    