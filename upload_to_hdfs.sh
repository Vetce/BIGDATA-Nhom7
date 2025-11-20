#!/bin/bash

echo "=================================================="
echo "Starting HDFS Upload Process"
echo "=================================================="

# Create main directory
echo ""
echo "📁 Creating /bigdata directory..."
hdfs dfs -mkdir -p /bigdata 2>/dev/null || true

# Upload Datapack/Delivery
echo ""
echo "📁 Uploading Datapack/Delivery..."
hdfs dfs -mkdir -p /bigdata/Datapack/Delivery
hdfs dfs -put -f /home/sirin/BIGDATA/Datapack/Delivery/*.csv /bigdata/Datapack/Delivery/
echo "✓ Uploaded Delivery files"

# Upload Datapack/PickUp
echo ""
echo "📁 Uploading Datapack/PickUp..."
hdfs dfs -mkdir -p /bigdata/Datapack/PickUp
hdfs dfs -put -f /home/sirin/BIGDATA/Datapack/PickUp/*.csv /bigdata/Datapack/PickUp/
echo "✓ Uploaded PickUp files"

# Upload Datapack/Roadmap
echo ""
echo "📁 Uploading Datapack/Roadmap..."
hdfs dfs -mkdir -p /bigdata/Datapack/Roadmap
hdfs dfs -put -f /home/sirin/BIGDATA/Datapack/Roadmap/*.csv /bigdata/Datapack/Roadmap/
echo "✓ Uploaded Roadmap files"

# Upload output
echo ""
echo "📁 Uploading output..."
hdfs dfs -mkdir -p /bigdata/output
hdfs dfs -put -f /home/sirin/BIGDATA/output/*.csv /bigdata/output/
echo "✓ Uploaded output files"

# Verify structure
echo ""
echo "=================================================="
echo "=== HDFS Directory Structure Verification ==="
echo "=================================================="
echo ""
hdfs dfs -du -h /bigdata
echo ""
echo "=== Tree View ==="
hdfs dfs -ls -R /bigdata

echo ""
echo "✓ Upload process completed!"
