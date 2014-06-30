#! /usr/bin/python
#Creates well-formatted host-files for the nodes

import sys

data = sys.stdin

with open('hosts', 'w') as f:
	for line in data:
		if line[0] == '|':
			line = line[1:-2].split('|')
			line = [em.strip() for em in line]
			if line[0] == 'name':
				f.write('127.0.0.1 localhost.localdomain localhost\n')
			else:
				f.write('{0} {1}.c.hadoop-project-1.internal {1}\n'.format(line[1], line[0]))