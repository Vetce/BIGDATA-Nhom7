#!/usr/bin/env python3
"""
NFS Client Mount Script
Mounts the NFS share from the server to a local folder.
"""

import os
import subprocess
import sys
from pathlib import Path

# Cấu hình NFS server
NFS_SERVER = "sirin-LOQ-15IRH8"  # đổi thành hostname/IP của server
NFS_PATH = "/home/sirin/BIGDATA/archives"

# Thư mục mount mặc định
DEFAULT_MOUNT = "/mnt/archives"

def mount_nfs(mount_point=DEFAULT_MOUNT):
    print(f"Mounting NFS share from {NFS_SERVER}:{NFS_PATH} to {mount_point}")

    # Tạo thư mục nếu chưa có
    Path(mount_point).mkdir(parents=True, exist_ok=True)

    # Mount NFS
    cmd = ["sudo", "mount", "-t", "nfs", f"{NFS_SERVER}:{NFS_PATH}", mount_point]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Successfully mounted NFS share at {mount_point}")
        subprocess.run(["df", "-h", mount_point])
    else:
        print(f"✗ Failed to mount NFS share")
        print(result.stderr)
        sys.exit(1)
    
    print("\nTo mount automatically at boot, add to /etc/fstab:")
    print(f"{NFS_SERVER}:{NFS_PATH} {mount_point} nfs defaults,nofail 0 0")

def main():
    mount_point = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MOUNT
    mount_nfs(mount_point)

if __name__ == "__main__":
    main()
