#https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/
def charRisk(char):
    #"S = a", "E = z"
    if char == "S":
        char = "a"
    if char == "E":
        char = "z"
    return ord(char)-96

def flatten(l):
    return [item for sublist in l for item in sublist]

class pathMap:
    def __init__(self, mapFile):
        with open(mapFile, 'r') as file:
            #exercise specific char to int mapping
            self.map = [[val for val in line.strip("\n")] for line in file]

        self.H = len(self.map)
        self.W = len(self.map[0])
        self.dist = {}

    def Dijkstra(self):
        #create graph, dists and visited
        graph = {}
        self.dist = {}
        visited = {}
        for i, row in enumerate(self.map):
            for j, val in enumerate(row):
                #list of infinite distances
                self.dist[(i,j)] = float("inf")
                visited[(i,j)] = False

                #day specific modification
                #swap S and E for part B
                if val == "E":
                    root = (i,j)
                    self.dist[(i, j)] = 0
                if val == "S":
                    goal = (i,j)

                graph[(i,j)]=[]
                #square neighbours; up = (+1, 0), down = (-1, 0), left = (0, -1), right = (0, +1)
                neighbours = [(i+di, j+dj) for di, dj in [(+1, 0), (-1, 0), (0, -1), (0, +1)] if (0 <= i+di <= self.H-1 and 0 <= j+dj <= self.W-1)]
                for neighbour in neighbours:
                    #day specific modification part A:
                    a, b = neighbour
                    #reverse this also to revers and E
                    if charRisk(self.map[a][b])-charRisk(val) <= -2:
                        #not reachable
                        continue
                    
                    #point, distance
                    graph[(i,j)].append([neighbour, 1])

        #ACTUAL DIJKSTRA
        for ind in range(len(graph.keys())):
            u = None
            for node in graph.keys():
                if not visited[node] and (u == None or self.dist[node] < self.dist[u]):
                    u = node

            if self.dist[u] == float("inf"):
                continue

            visited[u] = True

            for point, distance in graph[u]:
                if self.dist[u] + distance < self.dist[point]:
                    self.dist[point] = self.dist[u] + distance

        return self.dist[goal]

    def partA(self):
        return self.Dijkstra()

    def partB(self, char):
        if not self.dist:
            self.Dijkstra()

        #find "a's"
        desired = []
        for i, row in enumerate(self.map):
            for j, val in enumerate(row):
                if val == char:
                    desired.append(self.dist[(i,j)])

        return min(desired)
        
#################################
day12 = pathMap("day12.inp")
print(day12.partA())
print(day12.partB("a"))
