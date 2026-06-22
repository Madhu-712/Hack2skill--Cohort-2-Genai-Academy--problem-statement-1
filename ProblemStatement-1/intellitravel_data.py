from google.cloud import bigquery
import pandas as pd

# =====================================
# CONFIGURATION
# =====================================

PROJECT_ID = "notebooklm-491108"
DATASET_ID = "intellitravel_nexus"

CSV_FILES = {
    "tourist_profiles": "tourist_profiles.csv",
    "destinations": "destinations.csv",
    "tourist_visits": "tourist_visits.csv",
    "destination_capacity_and_infrastructure": "destination_capacity_and_infrastructure.csv"
}

# =====================================
# BIGQUERY CLIENT
# =====================================

client = bigquery.Client(project=PROJECT_ID)

# =====================================
# CREATE DATASET IF NOT EXISTS
# =====================================

dataset_ref = bigquery.Dataset(
    f"{PROJECT_ID}.{DATASET_ID}"
)

try:
    client.get_dataset(dataset_ref)
    print(f"Dataset exists: {DATASET_ID}")

except Exception:
    dataset = client.create_dataset(dataset_ref)
    print(f"Created dataset: {DATASET_ID}")

# =====================================
# UPLOAD CSV FILES
# =====================================

for table_name, csv_path in CSV_FILES.items():

    print(f"\nUploading {table_name}...")

    df = pd.read_csv(csv_path)

    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    table = client.get_table(table_id)

    print(
        f"Loaded {table.num_rows} rows "
        f"into {table_id}"
    )

print("\nAll tables uploaded successfully!")