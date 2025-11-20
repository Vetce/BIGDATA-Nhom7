#!/usr/bin/env python3
"""
NFS Setup Script for /home/sirin/BIGDATA/archives

This script configures NFS (Network File System) for the archives folder,
enabling network-based file sharing and storage management.
"""

import os
import subprocess
import sys
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NFSSetup:
    """Handles NFS configuration and setup for the archives folder."""
    
    def __init__(self):
        self.archives_path = "/home/sirin/BIGDATA/archives"
        self.nfs_config_file = "/etc/exports"
        self.nfs_mount_options = "rw,sync,no_subtree_check,no_root_squash"
        
    def check_prerequisites(self):
        """Check if NFS server tools are installed."""
        logger.info("Checking NFS prerequisites...")
        
        try:
            subprocess.run(
                ["which", "exportfs"],
                check=True,
                capture_output=True
            )
            logger.info("✓ NFS utilities are installed")
            return True
        except subprocess.CalledProcessError:
            logger.error("✗ NFS utilities not found. Please install nfs-kernel-server")
            logger.info("Install with: sudo apt-get install nfs-kernel-server")
            return False
    
    def ensure_archives_directory(self):
        """Ensure the archives directory exists with proper permissions."""
        logger.info(f"Ensuring archives directory exists: {self.archives_path}")
        
        try:
            Path(self.archives_path).mkdir(parents=True, exist_ok=True)
            os.chmod(self.archives_path, 0o777)
            logger.info(f"✓ Directory ready: {self.archives_path}")
            return True
        except PermissionError:
            logger.error(f"✗ Permission denied creating/modifying {self.archives_path}")
            logger.info("Try: sudo chown -R $USER:$USER /home/sirin/BIGDATA/archives")
            return False
        except Exception as e:
            logger.error(f"✗ Error creating directory: {e}")
            return False
    
    def get_network_interfaces(self):
        """Get available network interfaces for NFS configuration."""
        logger.info("Detecting network interfaces...")
        
        try:
            result = subprocess.run(
                ["hostname", "-I"],
                capture_output=True,
                text=True,
                check=True
            )
            ips = result.stdout.strip().split()
            logger.info(f"Available IPs: {ips}")
            return ips
        except Exception as e:
            logger.error(f"Could not detect network interfaces: {e}")
            return ["127.0.0.1", "192.168.1.0/24"]
    
    def configure_nfs_exports(self):
        """Configure NFS exports for the archives folder."""
        logger.info(f"Configuring NFS exports for {self.archives_path}")
        
        try:
            # Check if already configured
            with open(self.nfs_config_file, 'r') as f:
                content = f.read()
                if self.archives_path in content:
                    logger.info("✓ Archives path already in NFS exports")
                    return True
        except FileNotFoundError:
            logger.warning(f"{self.nfs_config_file} not found, creating backup strategy")
        except PermissionError:
            logger.error("✗ Permission denied reading /etc/exports")
            logger.info("Try: sudo")
            return False
        
        # Generate NFS export entry
        export_entry = f"\n# NFS Export for BIGDATA Archives\n{self.archives_path} *(${self.nfs_mount_options})\n"
        
        logger.info(f"Export entry:\n{export_entry}")
        logger.info("To apply this configuration, run:")
        logger.info(f"echo '{export_entry}' | sudo tee -a {self.nfs_config_file}")
        logger.info("sudo exportfs -a -v")
        
        return True
    
    def start_nfs_services(self):
        """Start NFS services."""
        logger.info("Starting NFS services...")
        
        services = [
            "nfs-server",
            "rpc-statd",
            "rpc-mountd"
        ]
        
        logger.info("To start NFS services, run:")
        for service in services:
            logger.info(f"sudo systemctl start {service}")
            logger.info(f"sudo systemctl enable {service}")
        
        return True
    
    def verify_nfs_setup(self):
        """Verify NFS configuration."""
        logger.info("Verifying NFS setup...")
        
        logger.info("To verify NFS exports, run:")
        logger.info("sudo exportfs -v")
        logger.info("\nTo check NFS services status, run:")
        logger.info("sudo systemctl status nfs-server")
        logger.info("showmount -e localhost")
        
        return True
    
    def generate_mount_script(self):
        """Generate a script for mounting the NFS share on clients."""
        script_path = "/home/sirin/BIGDATA/mount_nfs_archives.sh"
        
        hostname = subprocess.run(
            ["hostname", "-f"],
            capture_output=True,
            text=True
        ).stdout.strip()
        
        mount_script = f"""#!/bin/bash
# NFS Mount Script for archives folder
# Usage: bash mount_nfs_archives.sh <mount_point>

MOUNT_POINT="${{1:-/mnt/archives}}"
NFS_SERVER="{hostname}"
NFS_PATH="{self.archives_path}"

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
"""
        
        try:
            with open(script_path, 'w') as f:
                f.write(mount_script)
            os.chmod(script_path, 0o755)
            logger.info(f"✓ Mount script generated: {script_path}")
            return True
        except Exception as e:
            logger.error(f"Error generating mount script: {e}")
            return False
    
    def print_setup_guide(self):
        """Print complete setup guide."""
        guide = f"""
{'='*70}
NFS SETUP GUIDE FOR {self.archives_path}
{'='*70}

STEP 1: Install NFS Server (if not already installed)
   sudo apt-get update
   sudo apt-get install nfs-kernel-server

STEP 2: Configure /etc/exports
   Add the following line to /etc/exports:
   
   {self.archives_path} *(${self.nfs_mount_options})
   
   Run:
   echo '{self.archives_path} *(${self.nfs_mount_options})' | sudo tee -a /etc/exports

STEP 3: Export NFS Shares
   sudo exportfs -a -v

STEP 4: Start NFS Services
   sudo systemctl start nfs-server
   sudo systemctl start rpc-statd
   sudo systemctl start rpc-mountd
   
   Enable auto-start:
   sudo systemctl enable nfs-server
   sudo systemctl enable rpc-statd
   sudo systemctl enable rpc-mountd

STEP 5: Verify NFS Setup
   Check exports:
   sudo exportfs -v
   
   Check service status:
   sudo systemctl status nfs-server
   
   List available exports:
   showmount -e localhost

STEP 6: Mount on Client (if different machine)
   mkdir -p /mnt/archives
   sudo mount -t nfs <server>:{self.archives_path} /mnt/archives
   
   Or use the generated script:
   bash /home/sirin/BIGDATA/mount_nfs_archives.sh

STEP 7: Verify Mount
   df -h | grep archives
   ls -la /mnt/archives

STEP 8: Persistent Mount (Optional)
   Add to /etc/fstab:
   <server>:{self.archives_path} /mnt/archives nfs defaults,nofail 0 0

   Then remount all:
   sudo mount -a

TROUBLESHOOTING:
   
   Check if NFS is listening:
   sudo netstat -tulpn | grep nfs
   
   Check ports (2049 for NFS):
   sudo ss -tlnp | grep 2049
   
   View NFS server logs:
   sudo journalctl -u nfs-server -f
   
   Reload exports without restart:
   sudo exportfs -ra

{'='*70}
"""
        print(guide)
        logger.info("Setup guide printed")
    
    def setup(self):
        """Execute complete NFS setup."""
        logger.info("Starting NFS setup for archives folder...")
        logger.info("="*70)
        
        # Print setup guide
        self.print_setup_guide()
        
        # Execute setup steps
        steps = [
            ("Checking prerequisites", self.check_prerequisites),
            ("Ensuring archives directory", self.ensure_archives_directory),
            ("Detecting network interfaces", self.get_network_interfaces),
            ("Configuring NFS exports", self.configure_nfs_exports),
            ("Starting NFS services", self.start_nfs_services),
            ("Verifying NFS setup", self.verify_nfs_setup),
            ("Generating mount script", self.generate_mount_script),
        ]
        
        for step_name, step_func in steps:
            try:
                logger.info(f"\n{step_name}...")
                result = step_func()
                if result:
                    logger.info(f"✓ {step_name} completed")
                else:
                    logger.warning(f"⚠ {step_name} completed with warnings")
            except Exception as e:
                logger.error(f"✗ Error during {step_name}: {e}")
        
        logger.info("\n" + "="*70)
        logger.info("NFS setup configuration complete!")
        logger.info("Note: Some steps require sudo privileges to execute")
        logger.info("="*70)


def main():
    """Main entry point."""
    try:
        nfs_setup = NFSSetup()
        nfs_setup.setup()
    except KeyboardInterrupt:
        logger.info("\nSetup interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
