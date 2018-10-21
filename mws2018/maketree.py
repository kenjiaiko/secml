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

def enc(x):
	return str(x)[1:-1]

def dec(x):
	return map(lambda v:int(v), x.split(", "))

def ngram(s, N):
	r = {}
	p = 0
	while 1:
		v = s[p:p+N]
		if len(v) != N:
			break
		v = enc(v)
		r.setdefault(v, 0)
		r[v] += 1
		p += 1
	return r

def name2num(data, k, table, sz):
	nums = []
	for f in data["funcs"][k]:
		nums.append(table["name2num"][f])
	return nums

def _t(filepath, blacks_th, lock, table, blacks):
	if 1:
		with open(filepath, "rb") as f:
			data = pickle.load(f)
		for name in data.keys():
			flag1 = 0
			onetree = {}
			if type(None) == type(data[name]):
				continue
			for pid in data[name].keys():
				for proc in data[name][pid]:
					for tid in proc.keys():
						nums = []
						for func in proc[tid]:
							nums.append(table["name2num"][func])
						flist = str(nums)[1:-1]
						for b in blacks:
							if flist.find(b) != -1:
								lock.acquire()
								blacks_th.setdefault(b, 0)
								blacks_th[b] += 1
								lock.release()
								flag1 = 1
								break
						if flag1 == 1:
							break
					if flag1 == 1:
						break
				if flag1 == 1:
					break
	return

def main(sz, path):
	with open(path + "/t.pickle", "rb") as f:
		table = pickle.load(f)
	# --
	alltree = {}
	for name in os.listdir(path):
		if name == "t.pickle":
			continue
		with open(path + "/" + name, "rb") as f:
			data = pickle.load(f)
		for name in data.keys():
			onetree = {}
			if type(None) == type(data[name]):
				continue
			for pid in data[name].keys():
				for proc in data[name][pid]:
					for tid in proc.keys():
						nums = []
						for func in proc[tid]:
							nums.append(table["name2num"][func])
						tfu = ngram(nums, sz)
						for k1 in tfu.keys():
							onetree.setdefault(k1, 0)
							onetree[k1] = 1
			for k2 in onetree.keys():
				alltree.setdefault(k2, 0)
				alltree[k2] += 1
	# --
	blacks = []
	for k, v in sorted(alltree.items(), key=lambda x:x[1], reverse=True):
		if v < 2:
			break
		blacks.append(k)
	# --
	blacks_th = {}
	lock = threading.Lock()
	for name in os.listdir(path):
		if name == "t.pickle":
			continue
		while 30 < len(threading.enumerate()):
			time.sleep(1)
		threading.Thread(target=_t, name="_t", args=(path + "/" + name, blacks_th, lock, table, blacks, )).start()
	# --
	while 1 < len(threading.enumerate()):
		time.sleep(1)
	h1 = suffixtree2.ST()
	for k, v in sorted(blacks_th.items(), key=lambda x:x[1], reverse=True):
		threading.Thread(target=h1.update, name="_t", args=(dec(k), v, )).start()
	with open("tree.pickle", "wb") as f:
		pickle.dump(h1, f)

if __name__ == '__main__':
	sys.setrecursionlimit(1000000)
	main(int(sys.argv[1]), sys.argv[2])

