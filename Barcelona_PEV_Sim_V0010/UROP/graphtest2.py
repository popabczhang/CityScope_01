f = open('RD_PTS_160401.txt', 'r')
od = open('OD_160330.tsv','r')
import re
# f = open('RD_CRV_PTS_151231.txt', 'r')
# with open('sample.txt', 'r') as reader:
#   f = reader.read()
# reader.closed

import time

# dictionary format: {start: [(end1)],[(end2)]}

#variable names
#l = list
#g = graph
#s = start
#i = index

g = {}

lcount = -1

#length of segment
length = 1

s= 0
l = []
#Preprocess into list
for line in f:
    l1 = line.strip('\n')
    l1 = l1.strip('\r')
    l.append(l1)

for i in range(0,len(l)):
    # print line
    # if line != '\n':
        #Check for beginnings of nodes
    if l[i] != 'start':
        #first = file.nextline()

        #check for beginning of road
        if l[i] == 'one way':
            lcount = 0

        #Check for manual end of road
        elif l[i] == 'end':
            if lcount > 1:
                # print "manual end" + l[i-1]
                g[s].append(l[i-1])
            lcount = 0

        #Check for start of line/code
        elif lcount == 0:
            s = l[i]
            if s not in g.keys():
                g[s] = []
            lcount += 1
            # print 'begin' + s

        #Check for end of segments
        elif lcount == length:
            # print "natural end" + l[i]
            g[s].append(l[i])
            s = l[i]
            if s not in g.keys():
                g[s] = []
            lcount = 1

        else:
            lcount += 1

class PEV:
    def __init__(self, path, graph, current_location, pickup_location, dropoff, status):
        self.g = graph
        self.current = current_location
        self.pickup = pickup_location
        self.drop = dropoff
        self.stat = status
        self.p = path

    #Start code for BST
    #Refer to http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    def paths(self,s,g):
        graph = self.g
        start = s
        goal = g
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            #Check for edge cases on code below:
            for next in set(graph[vertex]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def update(self):
        #e for empty
        if self.stat == 'e':
            pass
        #f for find
        elif self.stat == 'f':
            self.current = self.p.pop(0)
        #d for dropping off
        elif self.stat == 'd':
            self.current = self.p.pop(0)
        else:
            print "update error status"
        #update location:  debug log: check what to do if cab finds the target location
        if self.current == self.drop:
            print "change from d to e" + self.stat
            self.stat = 'e'
        elif self.current == self.pickup:
            print "change from f to d"
            self.stat = 'd'


    def find(self):
        graph = self.g
        start = self.pickup
        goal = self.drop
        try:
            return next(self.paths(start,goal))
        except StopIteration:
            return None
    #return list of paths

cab1 = PEV([],g, '0', '1445.558,1009.0937,0.0','1229.897,1374.1716,0.0','e')
print cab1.find()