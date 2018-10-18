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
	for p in proc:
		th = {}
		for c in p["calls"]:
			th.setdefault(c["thread_id"], [])
			th[c["thread_id"]].append(c["api"])
		pr.setdefault(p["process_id"], [])
		pr[p["process_id"]].append(th)
	return pr

def make_table(namelist):
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

def main(path, filename):
	allfuncs = set()
	data = {}
	for name in os.listdir(path):
		if name.find(".json") == -1:
			continue
		pl = onefile(path + name)
		if pl == None:
			continue
		for pk in pl.keys():
			for tl in pl[pk]:
				for tk in tl.keys():
					for func in tl[tk]:
						allfuncs.add(func)
		data.setdefault(name, {})
		data[name] = pl
	r = make_table(list(allfuncs))
	with open(filename + "t.pickle", "w") as f:
		pickle.dump(r, f)
	with open(filename + "p.pickle", "w") as f:
		pickle.dump(data, f)

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])

