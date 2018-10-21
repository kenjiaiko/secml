#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import pickle

def onefile(path):
	try:
		data = json.loads(open(path).read())
		proc = data["behavior"]["processes"]
	except:
		print path
		return None
	pr = {}
	ff = []
	for p in proc:
		th = {}
		for c in p["calls"]:
			if ff == []:
				try:
					xx = c["tid"]
					ff = ["tid", "pid"]
				except:
					ff = ["thread_id", "process_id"]
			th.setdefault(c[ff[0]], [])
			th[c[ff[0]]].append(c["api"])
		if ff == []:
			continue
		pr.setdefault(p[ff[1]], [])
		pr[p[ff[1]]].append(th)
	return pr

def maketable(namelist):
	name2num = {}
	num2name = {}
	i = 1
	for v in list(set(namelist)):
		name2num.setdefault(v, 0)
		name2num[v] = i
		num2name.setdefault(i, "")
		num2name[i] = v
		i += 1
	r = { "name2num": name2num, "num2name": num2name }
	return r

def main(srcpath, dstpath, dirname):
	data = {}
	allfuncs = set()
	os.mkdir(dstpath + dirname)
	i = 0
	for name in os.listdir(srcpath):
		if name.find(".json") == -1:
			continue
		pl = onefile(srcpath + name)
		if pl == None:
			continue
		for pk in pl.keys():
			for tl in pl[pk]:
				for tk in tl.keys():
					for func in tl[tk]:
						allfuncs.add(func)
		data.setdefault(name, {})
		data[name] = pl
		i += 1
		if i % 100 == 0:
			w = dstpath + dirname + "/" + str(i / 100) + ".pickle"
			with open(w, "wb") as f:
				pickle.dump(data, f)
			data = {}
	r = maketable(list(allfuncs))
	with open(dstpath + dirname + "/t.pickle", "wb") as f:
		pickle.dump(r, f)

if __name__ == "__main__":
	srcpath = sys.argv[1]
	dstpath = sys.argv[2]
	dirname = sys.argv[3]
	main(srcpath, dstpath, dirname)
