#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import time
import random

import lcs
import suffixtree2

def check(s, p):
	i = 0
	for c in s:
		if c == p[i]:
			i += 1
			if len(p) <= i:
				return True
	return False

def main(filepath):
	dataset = json.loads(open(filepath).read())["dataset"]
	original = {}
	sequences= {}
	for d in dataset:
		original.setdefault(d, 0)
		original[d] += 1
	keys = original.keys()
	for i in range(len(keys)):
		for j in range(i+1, len(keys)):
			lcs_result = lcs.lcs(keys[i], keys[j])
			for l in lcs_result:
				if len(l) < 3:
					continue
				str_result = ""
				for c in l:
					str_result += c
				sequences.setdefault(str_result, 0)
				sequences[str_result] += 1
	result = {}
	h = suffixtree2.ST(sequences)
	alldata = h.print_tree(h.get(), 3)
	for k, v in sorted(alldata.items(), key=lambda x:x[1], reverse=True):
		_cnt = 0
		for s in keys:
			if check(s, k) == True:
				_cnt += 1
		result.setdefault(k, 0)
		result[k] = _cnt
	for k, v in sorted(result.items(), key=lambda x:x[1], reverse=True):
		print k + " was included in " + str(v) + " data."

if __name__ == "__main__": 
	sys.setrecursionlimit(1000000)
	main(sys.argv[1])

