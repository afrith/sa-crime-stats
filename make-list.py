#!/usr/bin/env python

# Copyright (c) 2014 Adrian Frith <adrian@adrianfrith.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import csv, re

outfile = open('crime-stats.csv', 'w')
writer = csv.writer(outfile)

writer.writerow(('station', 'province', 'crime', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'))

for prov in ('EC', 'FS', 'GP', 'KZN', 'LI', 'MP', 'NC', 'NW', 'WC'):
    station = None
    rex = re.compile('Crime in\s*(.*)\s*\(' + prov)
    rdr = csv.reader(open('source/' + prov.lower() + '.csv'))
    for line in rdr:
        mo = rex.match(line[0])
        if mo:
            station = mo.group(1).strip()
            continue

        if line[1].isdigit() and station != None:
            crime = line[0]
            stats = list(map(int, line[1:]))
            writer.writerow([station, prov, crime] + stats)

outfile.close()
