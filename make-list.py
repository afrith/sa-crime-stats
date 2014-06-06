#!/usr/bin/env python
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
