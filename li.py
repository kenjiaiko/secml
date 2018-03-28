#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
#import matplotlib
#matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram

def get_num_of_clusters(X, debug):
	r = linkage(pdist((X)))
	if debug == True:
		dendrogram(r)
		plt.show()
	g = {}
	N = len(X)
	for i in range(N):
		g.setdefault(i, [i])
	for v in r:
		g.setdefault(N, [])
		for w in g[v[0]]:
			g[N].append(w)
		for w in g[v[1]]:
			g[N].append(w)
		N += 1
	before = -1.0
	count  = 0
	_mmax  = 0.0
	for v in sorted(r, key=lambda x:x[2], reverse=True):
		if 0.0 < before:
			if _mmax < (before - v[2]):
				_mmax = (before - v[2])
				count += 1
		before = v[2]
	N = len(g.keys()) - 1
	c = [ g[N] ]
	for i in range(count):
		d = []
		_next = g[N - (i + 1)]
		for v in c:
			if _next[0] in v:
				d.append(_next)
				d.append(list( set(v) - set(_next) ))
			else:
				d.append(v)
		c = d
	return c

if __name__ == '__main__':
	readfile = sys.argv[1]
	r = get_num_of_clusters(np.loadtxt(readfile), True)
	print "num of clusters: " + str(len(r))
	print r

