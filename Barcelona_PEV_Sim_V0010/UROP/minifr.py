od = open('OD_160330.csv','r')
import re

l = []
#Preprocess into list
for line in od:
    l1 = line.strip('\n')
    l1 = l1.strip('\r')
    l1 = l1.split(',')
    l.append(l1)
print l