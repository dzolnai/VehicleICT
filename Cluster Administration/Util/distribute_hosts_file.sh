#! /bin/bash
gcutil listinstances --columns name,network-ip | ./create_hosts_file.py
gcutil push manager-node hosts /home/ujj/
gcutil push master-node hosts /home/ujj/
gcutil push slave-a-node hosts /home/ujj/
gcutil push slave-b-node hosts /home/ujj/
gcutil push slave-c-node hosts /home/ujj/
gcutil ssh manager-node 'sudo cp hosts /etc/hosts'
gcutil ssh master-node 'sudo cp hosts /etc/hosts'
gcutil ssh slave-a-node 'sudo cp hosts /etc/hosts'
gcutil ssh slave-b-node 'sudo cp hosts /etc/hosts'
gcutil ssh slave-c-node 'sudo cp hosts /etc/hosts'
gcutil ssh manager-node 'rm /home/ujj/hosts'
gcutil ssh master-node 'rm /home/ujj/hosts'
gcutil ssh slave-a-node 'rm /home/ujj/hosts'
gcutil ssh slave-b-node 'rm /home/ujj/hosts'
gcutil ssh slave-c-node 'rm /home/ujj/hosts'
