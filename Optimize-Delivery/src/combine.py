import dask.dataframe as dd
from pathlib import Path
import os

# Configuration
USE_HDFS = False  # Set to True to use HDFS
HDFS_PATH = "hdfs://localhost:9000/bigdata/output"  # HDFS output path
LOCAL_OUTPUT = False  # Set to True to also save locally

# Define folder paths
base_dir = Path(__file__).parent.parent.parent
delivery_folder = base_dir / "Datapack" / "Delivery"
pickup_folder = base_dir / "Datapack" / "PickUp"
roadmap_folder = base_dir / "Datapack" / "Roadmap"
output_folder = base_dir / "output"

# Create local output folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Create HDFS directory if using HDFS
if USE_HDFS:
    try:
        os.system(f"hadoop fs -mkdir -p {HDFS_PATH}")
        print(f"HDFS directory created/verified: {HDFS_PATH}")
    except Exception as e:
        print(f"Warning: Could not create HDFS directory - {str(e)}")

# List to store all dataframe paths
delivery_files = list(delivery_folder.glob("*.csv"))
pickup_files = list(pickup_folder.glob("*.csv"))
roadmap_files = list(roadmap_folder.glob("*.csv"))

all_files = []

# Add delivery files with source tag
print("Processing Delivery files...")
for csv_file in delivery_files:
    print(f"  {csv_file.name}")
    all_files.append(('delivery', str(csv_file)))

# Add pickup files with source tag
print("\nProcessing PickUp files...")
for csv_file in pickup_files:
    print(f"  {csv_file.name}")
    all_files.append(('pickup', str(csv_file)))

# Add roadmap files with source tag
print("\nProcessing Roadmap files...")
for csv_file in roadmap_files:
    print(f"  {csv_file.name}")
    all_files.append(('roadmap', str(csv_file)))

# Read and combine using Dask
if all_files:
    print("\nCombining all files with Dask...")
    dask_dfs = []
    
    for source, file_path in all_files:
        try:
            # Use blocksize=None to avoid chunking issues with malformed CSV
            ddf = dd.read_csv(file_path, blocksize=None, engine='python', on_bad_lines='skip')
            ddf['source'] = source
            dask_dfs.append(ddf)
        except Exception as e:
            print(f"  Warning: Skipping {file_path} - {str(e)}")
            continue
    
    if dask_dfs:
        # Concatenate all dask dataframes
        combined_ddf = dd.concat(dask_dfs, ignore_index=True)
        
        # Save to local folder
        if LOCAL_OUTPUT:
            output_file = str(output_folder / "combined_all_data.csv")
            print(f"Saving to local: {output_file}")
            combined_ddf.to_csv(output_file, single_file=True, index=False)
            print(f"Local file saved: {output_file}")
        
        # Save to HDFS
        if USE_HDFS:
            hdfs_output = f"{HDFS_PATH}/combined_all_data"
            print(f"Saving to HDFS: {hdfs_output}")
            combined_ddf.to_csv(hdfs_output, index=False)
            print(f"HDFS file saved: {hdfs_output}")
        
        # If neither selected, save to local by default
        if not USE_HDFS and not LOCAL_OUTPUT:
            output_file = str(output_folder / "combined_all_data.csv")
            print(f"Saving to local (default): {output_file}")
            combined_ddf.to_csv(output_file, single_file=True, index=False)
            print(f"Local file saved: {output_file}")
        
        print(f"\n{'='*50}")
        print(f"Combined file saved successfully!")
        if USE_HDFS:
            print(f"HDFS location: {HDFS_PATH}/combined_all_data")
        else:
            print(f"Local location: {output_folder}/combined_all_data.csv")
        print(f"{'='*50}")
    else:
        print("No files could be combined successfully!")
else:
    print("No CSV files found to combine!")
