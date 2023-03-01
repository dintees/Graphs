import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample, random, randint

def randomNE(n, e):
    """Returns list of e random edges for nodes in range [0, n-1]"""
    if n*(n-1)/2 < e or n < 0 or e < 0:
        return None
    allEdges = combinations(range(n), 2)
    edges = sample(list(allEdges), e) 
    return edges 

def randomNP(n, p):
    """Returns list of random edges with probability p for nodes in range [0, n-1]"""
    if p < 0 or p > 1 or n < 0:
        return None 
    edges = combinations(range(n), 2)
    edges = list(filter(lambda _: random() < p, edges))
    return edges 

def showGraph(g):
    """Shows graph"""
    p = plt.figure(randint(0, 10e10))
    p.set_size_inches(8,8)
    node_opts = {"node_size": 500, "node_color": "tab:red", "edgecolors": "black", "linewidths": 1.0}
    pos = nx.circular_layout(g)
    nx.draw_networkx_nodes(g, pos, **node_opts)
    nx.draw_networkx_labels(g, pos, font_size=14)
    nx.draw_networkx_edges(g, pos, width=2.0, edge_color="black")
    p.tight_layout()
    p.show()

    
nodeCount = 5 
G = nx.Graph()
nodes = list(range(nodeCount))
edges = randomNP(nodeCount, 1)
G.add_nodes_from(nodes)
G.add_edges_from(edges)

showGraph(G)
showGraph(G)
#linijka ponizej zeby sie nie zamykalo
plt.show()