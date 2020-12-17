import sys

class Vertex():
    """
        Creating class for Vertices including information of
        finish time, discover time, out direction degrees
        and Adjacent Verticess.
    """
    def __init__(self):
        self.f = 0
        self.d = 0
        self.outDeg = 0
        self.outList = []

class Graph():
    """
        Creating class for Graph
    """
    def __init__(self):
        """
            Graph needs information of numbers of Vertices
            numbers of Edges and individual Vertices
        """
        self.NofV = 0
        self.NofE = 0
        self.vertices = []

    def initGraph(self, numV, numE):
        """
            initializing Graph
            we need to convert numV and numE, since they are in string initially
            and if we have invalid numbers of V and E we returns False because
            we cannot create one at all
            then if we successfully create graph, returning True
        """
        numV = int(numV)
        numE = int(numE)
        if numV < 1:
            print("Invalid Number of Nodes")
            ret = False
        elif numE < numV - 1:
            print("Invalid Number of Edges")
            ret = False
        
        self.NofV = numV
        self.NofE = numE
        for i in range(numV):
            self.vertices.append(Vertex())
            for j in range(numV):
                self.vertices[i].outList.append(-1)
        ret = True
        
        return ret

    def makeEdge(self, i, j):
        """
            Create Edge
            If we fail to make one then return false
            or we return true for success
        """
        i = int(i)
        j = int(j)
        
        i -= 1
        j -= 1
        if i != j and i < j:
            self.vertices[i].outList[self.vertices[i].outDeg] = j
            self.vertices[i].outDeg += 1
            ret = True
        else:
            ret = False
        return ret

class TopologicalSort():
    """
        using DFS concept with recursion
        search deep first and store Topologically
    """
    def __init__(self, g):
        self.graph = g
        self.numPath = 0
        self.SPathLength = self.graph.NofE
        self.LPathLength = 0

    def traverseGraph(self):
        self.travelNode(0, 0)

    def travelNode(self, node, length):
        """
            recusion will make this code search until it search all the nodes
            As we searching through, add number of path for return value
            if input length is shorter or larger then it will automatically assigned to
            either Short Path Length or Long Path Length.
        """
        if node == self.graph.NofV - 1:
            self.numPath += 1
            
            if length < self.SPathLength:
                self.SPathLength = length

            if length > self.LPathLength:
                self.LPathLength = length
                
        elif node != -1:
            length += 1
            for i in range(self.graph.vertices[node].outDeg):
                self.travelNode(self.graph.vertices[node].outList[i], length)

def main():
    
    mainGraph = Graph()
    fp = sys.stdin.readlines()
    N = int(fp[0])
    M = int(fp[1])
    
    mainGraph.initGraph(N, M)
    
    """python has recursion limit"""
    if mainGraph.NofV > sys.getrecursionlimit():
        sys.setrecursionlimit(mainGraph.NofV + 3)
    
    for i in range(mainGraph.NofE):
        u, v = fp[i + 2].split()[0], fp[i + 2].split()[1]
        connect = mainGraph.makeEdge(u, v)
        if not connect:
            break

    topolog = TopologicalSort(mainGraph)
    topolog.traverseGraph()
    
    print "Total number of paths: ", topolog.numPath
    print "Shortest path length: ", topolog.SPathLength
    print "Longest path length: ", topolog.LPathLength

if __name__ == '__main__':
    main()
