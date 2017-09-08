#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
import matplotlib
matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

import gm

def main(filename):
	X = np.loadtxt(filename)
	model = gm.GaussianMixture(3)
	model.fit(X, iter_max=100)
	labels = model.classify(X)
	colors= ["red", "blue", "green"]
	plt.scatter(X[:, 0], X[:, 1], c=[colors[int(label)] for label in labels], s=5)
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	plt.savefig("output.png")
	#plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "python this.py <filepath>"
		sys.exit(1)
	filename = sys.argv[1]
	main(filename)

