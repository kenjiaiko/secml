#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
#import matplotlib
#matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

import sc
import li
import gm

def distance(a, b):
	return np.linalg.norm(np.array(a) - np.array(b))

def main(readfile):
	X = np.loadtxt(readfile)
	centers = sc.search_center(X, 10, 0.5, 0.1, distance, True)
	labels = [ "blue" for i in range(len(X)) ]
	C = np.zeros((0, 2))
	for c in centers:
		labels[c[0]] = "red"
		C = np.r_[C, np.array(X[c[0]]).reshape(1,-1)]
	r = li.get_num_of_clusters(C, False)
	model = gm.GaussianMixture(len(r))
	model.fit(C, iter_max=100)
	labels = model.classify(C)
	plt.scatter(X[:, 0], X[:, 1], s=5)
	x_test, y_test = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
	probs = model.predict_proba(np.array([x_test, y_test]).reshape(2, -1).transpose())
	plt.contour(x_test, y_test, probs.reshape(100, 100), levels=[i for i in np.arange(0.0, 1.0, 0.01)])
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	#plt.savefig("output.png")
	plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "python this.py <readfile>"
		sys.exit(1)
	readfile = sys.argv[1]
	main(readfile)

