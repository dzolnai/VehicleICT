#! /bin/bash
#Deletes all nodes, keeping their disks

gcutil deleteinstance manager-node -f --nodelete_boot_pd > /dev/null 2>&1 &
gcutil deleteinstance master-node -f --nodelete_boot_pd > /dev/null 2>&1 &
gcutil deleteinstance slave-a-node -f --nodelete_boot_pd > /dev/null 2>&1 &
gcutil deleteinstance slave-b-node -f --nodelete_boot_pd > /dev/null 2>&1 &
gcutil deleteinstance slave-c-node -f --nodelete_boot_pd > /dev/null 2>&1 &
gcutil deleteinstance slave-d-node -f --nodelete_boot_pd > /dev/null 2>&1 &
gcutil deleteinstance slave-e-node -f --nodelete_boot_pd > /dev/null 2>&1