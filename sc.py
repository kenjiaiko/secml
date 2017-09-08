#!/usr/bin/env python
# coding: utf-8

import sys

def distances(dataset, func):
	di = {}
	for i in range(len(dataset[0])):
		di.setdefault(i, {})
		a = []
		for k in range(len(dataset)):
			a.append(dataset[k][i])
		for j in range(len(dataset[0])):
			di[i].setdefault(j, 0.0)
			if j < (i+1):
				di[i][j] = di[j][i]
			else:
				b = []
				for k in range(len(dataset)):
					b.append(dataset[k][j])
				di[i][j] = func(a, b)
	return di

def neighborhood(dist, N):
	rank = {}
	for k in dist.keys():
		rank.setdefault(k, 0.0)
		total = 0.0
		count = 1
		for (i, v) in sorted(dist[k].items(), key=lambda x:x[1]):
			if N < count:
				break
			total += dist[k][i]
			count += 1
		rank[k] = total / float(count - 1)
	return rank

def original_index(k, tb):
	for i in range(len(tb)):
		if tb[i] == True:
			k += 1
		if k == i:
			break
	return k

def format(dataset):
	result = []
	for i in range(len(dataset[0])):
		d = []
		for j in range(len(dataset)):
			d.append(dataset[j][i])
		result.append(d)
	return result

def search_center(dataset, num_of_neighbors, threshold, delete_distance, func, format_flag=False):
	if format_flag == True:
		dataset = format(dataset)
	centers = []
	tb = [ False for i in range(len(dataset[0])) ]
	saved_dataset = dataset
	while 1:
		dist = distances(dataset, func)
		rank = neighborhood(dist, num_of_neighbors)
		(idx, dis) = sorted(rank.items(), key=lambda x:x[1])[0]
		if threshold < dis:
			break
		orig_idx = original_index(idx, tb)
		centerN1 = [ orig_idx ]
		for i in range(len(saved_dataset)):
			centerN1.append(saved_dataset[i][orig_idx])
		centers.append(centerN1)
		delete______idx = [ idx ]
		delete_orig_idx = [ orig_idx ]
		for i in dist[idx].keys():
			if dist[idx][i] < delete_distance:
				delete_orig_idx.append(original_index(i, tb))
				delete______idx.append(i)
		for idx in delete_orig_idx:
			tb[idx] = True
		dataset = []
		for i in range(len(saved_dataset)): #num of dims
			one = []
			for j in range(len(saved_dataset[i])): #num of dataset
				if tb[j] == True:
					continue
				one.append(saved_dataset[i][j])
			dataset.append(one)
	return centers

if __name__ == '__main__':
	pass

