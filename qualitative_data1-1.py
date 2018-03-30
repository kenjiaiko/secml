#!/usr/bin/env python
# coding: utf-8

import sys

result = {}

dataset = [
	"ECAEA", "ECAAD", "ECACA", "ECABB", "ECACA", # ECA**
	"FBABF", "ABABC", "DBABA",                   # *BAB*
	"ABCDE",
	"DDFEA",
	"BCDAA",
	"FFFED",
	"AAAAA",
	"EEEEE",
	"BBDBB"
]

N = len(dataset)
for i in range(N):
	for j in range(i+1, N):
		_cmp = ""
		for k in range(len(dataset[0])):
			if dataset[i][k] == dataset[j][k]:
				_cmp += dataset[i][k]
			else:
				_cmp += "*"
		if len(list(set(_cmp))) == 1 and _cmp[0] == "*":
			continue
		result.setdefault(_cmp, 0)
		result[_cmp] += 1

_tmp = result
for k, v in sorted(result.items(), key=lambda x:x[1], reverse=True):
	_cnt = 0
	for i in range(len(k)):
		if k[i] == "*":
			continue
		_cnt += 1
	_tmp[k] *= 6 ** (_cnt - 1)
result = _tmp

print "SCORE: "
for k, v in sorted(result.items(), key=lambda x:x[1], reverse=True):
	print k, v
print

total = {}
print "DATASET: "
for d in dataset:
	_total = 0
	for k in result.keys():
		_all = 0
		_cnt = 0
		for i in range(len(dataset[0])):
			if k[i] == "*":
				continue
			_all += 1
			if d[i] == k[i]:
				_cnt += 1
		if _all == _cnt:
			_total += result[k]
	total.setdefault(d, 0)
	total[d] = _total

for k, v in sorted(total.items(), key=lambda x:x[1], reverse=True):
	print k, v

