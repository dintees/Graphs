from ex1_generate_random_flow_network import generate_random_flow_network 
import copy
from math import inf

def BFS(n, G, f): 
    neighbours = [[] for _ in range(n-1)]
    for i in range(len(G)):
        if f[i] != 0:
            neighbours[G[i][0]].append(G[i][1]) 

    d = [inf for _ in range(n-1)]
    d.insert(0, 0)
    p = [0 for _ in range(n)]
    
    Q = [0]
    while len(Q) > 0:
        v = Q.pop(0)
        if v != n-1:
            for u in neighbours[v]: 
                if d[u] == inf:
                        d[u] = d[v]+1
                        p[u] = v
                        Q.append(u)

    index = len(p)-1
    nodes = [index]
    while index != 0:
        index = p[index]
        nodes.append(index)

    return [(nodes[i], nodes[i-1]) for i in range(len(nodes)-1,0,-1)]

def findCf(edges, G, c):
    cf = inf

    for edge in edges:
        if edge in G:
            id = G.index(edge)
            if c[id] < cf:
                cf = c[id]
        else:
            return None
    
    return cf   

def updateResedualGraph(G, edges, cf, cf_min):
    for i in range(len(G)):
        if G[i] in edges:
            cf[i] -= cf_min 
            if cf[i] == 0: 
                G[i] = None

    return cf


def ford_fulkerson(nodes, weightedEdges):
    # f - przepływ, c - przepustowość, G - krawiędzie sieci
    f = [0 for _ in range(len(weightedEdges))]
    c = [weightedEdge[2]['weight'] for weightedEdge in weightedEdges]
    G = [(weightedEdge[0], weightedEdge[1]) for weightedEdge in weightedEdges]

    # cf - przepustowość sieci rezydualnej, 
    # cf_min - minimalna przepustowość rezydualna,
    # f_max - maksymalmy przepływ na sieci (szukamy)
    cf = copy.deepcopy(c)
    cf_min = 0
    f_max = 0

    while cf_min != None: 
        # szukamy krótszej ścieżki rozszerzającej (krawiędzie)
        p = BFS(len(nodes), G, cf)
        cf_min = findCf(p, G, cf)

        # zwiększamy albo kasujemy przepływ wzdłuż ścieżki rozszerzającej
        if cf_min != None:
            f_max += cf_min
            for edge in p:
                id = G.index(edge)
                if edge in G:
                    f[id] = f[id] + cf_min
                else:
                    f[id] = f[id] - cf_min  

            # aktualizujemy sieć rezydualną
            cf = updateResedualGraph(G, p, cf, cf_min)

    return f_max   
