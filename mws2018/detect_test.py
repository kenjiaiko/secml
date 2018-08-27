#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import sys
import csv
import random
import threading
import time

import suffixtree

def longstr(r, k, v):
	R = []
	i = 0
	j = 0
	d = ""
	f = False
	for c in r:
		if c == 0:
			i += 1
			j  = 0
			f  = False
			continue
		if f == False:
			if 0 < len(d):
				R.append(d)
			d = ""
		if v < c:
			f = True
			d += k[i+j:i+j+1]
		else:
			f = False
		j += 1
	if len(R) == 0:
		return ""
	return sorted(R, key=lambda x:len(x), reverse=True)[0]

# main

# python this.py 20 15
treeval = int(sys.argv[1])
strlen  = int(sys.argv[2])

total = json.loads(open("malware.csv.json").read())
clean = json.loads(open("cleanware.csv.json").read())[""]

dataset = []
dataset = total["201701"] 
#dataset += total["201702"] 
#dataset += total["201703"] 
#dataset += total["201704"] 
#dataset += total["201705"] 
#dataset += total["201706"] 
#dataset += total["201707"] 
#dataset += total["201708"] 
#dataset += total["201709"] 
#dataset += total["201710"] 
#dataset += total["201711"] 
future = "201702"

random.shuffle(clean)
dataset += clean[:len(dataset)]

future_dataset = total[future]
future_mal_size = len(future_dataset)

#
# dataset = past data
# future_dataset = future data
# future_mal_size = len(future data)
# 

data = {}
for v in dataset:
	ssd = v[0] # ssdeep
	imf = v[1] # imf
	# --
	data.setdefault(ssd, 0)
	data[ssd] += 1

print "1.step: read ok"

sys.setrecursionlimit(1000000)

addi1 = {}
addi2 = {}
addi3 = {}

h1 = suffixtree.ST()
for k, v in sorted(data.items(), key=lambda x:x[1], reverse=True):
	if v < 2:
		addi1.setdefault(k[:20], [])
		addi1[k[:20]].append(k)
		# --
		addi2.setdefault(k[20:40], [])
		addi2[k[20:40]].append(k)
		# --
		addi3.setdefault(k[40:60], [])
		addi3[k[40:60]].append(k)
		continue
	h1.update(k, v)

for k in addi1.keys():
	if len(addi1[k]) < 2:
		continue
	h1.update(k, len(addi1[k]))
# --
for k in addi2.keys():
	if len(addi2[k]) < 2:
		continue
	h1.update(k, len(addi2[k]))
# --
for k in addi3.keys():
	if len(addi3[k]) < 2:
		continue
	h1.update(k, len(addi3[k]))

print "2.step: update ok"

total = {}
for k, v in sorted(data.items(), key=lambda x:x[1], reverse=True):
	r = h1.score(k)
	r = longstr(r, k, treeval)
	if strlen < len(r):
		total.setdefault(r[:strlen], 0)
		total[r[:strlen]] += 1

print "3.step: score ok"

print "turn.1"

cnt = 0
for v in future_dataset:
	v = v[0]
	for w in total.keys():
		if v.find(w) != -1:
			cnt += 1
			break
print cnt, len(future_dataset)

whitelist = set()

cnt = 0
for v in clean:
	v = v[0]
	f = False
	for w in total.keys():
		if v.find(w) != -1:
			whitelist.add(w)
			if f == False:
				cnt += 1
			f = True
print cnt, len(clean)

print "turn.2"

cnt = 0
for v in future_dataset:
	v = v[0]
	for w in total.keys():
		if w in whitelist:
			continue
		if v.find(w) != -1:
			cnt += 1
			break
print cnt, len(future_dataset)

cnt = 0
for v in clean:
	v = v[0]
	for w in total.keys():
		if w in whitelist:
			continue
		if v.find(w) != -1:
			cnt += 1
			break
print cnt, len(clean)

