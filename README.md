#VehicleICT
j
==========
k
##Notes
###Building the cluster
For a proper Hadoop dev cluster one needs at least 5 nodes: 1 manager, 1 master and 3 slaves. The manager node runs Cloudera Manager, which will help us administer the cluster. The master node will take the role of the HDFS NameNode and the YARN ResourceManager, as well as the role of the Secondary NameNode (seems odd to place the Secondary NameNode on the same node as the primary one, but in fact the Secondary NameNode's task is not to replace the primary one, but to support it by occasionally checkpointing the logs... worst naming ever). The slave nodes will run the HDFS DataNode and YARN NodeManager daemons. Other roles will be distributed across all the nodes, to balance load. It's important to note, that the manager and master nodes need a lot of RAM (6-8GB will do for the manager, 10-15GB for the master).
####Steps:
1. Create the permanent disks with the standard Debian 7 image Google provides.
2. Create VM instances and attach the disks to them.
3. Partition the disks, so the OS will be able to use the whole capacity.
4. Set up /etc/hosts to include the well-formed names of the nodes.
5. Disable swapping for the managed nodes, as it can hurt Hadoop performance.
6. Configure the manager node to be able to ssh to the managed nodes (gcutil creates a key which all the nodes accept, so easiest way is to copy that key).
7. Install Cloudera Manager on the manager node. The console will be shortly available at localhost:7180.
8. Configure CM to find the managed nodes and use it to deploy Hadoop on the managed cluster. (Optionally set up an HBase Thrift Server and 3 ZooKeeper nodes.)

Note: steps 1-6 are automated by *build_cluster.sh*, but steps 7-8 need to be done manually.
####Tearing down the cluster
Executing *teardown_cluster.sh* will completely destroy the cluster, throwing away the permanent disks. This can't be undone, so you should use it with care.

###Normal routine
Being a dev cluster on Google Compute Engine VMs, charges will be incurred for every minute it operates, so you should only operate it when you really need to, and hibernate it otherwise.
####Starting the cluster
Starting the cluster is relatively easy, you should consider the following steps:

1. Start the VMs and attach the permanent disks
2. As IP addresses always change, when you create new VMs, create the proper /etc/hosts files and distribute it across the cluster nodes
3. Managed nodes send heartbeats to the manager node based on a configuration file (/etc/cloudera-scm-agent/config.ini), so set the correct IP address in this file on all the nodes
4. Reboot the managed nodes, in order the configuration changes to take effect
5. Go to http://manager-node:7180, and start the cluster services with the help of Cloudera Manager

Note: steps 1-4 are automated by *start_cluster.sh*.

####Hibernating the cluster
All you need to do is to stop the cluster services on the CM Console, then execute *hibernate_cluster.sh*, which shuts down the VMs, preserving the permanent disks.

##Progress
###2014.06.30.
* Created scripts for automated cluster management
* Built a dev cluster and deployed Hadoop

###2014.07.01.
* Created simple webapp2 REST endpoint to receive data

###2014.07.03.
* Configured Flume to receive data from web server and loading it to HDFS
