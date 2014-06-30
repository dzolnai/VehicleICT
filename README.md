#VehicleICT
==========
##Notes
###Building the cluster
For a proper Hadoop dev cluster one needs at least 5 nodes: 1 manager, 1 master and 3 slaves. The manager node runs Cloudera Manager, which will help us administer the cluster. The master node will take the role of the HDFS NameNode and the YARN ResourceManager, as well as the role of the Secondary NameNode (seems odd to place the Secondary NameNode on the same node as the primary one, but in fact the Secondary NameNode's task is not to replace the primary one, but to support it by occasionally checkpointing the logs... worst naming ever). The slave nodes will run the HDFS DataNode and YARN NodeManager daemons. Other roles will be distributed across all the nodes, to balance load. It's important, that the manager and master nodes need a lot of RAM (6-8GB will do).
####The steps:
1. Create the permanent disks with the standard Debian 7 image Google provides.
2. Create VM instances and attach the disks to them.
3. Partition the disks, so the OS will be able to use the whole capacity.
4. Set up /etc/hosts to include the well-formed names of the nodes.
5. Disable swapping for the managed nodes, as it can hurt Hadoop performance.
6. Configure the manager node to be able to ssh to the managed nodes (gcutil creates a key, which all the nodes accept, so easiest way is to copy that key).
7. Install Cloudera Manager on the manager node. The console will be shortly available on localhost:7180.

##Progress
###2014.06.30.
* Created scripts for automated cluster management
* Initialized cluster
