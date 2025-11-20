import pandas as pd
import os
from pathlib import Path

# Get the directory of the current script
script_dir = Path(__file__).parent.parent.parent

# Define the roadmap folder path
roadmap_folder = script_dir / "Datapack" / "Roadmap"

# Check if folder exists
if not roadmap_folder.exists():
    print(f"Error: Roadmap folder not found at {roadmap_folder}")
else:
    # Dictionary to store dataframes
    roadmap_dataframes = {}
    
    # Read all CSV files from the roadmap folder
    csv_files = list(roadmap_folder.glob("*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {roadmap_folder}")
    else:
        for csv_file in csv_files:
            file_name = csv_file.stem  # Get filename without extension
            try:
                # Try reading with different engine and error handling
                df = pd.read_csv(csv_file, engine='python', on_bad_lines='skip')
                roadmap_dataframes[file_name] = df
                print(f"{file_name}:")
                print(f"  Records: {len(df)}")
                print(f"  Columns: {list(df.columns)}")
            except Exception as e:
                print(f"Error reading {csv_file.name}: {str(e)}")