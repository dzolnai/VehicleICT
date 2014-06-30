#! /usr/bin/python

import sys

data = sys.stdin

for line in data:
	if line[0] == '|':
		line = line[1:-2].split('|')
		line = [em.strip() for em in line]
		if line[0] == 'manager-node':
			print line[1],