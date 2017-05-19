#!/usr/bin/env python
# -*- coding:utf-8 -*-

def csv_read(filename):
	import csv
	with open(filename, 'r') as fd:
		data=[[float(elm) for elm in v] for v in csv.reader(fd)]
	return data
