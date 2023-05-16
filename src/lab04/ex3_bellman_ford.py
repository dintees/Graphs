from math import inf

def relax(edge, d_s, p_s):
    u, v = edge[0]
    w = edge[1]
    if d_s[v] > d_s[u] + w:
        d_s[v] = d_s[u] + w
        p_s[v] = u

def bellman_ford(nodes, edges, source):
    n = len(nodes)
    d_s = [inf for _ in nodes]
    p_s = [None for _ in nodes]

    d_s[source] = 0
    for _ in range(0, n-1): 
        for edge in edges:
            relax(edge, d_s, p_s)

    is_negative_cycle = False
    for edge in edges: 
        u, v = edge[0]
        w = edge[1]
        if d_s[v] > d_s[u] + w:
            is_negative_cycle = True
            return is_negative_cycle, d_s, p_s

    return is_negative_cycle, d_s, p_s 


