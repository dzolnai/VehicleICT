#VehicleICT
==========
##Notes
###Building the cluster
For a proper Hadoop dev cluster one needs at least 5 nodes: 1 manager, 1 master and 3 slaves. The manager node runs Cloudera Manager, which will help us administer the cluster. The master node will take the role of the HDFS NameNode and the YARN ResourceManager, as well as the role of the Secondary NameNode (seems odd to place the Secondary NameNode on the same node as the primary one, but in fact the Secondary NameNode's task is not to replace the primary one, but to support it by occasionally checkpointing the logs... worst naming ever). The slave nodes will run the DataNode and NodeManager daemons. 
##Progress
###2014.06.30.
* Created scripts for automated cluster management
* Initialized cluster
