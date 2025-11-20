import dask.dataframe as dd
from pathlib import Path
import gc

# Define folder paths
base_dir = Path(__file__).parent.parent.parent
delivery_folder = base_dir / "Datapack" / "Delivery"
pickup_folder = base_dir / "Datapack" / "PickUp"
roadmap_folder = base_dir / "Datapack" / "Roadmap"
output_folder = base_dir / "output"

# Create local output folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Dask configuration for memory efficiency
import dask
dask.config.set({'dataframe.shuffle.method': 'tasks'})
dask.config.set({'dataframe.convert-string': False})

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

# Read and combine using Dask with optimized settings
if all_files:
    print("\nCombining all files with Dask (optimized for large files)...")
    dask_dfs = []
    
    for source, file_path in all_files:
        try:
            # Use efficient chunking: 64MB blocks for better performance
            ddf = dd.read_csv(
                file_path, 
                blocksize='64MB',  # Chunk size for memory efficiency
                engine='python',
                on_bad_lines='skip'
            )
            ddf['source'] = source
            dask_dfs.append(ddf)
            print(f"  Loaded {file_path.split('/')[-1]}")
        except Exception as e:
            print(f"  Warning: Skipping {file_path} - {str(e)}")
            continue
    
    if dask_dfs:
        # Concatenate all dask dataframes
        print("\nConcatenating dataframes...")
        combined_ddf = dd.concat(dask_dfs, ignore_index=True)
        
        # Optimize partitions
        combined_ddf = combined_ddf.repartition(npartitions=50)
        
        # Save to output folder with partitioning for efficiency
        output_file = str(output_folder / "combined_all_data")
        print(f"Saving to: {output_file}")
        combined_ddf.to_csv(output_file, single_file=True, index=False)
        
        # Cleanup
        gc.collect()
        
        print(f"\n{'='*50}")
        print(f"Combined file saved successfully!")
        print(f"Output location: {output_file}.csv")
        print(f"{'='*50}")
    else:
        print("No files could be combined successfully!")
else:
    print("No CSV files found to combine!")
