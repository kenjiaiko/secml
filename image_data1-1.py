#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import math
import numpy as np
import cv2 as cv

from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram

from matplotlib import pyplot as plt

def check_images(imgfile1, imgfile2, mmin_match_count, dist):
	img1 = cv.imread(imgfile1, 0)
	img2 = cv.imread(imgfile2, 0)
	height, width = img1.shape[:2]
	# --
	# Initiate SIFT detector
	sift = cv.xfeatures2d.SIFT_create()
	kp1, des1 = sift.detectAndCompute(img1, None)
	kp2, des2 = sift.detectAndCompute(img2, None)
	# --
	FLANN_INDEX_KDTREE = 1
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)
	flann = cv.FlannBasedMatcher(index_params, search_params)
	matches = flann.knnMatch(des1, des2, k=2)
	# --
	# store all the good matches as per Lowe's ratio test.
	good = []
	for m, n in matches:
		if m.distance < dist * n.distance:
			good.append(m)
	if len(good) < mmin_match_count:
		return None
	src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1, 1, 2)
	dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1, 1, 2)
	M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
	matchesMask = mask.ravel().tolist()
	accepted= []
	for i in range(len(matchesMask)):
		if matchesMask[i] != 1:
			continue
		accepted.append(kp1[good[i].queryIdx].pt)
	return list(set(accepted))

def clustering(X, threshold):
	if len(X) < 10:
		return None
	r = linkage(pdist((X)))
	#dendrogram(r)
	#plt.show()
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

def main(imgfile1x, imgfile2x, saved_path):
	data = check_images(imgfile1x, imgfile2x, 10, 0.7)
	if data == None:
		return None
	m_data = []
	for v in data:
		m_data.append( (v[0] / float(100), v[1] / float(100)) )
	label = clustering(m_data, 0.5)
	l_data= []
	for a in label:
		one = []
		for v in a:
			one.append( data[v] )
		l_data.append(one)
	_no = 1
	for D in l_data:
		_mmin_x = 99999.9
		_mmin_y = 99999.9
		_mmax_x = -1.0
		_mmax_y = -1.0
		for v in D:
			if v[0] < _mmin_x:
				_mmin_x = v[0]
			if v[1] < _mmin_y:
				_mmin_y = v[1]
			if _mmax_x < v[0]:
				_mmax_x = v[0]
			if _mmax_y < v[1]:
				_mmax_y = v[1]
		if (_mmax_x - _mmin_x) < 1.0 or (_mmax_y - _mmin_y) < 1.0:
			continue
		filename = str(_no) + ".jpg"
		img1 = cv.imread(imgfile1x, 0)
		cv.imwrite(saved_path + filename, img1[int(_mmin_y):int(_mmax_y), int(_mmin_x):int(_mmax_x)])
		_no += 1

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], "saved/")

