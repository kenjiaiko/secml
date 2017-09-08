#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
import matplotlib
matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram

def main(readfile):
	X = np.loadtxt(readfile)
	r = linkage(pdist((X)))
	print r
	dendrogram(r)
	plt.savefig("output.png")
	#plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "python this.py <readfile>"
		sys.exit(1)
	readfile = sys.argv[1]
	main(readfile)

