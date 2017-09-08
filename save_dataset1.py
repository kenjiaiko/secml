#!/usr/bin/env python
# coding: utf-8

import numpy as np
# -- bash on Windows
#import matplotlib
#matplotlib.use('Agg')
# --
import matplotlib.pyplot as plt
import sys

def create_normal(sz, scale, c):
	return np.random.normal(size=sz, scale=scale) + np.array(c)

def dataset():
	d1 = create_normal((150, 2), 1.0, [5,  5])
	d2 = create_normal(( 50, 2), 0.5, [5, -5])
	d3 = create_normal((100, 2), 1.0, [-5, 5])
	return np.vstack((d1, d2, d3))

def main(filename):
	X = dataset()
	if filename != None:
		np.savetxt(filename, X)
	plt.scatter(X[:, 0], X[:, 1], c=["blue" for i in range(len(X))], s=5)
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	#plt.savefig("output.png")
	plt.show()

if __name__ == '__main__':
	filename = None
	if 1 < len(sys.argv):
		filename = sys.argv[1]
	main(filename)

