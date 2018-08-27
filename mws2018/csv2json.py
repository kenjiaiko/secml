#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import csv
import sys

csvfile = sys.argv[1]
data = {}
reader = csv.reader(open(csvfile))
next(reader)
for row in reader:
	day = row[0][:6]
	data.setdefault(day, [])
	data[day].append([row[4], row[6]])
open(csvfile + ".json", "w").write(json.dumps(data, indent=4))

