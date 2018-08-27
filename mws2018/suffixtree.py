#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

class ST:

	def __init__(self, lastword="\x00"):
		self.root = { None: 0 }
		self.lastword = lastword
		self.gstack = []
		self.gscore = []
		self.alldata= {}
		self.values = []
	
	def update(self, ss, value=1):
		root = { None: 0 }
		ss += self.lastword
		for i in range(len(ss)):
			node = root
			for c in ss[i:]:
				node.setdefault(c, { None: 0 })
				node[c][None] = value
				node = node[c]
		self.add(self.root, root)
	
	def add(self, a, b):
		for k in b.keys():
			if k == None:
				continue
			a.setdefault(k, { None: 0 })
			a[k][None] += b[k][None]
			self.add(a[k], b[k])
	
	def sub(self, a, b):
		for k in b.keys():
			if k == None:
				continue
			a.setdefault(k, { None: 0 })
			a[k][None] -= b[k][None]
			self.sub(a[k], b[k])
	
	def get(self):
		return self.root
	
	def score(self, s):
		_score = []
		s += self.lastword
		for i in range(len(s)):
			node = self.root
			for c in s[i:]:
				try:
					v = node[c][None]
					_score.append(v)
				except:
					break
				node = node[c]
			_score.append(0)
		return _score

	def print_tree(self, tree, strlen):
		for k in tree.keys():
			if k == None:
				continue
			if len(self.gstack) == strlen:
				s = ""
				for c in self.gstack:
					s += c
				if len(self.gscore) < 1:
					continue
				n = self.gscore[-1]
				self.alldata.setdefault(s, 0)
				self.alldata[s] = n
				continue
			self.gstack.append(k)
			self.gscore.append(tree[k][None])
			self.print_tree(tree[k], strlen)
			self.gscore.pop()
			self.gstack.pop()
		return self.alldata

def main():
	dataset = [
		"I am hello", "hello is me", "hello are you", "this is test"
	]
	h1 = ST()
	for ds in dataset:
		h1.update(ds)
	data = h1.print_tree(h1.get(), 5)
	print data
	(k, v) = sorted(data.items(), key=lambda x:x[1], reverse=True)[0]
	print k, v
	for d in dataset:
		print h1.score(d)

if __name__ == "__main__": 
	main()

