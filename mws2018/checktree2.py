#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import pickle
import random
import threading
import time
import pickle

import suffixtree2

def main(path, year, slen, point, tablepath):
	with open(year + ".pickle", "rb") as f:
		tree = pickle.load(f)
	with open(tablepath + "/t.pickle", "rb") as f:
		table = pickle.load(f)
	# --
	total = 0
	count = 0
	for name in os.listdir(path):
		if name == "t.pickle":
			continue
		with open(path + "/" + name, "rb") as f:
			data = pickle.load(f)
		for name in data.keys():
			total += 1
			if type(None) == type(data[name]):
				continue
			flag1 = 0
			for pid in data[name].keys():
				for proc in data[name][pid]:
					for tid in proc.keys():
						nums = []
						for func in proc[tid]:
							try:
								nums.append(table["name2num"][func])
							except:
								nums.append(-1)
						ll = 0
						mm = 0
						for v in tree.score(nums):
							if point <= v:
								ll += 1
							else:
								if mm < ll:
									mm = ll
								ll = 0
						if slen <= mm:
							flag1  = 1
							count += 1
							break
						if flag1 == 1:
							break
					if flag1 == 1:
						break
				if flag1 == 1:
					break
	print count, total, count / float(total)

if __name__ == '__main__':
	sys.setrecursionlimit(1000000)
	main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
