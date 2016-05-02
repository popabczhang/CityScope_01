od = open('OD_160330.csv','r')
import re

l = []
#Preprocess into list
index = 0
for line in od:
	if index == 0:
		pass
	else:
		l1 = line.strip('\n')
		l1 = l1.strip('\r')
		l1 = l1.split(',')
		tupver = (float(l1[0]),float(l1[1]))
		l.append(tupver)
	index += 1
#Take off the first line
print l

def coordify(coord):
    l1 = coord.split(',')
    tupver = (float(l1[0]),float(l1[1]))
    return tupver

print coordify('1289.1814,1381.119,0.0')

pevnums = input('Enter# PEVs:')
print "hi"
print pevnums