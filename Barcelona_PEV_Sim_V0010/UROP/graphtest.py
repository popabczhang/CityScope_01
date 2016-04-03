f = open('RD_CRV_PTS_151231.txt', 'r')
od = open('OD_160330.tsv','r')
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
length = 4

#Put in object
    #current loc
    #Pickup loc
    #drop off loc
    #Status empty/not

#Function
    #Add/remove/run
    #run: if assigned (wandering)
    #Pickup/no pickup/something in it/not

#Questions to ask:
#How should we treat edge cases? I.e. Node of 1 point (is it even important to treat these)
#Remove empty entries

s= 0
l = []
#Preprocess into list
for line in f:
    l1 = line.strip('\n')
    l1 = l1.strip('\r')
    l.append(l1)

#function for checking tolerance
# def check(start,end):
#     if start()

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
print g

class PEV:
    def __init__(self, graph, current_location, pickup_location, dropoff, status):
        self.g = graph
        self.current = current_location
        self.pickup = pickup_location
        self.drop = dropoff
        self.stat = status

    #Start code for BST
    #Refer to http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    def paths(self):
        graph = self.g
        start = self.pickup
        goal = self.drop
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            #Check for edge cases on code below:
            for next in set(graph[vertex]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def find(self):
        try:
            return next(self.paths())
        except StopIteration:
            return None

cab = PEV(g,'0', '1445.558018,1009.093722,0.0', '1213.157954,1209.565353,0.0', 'e')

r = cab.find()
print r
