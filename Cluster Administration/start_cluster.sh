#! /bin/bash
#Starts the cluster from sleep mode

echo "Starting nodes"
gcutil addinstance manager-node --disk=manager-node-disk,boot --machine_type=n1-standard-2 --zone=europe-west1-b > /dev/null 2>&1 &
gcutil addinstance master-node --disk=master-node-disk,boot --machine_type=n1-highmem-2 --zone=europe-west1-b > /dev/null 2>&1 &
gcutil addinstance slave-a-node --disk=slave-a-node-disk,boot --machine_type=n1-standard-1 --zone=europe-west1-b > /dev/null 2>&1 &
gcutil addinstance slave-b-node --disk=slave-b-node-disk,boot --machine_type=n1-standard-1 --zone=europe-west1-b > /dev/null 2>&1 &
gcutil addinstance slave-c-node --disk=slave-c-node-disk,boot --machine_type=n1-standard-1 --zone=europe-west1-b > /dev/null 2>&1
sleep 60
echo "Distributing hosts file"
./Util/distribute_hosts_file.sh
echo "Distributing config.ini file to managed nodes"
./Util/configure_managed_nodes.sh
echo "Rebooting managed nodes"
gcutil ssh master-node "sudo reboot" > /dev/null 2>&1 &
gcutil ssh slave-a-node "sudo reboot" > /dev/null 2>&1 &
gcutil ssh slave-b-node "sudo reboot" > /dev/null 2>&1 &
gcutil ssh slave-c-node "sudo reboot" > /dev/null 2>&1
sleep 60
echo
echo "Nodes started"

 
