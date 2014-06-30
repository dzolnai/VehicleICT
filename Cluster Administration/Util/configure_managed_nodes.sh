#! /bin/bash
#Distributes the configuration file (which contains the manager node's IP) across the managed nodes

gcutil listinstances --columns name,network-ip | ./get_manager_ip.py | ./create_slave_config_file.py
gcutil push master-node config.ini ~/
gcutil push slave-a-node config.ini ~/
gcutil push slave-b-node config.ini ~/
gcutil push slave-c-node config.ini ~/
gcutil ssh master-node 'sudo cp config.ini /etc/cloudera-scm-agent/config.ini'
gcutil ssh slave-a-node 'sudo cp config.ini /etc/cloudera-scm-agent/config.ini'
gcutil ssh slave-b-node 'sudo cp config.ini /etc/cloudera-scm-agent/config.ini'
gcutil ssh slave-c-node 'sudo cp config.ini /etc/cloudera-scm-agent/config.ini'
gcutil ssh master-node 'rm ~/config.ini'
gcutil ssh slave-a-node 'rm ~/config.ini'
gcutil ssh slave-b-node 'rm ~/config.ini'
gcutil ssh slave-c-node 'rm ~/config.ini'