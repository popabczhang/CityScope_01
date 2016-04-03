f = open('sample.txt', 'r')
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

start_time = time.time()

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
    def paths(s,g):
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


    def find(startfind,goalfind):
        graph = self.g
        start = startfind
        goal = goalfind
        try:
            return next(self.paths(start,goal))
        except StopIteration:
            return None
    #return list of paths
        
#Controller code

#Initialize list of cabs:
PEVlist = []
cab1 = PEV([],g, '0', '1','16','e')
PEVlist.append(cab1)
cab2 = PEV([],g, '0', '1','16','e')
PEVlist.append(cab2)
cab3 = PEV([],g, '0', '1','16','e')
PEVlist.append(cab3)

#Initialize time in minutes
time = 0

#initialize list of unpicked trips
demand = []

def tupify(x,y):
    tup = (x,y)
    return tup

for i in od:
    #some sort of index i that represents a LIST in the table once I figure out the proper way to read this
    while time < i[0]:
        for cab in PEVlist:
            if cab.status == 'e':
                if len(demand) != 0:
                    cab.status = 'f'
                    #modify this indicator once you figure out how to split stuff
                    passenger = demand.pop(0)
                    cab.pickup = tupify(passenger[1], passenger[2])
                    cab.dropoff = tupify(passenger[3], passenger[4])
                    cab.path = cab.find(cab.current, cab.pickup)
            else:
                #Think about if this should be "else" or the cab should also update
                cab.update()
        time += 1

    if time == i[0]:
        pickupswitch = False
        #loop through list of cabs to find empty cabs
        for cab in PEVlist:
            if cab.status == 'e':
                cab.status = 'f'
                #modify this indicator once you figure out how to split stuff
                cab.pickup = tupify(i[1],i[2])
                cab.dropoff = tupify(i[3],i[4])
                cab.path = cab.find(cab.current, cab.pickup)
                pickupswitch = True
        #if all cabs are full, at to demand list
        if pickupswitch = False:
            demand.append(i)
    else:
        #somehow irregularities in the simulation
        return "error"


path = cab.find()
print("--- %s seconds ---" % (time.time() - start_time))
print path

    # if l[i] != 'start':
    #   #first = file.nextline()

    #   #check for beginning of road
    #   if l[i] == 'one way':
    #       lcount = 0

    #   #Check for manual end of road
    #   elif l[i] == 'end':
    #       if lcount > 1:
    #           print "manual end" + l[i-1]
    #           g[s].append(l[i-1])
    #       lcount = 0

    #   #Check for start of line/code
    #   elif lcount == 0:
    #       s = l[i]
    #       if s not in g.keys():
    #           g[s] = []
    #       lcount += 1
    #       print 'begin' + s

    #   #Check for end of segments
    #   elif lcount == length:
    #       print "natural end" + l[i]
    #       g[s].append(l[i])
    #       s = l[i]
    #       if s not in g.keys():
    #           g[s] = []
    #       lcount = 1

    #   else:
    #       lcount += 1
    # # elif line == 'end':
    # #     #g[first].append(lcount)
    # #     print lcount
    # # if line != 'one way\n' and lcount != -1:
    # #     lcount += 1
    # #     # if lcount == 1:
    # #     # s = line
    # #     # g[s] = []
    # # if lcount == 1:
    # #     g[s].append(line.strip('\n'))
    # #     s = line.strip('\n')
    # #     g[s] = []
    # #     lcount = 0


# def BFS(g,s,e):
#   #q = queue
#   #p = path
#   #v = visited

#   q = []
#   p = []
#   v = {}

#   if s == e:
#       return s
#   #populate the start of the q
#   for i in g[s]:
#       if i != e:
#           q.append(i)
#   while q:
#       c = q.pop(0)
#       if c == e:
#           return c
#       for i in g[c]:
#           q.append(i)
    

# l = BFS(g,0,"15")

# print l

# Dijkstra search algorithm
# def search(start, end, graph):
#   #ideally initiate q in heap
#   q = []
#   #path format: {start:(end, weight)}
#   path = {}
#   node = start
#   for node != end:

