#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
#import matplotlib
#matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

import gm

def main(filename1, filename2, num):
	X = np.loadtxt(filename2)
	Y = np.loadtxt(filename1)
	model = gm.GaussianMixture(num)
	model.fit(X, iter_max=100)
	labels = model.classify(X)
	plt.scatter(Y[:, 0], Y[:, 1], s=5)
	plt.scatter(X[:, 0], X[:, 1], s=5)
	x_test, y_test = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
	probs = model.predict_proba(np.array([x_test, y_test]).reshape(2, -1).transpose())
	plt.contour(x_test, y_test, probs.reshape(100, 100), levels=[i for i in np.arange(0.0, 1.0, 0.01)])
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	#plt.savefig("output.png")
	plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print "python this.py <original filepath> <filepath> <num of clusters>"
		sys.exit(1)
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	num = int(sys.argv[3])
	main(filename1, filename2, num)

