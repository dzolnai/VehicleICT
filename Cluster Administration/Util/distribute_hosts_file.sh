#! /bin/bash

gcutil listinstances --columns name,network-ip | ./Util/create_hosts_file.py
gcutil push manager-node hosts ~/
gcutil push master-node hosts ~/
gcutil push slave-a-node hosts ~/
gcutil push slave-b-node hosts ~/
gcutil push slave-c-node hosts ~/
gcutil ssh manager-node 'sudo cp hosts /etc/hosts'
gcutil ssh master-node 'sudo cp hosts /etc/hosts'
gcutil ssh slave-a-node 'sudo cp hosts /etc/hosts'
gcutil ssh slave-b-node 'sudo cp hosts /etc/hosts'
gcutil ssh slave-c-node 'sudo cp hosts /etc/hosts'
gcutil ssh manager-node 'rm ~/hosts'
gcutil ssh master-node 'rm ~/hosts'
gcutil ssh slave-a-node 'rm ~/hosts'
gcutil ssh slave-b-node 'rm ~/hosts'
gcutil ssh slave-c-node 'rm ~/hosts'
