#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import cv2
import numpy as np

from PIL import Image

class AKAZE:
	
	def __init__(self):
		self.handle = cv2.AKAZE_create()
		self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)

	def feature(self, path):
		img  = cv2.imread(path)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		return self.handle.detectAndCompute(gray, None)

	def compare_with_file(self, path, fe, limit_d):
		r = set()
		(kp, des) = self.feature(path)
		matches = self.bf.knnMatch(des, fe, k=2)
		for mm, nn in matches:
			if mm.distance < limit_d * nn.distance:
				#print mm.imgIdx, mm.queryIdx, mm.trainIdx
				r.add(mm.trainIdx)
		return list(r)

def main(path):
	dess = []
	akaze = AKAZE()
	featureIdx = 0
	for name in sorted(os.listdir(path)):
		if name.find(".jpg") == -1:
			continue
		(kp, des) = akaze.feature(path + name)
		dess.append(des)
		featureIdx += len(des)
	# --
	contrib  = [ 0 for i in range(featureIdx) ]
	imageIdx = 0
	for name in sorted(os.listdir(path)):
		if name.find(".jpg") == -1:
			continue
		_tmp_dess = []
		_idx, _sz = (0, 0)
		for i in range(len(dess)):
			if i == imageIdx:
				_idx = len(_tmp_dess)
				_sz  = len(dess[i])
				continue
			for d in dess[i]:
				_tmp_dess.append(d)
		_tmp_dess = np.array(_tmp_dess)
		r = akaze.compare_with_file(path + name, _tmp_dess, 0.9)
		for i in range(len(r)):
			if _idx <= r[i]:
				r[i] += _sz
			contrib[r[i]] += 1
		imageIdx += 1
	# --
	featureIdx = 0
	true_dess = []
	for a in dess:
		for d in a:
			if contrib[featureIdx] != 0:
				true_dess.append(d)
			featureIdx += 1
	true_dess = np.array(true_dess)
	# --
	_mmin = None
	for name in sorted(os.listdir(path)):
		if name.find(".jpg") == -1:
			continue
		r = akaze.compare_with_file(path + name, true_dess, 0.1)
		print len(r), name
		if _mmin == None or len(r) < len(_mmin):
			_mmin = r
	true_dess2 = []
	for i in range(len(true_dess)):
		if i in _mmin:
			continue
		true_dess2.append(true_dess[i])
	# --
	print "--"
	true_dess2 = np.array(true_dess2)
	for name in sorted(os.listdir(path)):
		if name.find(".jpg") == -1:
			continue
		r = akaze.compare_with_file(path + name, true_dess2, 0.1)
		print len(r), name

if __name__ == '__main__':
	main(sys.argv[1])

