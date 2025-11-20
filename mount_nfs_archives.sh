#!/bin/bash
# NFS Mount Script for archives folder
# Usage: bash mount_nfs_archives.sh <mount_point>

MOUNT_POINT="${1:-/mnt/archives}"
NFS_SERVER="sirin-LOQ-15IRH8"
NFS_PATH="/home/sirin/BIGDATA/archives"

echo "Mounting NFS share from $NFS_SERVER:$NFS_PATH to $MOUNT_POINT"

# Create mount point if it doesn't exist
sudo mkdir -p "$MOUNT_POINT"

# Mount the NFS share
sudo mount -t nfs "$NFS_SERVER:$NFS_PATH" "$MOUNT_POINT"

# Verify mount
if mountpoint -q "$MOUNT_POINT"; then
    echo "✓ Successfully mounted NFS share at $MOUNT_POINT"
    df -h "$MOUNT_POINT"
else
    echo "✗ Failed to mount NFS share"
    exit 1
fi

# To add to /etc/fstab for permanent mounting:
# echo "$NFS_SERVER:$NFS_PATH $MOUNT_POINT nfs defaults,nofail 0 0" | sudo tee -a /etc/fstab
