#!/usr/bin/env python3
"""
Upload local folders to HDFS with the specified structure using native HDFS commands:
- /bigdata/Datapack/Delivery
- /bigdata/Datapack/PickUp
- /bigdata/Datapack/Roadmap
- /bigdata/output (including combined_all_data.csv)
"""

import subprocess
import os
import sys

def run_hdfs_command(cmd, description=""):
    """Run HDFS command and handle errors"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def hdfs_makedirs(path):
    """Create HDFS directory (parents included)"""
    success, output = run_hdfs_command(f"hdfs dfs -mkdir -p {path}")
    if success:
        print(f"✓ Created directory: {path}")
        return True
    else:
        # Directory might already exist
        return True

def hdfs_put_file(local_file, hdfs_path):
    """Upload a file to HDFS"""
    try:
        cmd = f"hdfs dfs -put -f {local_file} {hdfs_path}/"
        success, output = run_hdfs_command(cmd)
        
        if success:
            file_size = os.path.getsize(local_file)
            print(f"  ↑ Uploaded: {os.path.basename(local_file)} ({file_size:,} bytes)")
            return True
        else:
            print(f"  ✗ Upload failed: {output[:100]}")
            return False
    except Exception as e:
        print(f"  ✗ Error uploading {local_file}: {e}")
        return False

def upload_folder(local_path, hdfs_path):
    """Upload a local folder to HDFS"""
    if not os.path.exists(local_path):
        print(f"✗ Local path does not exist: {local_path}")
        return

    if not os.path.isdir(local_path):
        print(f"✗ Local path is not a directory: {local_path}")
        return

    print(f"\n📁 Processing: {local_path} -> {hdfs_path}")
    
    # Create the target directory in HDFS
    hdfs_makedirs(hdfs_path)
    
    # Upload all files in the directory
    try:
        files_uploaded = 0
        for filename in os.listdir(local_path):
            local_file = os.path.join(local_path, filename)
            
            if os.path.isfile(local_file):
                if hdfs_put_file(local_file, hdfs_path):
                    files_uploaded += 1
            elif os.path.isdir(local_file):
                print(f"  → Subdirectory: {filename}")
                hdfs_makedirs(f"{hdfs_path}/{filename}")
        
        print(f"  Summary: {files_uploaded} files uploaded")
    except Exception as e:
        print(f"✗ Error uploading to {hdfs_path}: {e}")

def verify_structure():
    """Verify the uploaded structure in HDFS"""
    print("\n" + "="*50)
    print("=== HDFS Verification ===")
    print("="*50 + "\n")
    
    success, output = run_hdfs_command("hdfs dfs -ls -R /bigdata")
    if success:
        print(output)
    else:
        print(f"Error listing /bigdata: {output}")

# Main execution
if __name__ == "__main__":
    print("="*50)
    print("Starting HDFS Upload Process")
    print("="*50)
    
    # Test connection
    print("\n🔗 Testing connection to HDFS...")
    success, output = run_hdfs_command("hdfs dfsadmin -report 2>/dev/null | head -1")
    if success:
        print(f"✓ Connected to HDFS successfully")
    else:
        print(f"✗ Cannot connect to HDFS: {output}")
        sys.exit(1)
    
    # Step 1: Create main bigdata directory
    hdfs_makedirs("/bigdata")
    
    # Step 2: Define the mappings of local paths to HDFS paths
    uploads = [
        ("/home/sirin/BIGDATA/Datapack/Delivery", "/bigdata/Datapack/Delivery"),
        ("/home/sirin/BIGDATA/Datapack/PickUp", "/bigdata/Datapack/PickUp"),
        ("/home/sirin/BIGDATA/Datapack/Roadmap", "/bigdata/Datapack/Roadmap"),
        ("/home/sirin/BIGDATA/output", "/bigdata/output"),
    ]
    
    # Check if Inventory exists before adding it
    if os.path.exists("/home/sirin/BIGDATA/Datapack/Inventory"):
        uploads.append(("/home/sirin/BIGDATA/Datapack/Inventory", "/bigdata/Datapack/Inventory"))
    
    # Step 3: Upload folders
    for local_path, hdfs_path in uploads:
        upload_folder(local_path, hdfs_path)
    
    # Step 4: Verify structure
    verify_structure()
    
    print("\n✓ Upload process completed!")
