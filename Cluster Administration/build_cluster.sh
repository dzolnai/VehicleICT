#! /bin/bash
#Builds a 1master/3slave cluster from scratch

echo "Creating nodes---------------------------------------"
echo "Creating manager node"
./create_new_node.sh manager 25 > /dev/null 2>&1 &
echo "Creating master node"
./create_new_node.sh master 25 > /dev/null 2>&1 &
echo "Creating slave node"
./create_new_node.sh slave-a 25 > /dev/null 2>&1 &
echo "Creating slave node"
./create_new_node.sh slave-b 25 > /dev/null 2>&1 &
echo "Creating slave node"
./create_new_node.sh slave-c 25 > /dev/null 2>&1
echo "Initializing disks (this might take a while)"
sleep 60
echo "Nodes are operational"
echo
echo "Copying installation file on manager-node------------"
gcutil push manager-node ./Util/cloudera-manager-installer.bin ~/cloudera-manager-installer.bin > /dev/null 2>&1 &
echo "Don't forget to manually install the service later"
echo
echo "Setting up hosts table-------------------------------"
gcutil listinstances --columns name,network-ip | ./Util/create_hosts_file.py
echo "Distributing hosts file"
gcutil push manager-node hosts ~/ > /dev/null 2>&1 &
gcutil push master-node hosts ~/ > /dev/null 2>&1 &
gcutil push slave-a-node hosts ~/ > /dev/null 2>&1 &
gcutil push slave-b-node hosts ~/ > /dev/null 2>&1 &
gcutil push slave-c-node hosts ~/ > /dev/null 2>&1
rm hosts
sleep 5
gcutil ssh manager-node 'sudo cp hosts /etc/hosts' > /dev/null 2>&1 &
gcutil ssh master-node 'sudo cp hosts /etc/hosts' > /dev/null 2>&1 &
gcutil ssh slave-a-node 'sudo cp hosts /etc/hosts' > /dev/null 2>&1 &
gcutil ssh slave-b-node 'sudo cp hosts /etc/hosts' > /dev/null 2>&1 &
gcutil ssh slave-c-node 'sudo cp hosts /etc/hosts' > /dev/null 2>&1
sleep 5
echo "Hosts table ready"
echo 
echo "Disabling swapping-----------------------------------"
gcutil ssh master-node "sudo sysctl vm.swappiness=0" > /dev/null 2>&1 &
gcutil ssh slave-a-node "sudo sysctl vm.swappiness=0" > /dev/null 2>&1 &
gcutil ssh slave-b-node "sudo sysctl vm.swappiness=0" > /dev/null 2>&1 &
gcutil ssh slave-c-node "sudo sysctl vm.swappiness=0" > /dev/null 2>&1 &
gcutil ssh master-node "echo 'vm.swappiness = 0' | sudo tee -a /etc/sysctl.conf" > /dev/null 2>&1 &
gcutil ssh slave-a-node "echo 'vm.swappiness = 0' | sudo tee -a /etc/sysctl.conf" > /dev/null 2>&1 &
gcutil ssh slave-b-node "echo 'vm.swappiness = 0' | sudo tee -a /etc/sysctl.conf" > /dev/null 2>&1 &
gcutil ssh slave-c-node "echo 'vm.swappiness = 0' | sudo tee -a /etc/sysctl.conf" > /dev/null 2>&1
echo "Swapping disabled"
echo
echo "Rebooting"
gcutil ssh manager-node 'sudo reboot' > /dev/null 2>&1 &
gcutil ssh master-node 'sudo reboot' > /dev/null 2>&1 &
gcutil ssh slave-a-node 'sudo reboot' > /dev/null 2>&1 &
gcutil ssh slave-b-node 'sudo reboot' > /dev/null 2>&1 &
gcutil ssh slave-c-node 'sudo reboot' > /dev/null 2>&1
sleep 20
echo "Cluster is ready! Now you should install Cloudera Manager on manager-node."

