#! /usr/bin/python

import re
import sys
import os

host_pattern = re.compile('#HOST#')
address = sys.stdin.readline()

with open('config.temp') as f:
	out = open('config.tmp', 'w')
	for line in f:
		out.write(re.sub(host_pattern, address, line))
	out.close()
	os.rename('config.tmp', 'config.ini')
