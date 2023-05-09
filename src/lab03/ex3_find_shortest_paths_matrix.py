from .ex2_djikstra import dijkstra

def find_shortest_paths_matrix(edgesWithWeight, n):
    """Nodes start at 0"""
    edgesWithWeight = [((edges[0]+1, edges[1]+1), weight) for edges, weight in edgesWithWeight]
    distanceMatrix = []
    for i in range(1, n+1):
        distances, _, _ = dijkstra(edgesWithWeight, n, i) 
        distanceMatrix.append(distances)
    return distanceMatrix
