
import pandas as pd
import os
from pathlib import Path

# Define the delivery folder path
delivery_folder = Path(__file__).parent.parent.parent / "Datapack" / "Delivery"

# Read all CSV files from the delivery folder
delivery_dataframes = {}

for csv_file in delivery_folder.glob("*.csv"):
    file_name = csv_file.stem  # Get filename without extension
    print(f"Reading {csv_file.name}...")
    delivery_dataframes[file_name] = pd.read_csv(str(csv_file))
    print(f"  Shape: {delivery_dataframes[file_name].shape}")
    print(f"  Columns: {list(delivery_dataframes[file_name].columns)}\n")

# Display summary of loaded dataframes
print("=" * 50)
print("Loaded Delivery Files Summary:")
print("=" * 50)
for name, df in delivery_dataframes.items():
    print(f"\n{name}:")
    print(f"  Records: {len(df)}")
    print(f"  Columns: {list(df.columns)}")

# Example: Access a specific dataframe
# df_cq = delivery_dataframes['delivery_cq']
# print(df_cq.head())