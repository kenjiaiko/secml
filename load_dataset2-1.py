#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
import matplotlib
matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

import sc

def distance(a, b):
	return np.linalg.norm(np.array(a) - np.array(b))

def main(readfile, writefile):
	X = np.loadtxt(readfile)
	centers = sc.search_center(X, 10, 0.5, 0.1, distance, True)
	labels = [ "blue" for i in range(len(X)) ]
	C = np.zeros((0, 2))
	for c in centers:
		labels[c[0]] = "red"
		C = np.r_[C, np.array(X[c[0]]).reshape(1,-1)]
	np.savetxt(writefile, C)
	plt.scatter(X[:, 0], X[:, 1], c=[label for label in labels], s=5)
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	plt.savefig("output.png")
	#plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print "python this.py <readfile> <writefile>"
		sys.exit(1)
	readfile = sys.argv[1]
	writefile= sys.argv[2]
	main(readfile, writefile)

