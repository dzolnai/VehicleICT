#! /bin/bash

echo "Shutting down nodes----------------------------------"
echo "Shutting down slave node"
gcutil deleteinstance slave-a-node -f --nodelete_boot_pd > /dev/null 2>&1 &
echo "Shutting down slave node"
gcutil deleteinstance slave-b-node -f --nodelete_boot_pd > /dev/null 2>&1 &
echo "Shutting down slave node"
gcutil deleteinstance slave-c-node -f --nodelete_boot_pd > /dev/null 2>&1 &
echo "Shutting down master node"
gcutil deleteinstance master-node -f --nodelete_boot_pd > /dev/null 2>&1 &
echo "Shutting down manager node"
gcutil deleteinstance manager-node -f --nodelete_boot_pd > /dev/null 2>&1
sleep 60
echo "Nodes are shut down"
echo
echo "Removing disks---------------------------------------"
echo "Removing manager disk"
gcutil deletedisk manager-node-disk -f > /dev/null 2>&1 &
echo "Removing master disk"
gcutil deletedisk master-node-disk -f > /dev/null 2>&1 &
echo "Removing slave disk"
gcutil deletedisk slave-a-node-disk -f > /dev/null 2>&1 &
echo "Removing slave disk"
gcutil deletedisk slave-b-node-disk -f > /dev/null 2>&1 &
echo "Removing slave disk"
gcutil deletedisk slave-c-node-disk -f > /dev/null 2>&1
echo "Disks are removed"
echo
echo "Cluster is completely tore down"
echo



