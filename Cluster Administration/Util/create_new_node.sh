#! /bin/bash
#Creates a new node with name arg[0] size arg[1]

gcutil adddisk $1-node-disk --source_image=debian-7 --size_gb=$2 --zone=europe-west1-b
sleep 10
gcutil addinstance $1-node --disk=$1-node-disk,boot --machine_type=n1-standard-1 --zone=europe-west1-b
sleep 40
gcutil ssh $1-node "echo -e 'd\nn\n\n\n\n\nw\n' | sudo fdisk /dev/sda"
sleep 5
gcutil ssh $1-node 'sudo reboot'
sleep 60
gcutil ssh $1-node 'sudo resize2fs /dev/sda1'
