class graph:
    def __init__(self, nodes):
        self.nodes = nodes
        #self.edges = edges
        self.graph = []
        #print("total nodes :", nodes)

    def addedge(self, u, v,w):
        self.graph.append([u,v,w])
        #print("added edge: ", [u,v,w])

    def getedge(self, i):
        #print("Getting edge : ", self.graph[i])
        return self.graph[i]

    def sortbyweight(self):
        self.graph = sorted(self.graph, key = lambda item:item[2])

    def find(self,parent, i):
        if parent[i-1]==-1:
            return i
        return self.find(parent, parent[i-1])

    def union(self, parent, rank, i, j):
        iroot = self.find(parent, i)
        jroot = self.find(parent, j)

        if rank[iroot]>rank[jroot]:
            parent[jroot]=iroot
        elif rank[jroot]>rank[iroot]:
            parent[iroot] = jroot
        else:
            parent[jroot]=iroot
            rank[iroot] +=1


def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    if g_nodes==0:
        return 0 
    if g_nodes==1:
        return g_weight
    grap = graph(g_nodes)
    for i in range(len(g_from)):
        grap.addedge(g_from[i], g_to[i], g_weight[i])

    mst = []
    b = 0 #for sorted edges by weight
    c = 0 #for mst result
    grap.sortbyweight() 
    parent = [-1]*g_nodes
    rank = [0]*g_nodes
    
    while c<g_nodes-1:
        uvw = grap.getedge(b)
        b+=1
        x = grap.find(parent, uvw[0])
        y = grap.find(parent, uvw[1])
        if x!=y:
            c+=1
            mst.append(uvw)
            grap.union(parent, rank, x,y)
            #print("MST so far: ",mst)
    weights = [ m[2] for m in mst]
    w = sum(weights)
    print(w)
