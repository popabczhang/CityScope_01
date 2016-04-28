f = open('RD_160420.txt', 'r')
od = open('OD_160420_dense.csv','r')
import re
import csv
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

speed = 3

pevnum = 60

log = []

def set_available():
    global available    # Needed to modify global copy of globvar
    available = 3

set_available()
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

def coordify(coord):
    l1 = coord.split(',')
    tupver = (float(l1[0]),float(l1[1]))
    return tupver

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
                g[s].append(coordify(l[i-1]))
            lcount = 0
        elif l[i] == "<null>":
            print "end" 
        #Check for start of line/code
        elif lcount == 0:
            s = coordify(l[i])
            if s not in g.keys():
                g[s] = []
            lcount += 1
            # print 'begin' + s

        #Check for end of segments
        elif lcount == length:
            # print "natural end" + l[i]
            g[s].append(coordify(l[i]))
            s = coordify(l[i])
            if s not in g.keys():
                g[s] = []
            lcount = 1

        else:
            lcount += 1
# print g

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
        else:
            if self.stat == 'f':
                #Check LOCATION at BEGINNING.  
                if self.current == self.pickup:
                    print "change from f to d" + self.stat
                    #find new path
                    self.stat = 'd'
                    print self.stat
                    self.p = self.find(self.current,self.drop)
                    # print self.p
                    print "self.drop "
                    print self.drop
                else:
                    self.current = self.p.pop(0)
        #d for dropping off
            elif self.stat == 'd':
                if self.current == self.drop:
                    print "change from d to e" + self.stat
                    self.stat = 'e'
                    print self.stat
                else:
                    # print "dropoff path"
                    # print self.p
                    # print "intended dropoff"
                    # print self.drop
                    # print self.current
                    # print "d loop???"
                    self.current = self.p.pop(0)
            else:
                print "update error status"
        #update location:  debug log: check what to do if cab finds the target location
        #No coincidence 
        # if self.stat != 'e':
        #     if self.current == self.drop:
        #         print "change from d to e" + self.stat
        #         self.stat = 'e'
        #         # available += 1
        #     elif self.current == self.pickup:
        #         print "change from f to d"
        #         #find new path
        #         self.stat = 'd'

    def find(self, startfind,goalfind):
        graph = self.g
        start = startfind
        goal = goalfind
        try:
            return next(self.paths(start,goal))
        except StopIteration:
            return None
    #return list of paths
        
#Controller code

#Matplotlib

#trip record:
#1) basic trip data, request time, pickup/dropoff point, total pev, available pev #, nearest pev (use Null/N/a/None for no available pevs), missed/not, waiting time, time of pickup, time of dropoff, delivery time
#2) PEV table 
#Examples of uses:  Missed trips throughout the day, Distribution of PEV trips throughout the day


#Priorities/what to do next:
#refine process, graph #PEVs vs dropped trips, optimize.  Get rid of skipped requests.
#Implement waitlist = > 1st available PEV => Pick up the one who waited the longest
#Total travel time <=> efficiency
#

#Initialize list of cabs:
#figure out how to make this automated

def tupify(x,y):
    # print "tupify loop"
    # print x
    # print y
    tup = (float(x),float(y))
    return tup

PEVlist = []
for i in range(0, pevnum):
    p = tupify('1404.534','1012.322')
    d = tupify('1390.86','1013.399')
    c = tupify('1229.897','1374.172')
    cab1 = PEV([],g,c, p, d,'e')
    PEVlist.append(cab1)

#Initialize time in minutes
time = 0

# #initialize list of unpicked trips
# demand = []

#log "trip record"
#Total PEV: Request, pickup/dropoff

trip = []
#Preprocess into list
for line in od:
    l1 = line.strip('\n')
    l1 = l1.strip('\r')
    l1 = l1.split(',')
    trip.append(l1)

#Take off the first line
trip.pop(0)
# print trip

missed = 0
errorpath = 0
wait = []

for i in trip:
    log.append([])
    print "in loop"
    print i[0]
    #some sort of index i that represents a LIST in the table once I figure out the proper way to read this
    while time < int(i[0]):
        for cab in PEVlist:
            # if cab.stat == 'e':
            #     if len(demand) != 0:
            #         cab.stat = 'f'
            #         #modify this indicator once you figure out how to split stuff
            #         passenger = demand.pop(0)
            #         cab.pickup = tupify(passenger[1], passenger[2])
            #         cab.dropoff = tupify(passenger[3], passenger[4])
            #         cab.path = cab.find(cab.current, cab.pickup)
            # else:
            #     #Think about if this should be "else" or the cab should also update
            cab.update()
        time += 1
        
    if time == int(i[0]):
        log[len(log)-1].append(int(i[0]))
        # print "reached"
        pickupswitch = False
        #loop through list of cabs to find empty cabs
        for cab in PEVlist:
            if cab.stat == 'e':
                cab.pickup = tupify(i[1],float(i[2]))
                print cab.pickup
                cab.dropoff = tupify(i[3],float(i[4]))
                print cab.dropoff
                #modify this indicator once you figure out how to split stuff
                if cab.find(cab.current, cab.pickup) != None:
                    log[len(log)-1].append(cab.pickup)
                    log[len(log)-1].append(cab.dropoff)
                    log[len(log)-1].append(PEVlist.index(cab))
                    #Logging available PEVs BEFORE they're taken
                    # log[len(log)-1].append(available)
                    cab.stat = 'f'
                    available -= 1
                    #modify this indicator once you figure out how to split stuff
                    cab.p = cab.find(cab.current, cab.pickup)
                    pickupswitch = True
                    log[len(log)-1].append(True)
                    print "picked up by" + str(PEVlist.index(cab))
                    #check to make sure this is a list
                    print "Cab path"
                    print cab.p
                    waittime = len(cab.p)/speed
                    # waittuple = (int(i[0]),waittime)
                    wait.append(waittime)
                    log[len(log)-1].append(waittime)
                    break
                    # log[len(log)-1].append(available)
                    log[len(log)-1].append(False)
                    log[len(log)-1].append(None)
        #if all cabs are full, at to demand list
        if pickupswitch == False:
            # demand.append(i)
            log[len(log)-1].append(None)
            log[len(log)-1].append(None)
            log[len(log)-1].append(None)
            #Logging available PEVs BEFORE they're taken
            # log[len(log)-1].append(available)
            log[len(log)-1].append(False)
            log[len(log)-1].append(None)
            missed += 1
            print "didn't pick up"
    else:
        #somehow irregularities in the simulation
        print "error simulator"
print log

#write log into csv
with open('log.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in log]

print wait
#now to find average wait time
sumwait = 0
avewait = 0

for i in wait:
    sumwait += i
avewait = sumwait/len(wait)
print "average wait time" 
print avewait
print "missed trips"
print missed
print "trips with no path"
print errorpath
