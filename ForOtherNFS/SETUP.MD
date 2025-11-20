
1/

python3 mount_nfs_client.py /mnt/archives


# Hướng dẫn mount NFS share từ server

## 1. Chuẩn bị
- Máy client cần cài NFS client utilities:
```bash
sudo apt update
sudo apt install nfs-common -y

Check mount

df -h | grep archives
ls -la /mnt/archives
