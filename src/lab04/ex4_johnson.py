from .ex3_bellman_ford import bellman_ford
from math import inf 

def johnson(nodes, edges):
    new_node = len(nodes)
    new_nodes = [node for node in nodes] + [new_node]
    new_edges = [[[edge[0][0], edge[0][1]], edge[1]] for edge in edges]

    for node in new_nodes[:-1]:
        new_edges.append([[new_node, node], 0])
    
    is_negative_cycle, d_s, p_s = bellman_ford(new_nodes, new_edges, new_node)
    h = [el for el in d_s]
    if is_negative_cycle:
        return "Negative cycle detected"


    reweighted_edges = []
    for [[u, v], w] in new_edges:
        reweighted_edges.append([[u, v], w + h[u] - h[v]])

    shortest_paths = [None for _ in new_nodes]
    for node in new_nodes:
        is_negative_cycle, d_s, _ = bellman_ford(new_nodes, reweighted_edges, node)
        if is_negative_cycle:
            return "Negative cycle detected"
        shortest_paths[node] = d_s[:-1]
    
    shortest_paths = shortest_paths[:-1]
    
    for u in range(len(shortest_paths)):
        for v in range(len(shortest_paths[u])):
            if shortest_paths[u][v] == inf:
                return "Graph is not strongly connected"
            shortest_paths[u][v] += -h[u] + h[v]
    
    return shortest_paths