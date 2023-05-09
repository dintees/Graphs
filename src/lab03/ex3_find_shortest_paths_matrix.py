from .ex2_djikstra import dijkstra

def find_shortest_paths_matrix(edgesWithWeight, n):
    distanceMatrix = []
    for i in range(1, n+1):
        distances, _, _ = dijkstra(edgesWithWeight, n, i) 
        distanceMatrix.append(distances)
    return distanceMatrix
