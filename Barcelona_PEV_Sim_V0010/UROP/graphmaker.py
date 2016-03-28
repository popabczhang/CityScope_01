f = open('sample.txt', 'r')
# with open('sample.txt', 'r') as reader:
#   f = reader.read()
# reader.closed

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
    l.append(line.strip('\n'))

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
                print "manual end" + l[i-1]
                g[s].append(l[i-1])
            lcount = 0

        #Check for start of line/code
        elif lcount == 0:
            s = l[i]
            if s not in g.keys():
                g[s] = []
            lcount += 1
            print 'begin' + s

        #Check for end of segments
        elif lcount == length:
            print "natural end" + l[i]
            g[s].append(l[i])
            s = l[i]
            if s not in g.keys():
                g[s] = []
            lcount = 1

        else:
            lcount += 1

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
        graph = self.g
        start = self.pickup
        goal = self.drop
        try:
            return next(self.paths())
        except StopIteration:
            return None

cab = PEV(g, '0', '1','17',False)

path = cab.find()
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

