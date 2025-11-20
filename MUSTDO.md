rm -rf /tmp/hadoop-sirin/dfs/name
rm -rf /tmp/hadoop-sirin/dfs/data
mkdir -p /tmp/hadoop-sirin/dfs/name
mkdir -p /tmp/hadoop-sirin/dfs/data

chmod -R 777 /tmp/hadoop-sirin


hdfs namenode -format

start-dfs.sh
start-yarn.sh


jps

stop-dfs.sh
stop-yarn.sh