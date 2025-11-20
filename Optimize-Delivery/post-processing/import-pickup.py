import pandas as pd
import os
from pathlib import Path

# Define the pickup folder path
pickup_folder = Path(__file__).parent.parent.parent / "Datapack" / "PickUp"

# Read all CSV files from the pickup folder
pickup_dataframes = {}

for csv_file in pickup_folder.glob("*.csv"):
    file_name = csv_file.stem  # Get filename without extension
    print(f"Reading {csv_file.name}...")
    pickup_dataframes[file_name] = pd.read_csv(str(csv_file))
    print(f"  Shape: {pickup_dataframes[file_name].shape}")
    print(f"  Columns: {list(pickup_dataframes[file_name].columns)}\n")

# Display summary of loaded dataframes
print("=" * 50)
print("Loaded PickUp Files Summary:")
print("=" * 50)
for name, df in pickup_dataframes.items():
    print(f"\n{name}:")
    print(f"  Records: {len(df)}")
    print(f"  Columns: {list(df.columns)}")

# Example: Access a specific dataframe
# df_cq = pickup_dataframes['pickup_cq']
# print(df_cq.head())
