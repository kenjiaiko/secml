#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

class ST:

	def __init__(self, strings, lastword="\x00"):
		self.root = { None: 0 }
		self.lastword = lastword
		self.gstack = []
		self.alldata= {}
		for ss in strings.keys():
			ss += lastword
			for i in range(len(ss)):
				node = self.root
				for c in ss[i:]:
					node.setdefault(c, { None: 0 })
					node[c][None] += strings[ss[:-1]]
					node = node[c]
	
	def get(self):
		return self.root
	
	def print_tree(self, tree, num):
		for k in tree.keys():
			if k == None:
				continue
			if len(self.gstack) == num:
				s = ""
				for c in self.gstack:
					s += c
				self.alldata.setdefault(s, 0)
				self.alldata[s] += tree[k][None]
				continue
			self.gstack.append(k)
			self.print_tree(tree[k], num)
			self.gstack.pop()
		return self.alldata

if __name__ == "__main__":
	pass

