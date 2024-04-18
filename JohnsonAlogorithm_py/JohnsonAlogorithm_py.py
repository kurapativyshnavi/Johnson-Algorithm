import sys

def minDistance(dist, sptSet):
    min_val = sys.maxsize
    min_index = 0
    for v in range(V):
        if sptSet[v] == False and dist[v] <= min_val:
            min_val = dist[v]
            min_index = v
    return min_index

def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == sys.maxsize:
                print("{:>7s}".format("INF"), end="")
            else:
                print("{:>7d}".format(dist[i][j]), end="")
        print()

def floydWarshall(graph):
    dist = [[0 for x in range(V)] for y in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    printSolution(dist)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        V = int(f.readline().strip())
        graph = []
        for _ in range(V):
            row = f.readline().split()
            graph.append([int(x) if x != 'INF' else sys.maxsize for x in row])

    floydWarshall(graph)
