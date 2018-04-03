#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json

import suffixtree

if __name__ == "__main__":
	dataset = json.loads(open(sys.argv[1]).read())["dataset"]
	N = len(dataset)
	original = {}
	for d in dataset:
		original.setdefault(d, 0)
		original[d] += 1
	h = suffixtree.ST(original)
	dd = h.print_tree(h.get(), 3)
	for k, v in sorted(dd.items(), key=lambda x:len(x[1]), reverse=True):
		if len(v) < 2:
			continue
		print k + " was included in " + str(len(v)) + " data."

