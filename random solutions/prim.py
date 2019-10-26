class graph:
    def __init__(self, nodes, edges, e):
        self.nodes = nodes
        self.edges = edges
        self.graph = [[0]*(self.nodes) for _ in range(self.nodes)]
        self.e = e
        
    def addedge(self):
        
        for i in range(len(self.e)):
            u,v,w = self.e[i][0], self.e[i][1], self.e[i][2]
            self.graph[u-1][v-1]=w
            self.graph[v-1][u-1]=w
    def getedge(self):
        return self.graph
  

# Complete the prims function below.
def prims(n, edges, start):
    if n==0:
        return 0
    if n==1:
        return edges[2]
    MST = []
    notMST = set()
    gph = graph(n, len(edges), edges)
    gph.addedge()
    notMST.add(start)
    while len(notMST)!=n:
        cross = set()
        for m in notMST:
            for k in range(n):
                new = gph.getedge()
                if k not in notMST and new[m][k] != 0:
                    cross.add((m,k))
        g = gph.getedge()
        print("g",g)
        edge = sorted(cross, key=lambda e:g[e[0]][e[1]])[0]
        print("edge ",edge)
        MST.append(edge)
        print("MST ", MST)
        notMST.add(edge[1])
        print("notmst ", notMST)
    gp = gph.getedge()
    weights= []
    for (a,b) in MST:
        weights.append(gp[a][b])
    #print(sum(weights))
    return sum(weights)