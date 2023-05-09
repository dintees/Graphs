class Vertice():
  def __init__(self, v: float, n: list):
    self.number = v
    self.neighbours = n

  def __str__(self):
    return f'{self.number}: {self.neighbours}'

  __repr__ = __str__

def DFS_visit(v, d, f, t, s, neighbourhood_list):
    t[0] += 1
    d[v - 1] = t[0]
    for u in neighbourhood_list[v - 1].neighbours:
        if d[u - 1] == -1:
            DFS_visit(u, d, f, t, s, neighbourhood_list)
    t[0] += 1
    f[v - 1] = t[0]
    s.append(v)

def transpose_graph(n):
    n_T_tmp = [[] for _ in n]
    for i in n:
      for n in i.neighbours:
        n_T_tmp[n - 1].append(i.number)

    n_T = [Vertice(i + 1, v) for i, v in enumerate(n_T_tmp)]
    return n_T

def components_r(nr, v, G_T, comp):
    neighbours = next(o.neighbours for o in G_T if o.number == v)
    for u in neighbours:
        if comp[u - 1] == -1:
            comp[u - 1] = nr[0]
            components_r(nr, u, G_T, comp)

def kosaraju(nodes, edges):
    # DFS init
    # nodes = [n+1 for n in nodes]
    # edges = [(e1+1, e2+1) for e1, e2 in edges]
    # neighbourhood_list = to_neighbourhood_list(nodes, edges)
    d = [-1 for i in nodes]
    f = [-1 for i in nodes]
    t = [0]
    s = [] # stack

    for v in nodes:
        if d[v - 1] == -1:
            DFS_visit(v, d, f, t, s, neighbourhood_list)

    # print(d)
    # print(f)
    # print("Stack", s)

    # G^T
    G_T = transpose_graph(neighbourhood_list)
    nr = [0]
    comp = [-1 for _ in range(len(G_T))]

    while len(s) > 0:
        v = s.pop()
        if comp[v - 1] == -1:
            nr[0] += 1
            comp[v - 1] = nr[0]
            components_r(nr, v, G_T, comp)
    return comp


def to_neighbourhood_list(nodes, edges):
    lists = {node:[] for node in nodes}
    for edge in edges:
        lists[edge[0]].append(edge[1])
    neighbourhood_list = [Vertice(node, l) for node, l in lists.items()]
    print(neighbourhood_list)
    return neighbourhood_list

def to_nodes_edges(neighbourhood_list):
    nodes = [v.number for v in neighbourhood_list]
    edges = [[] for n in neighbourhood_list]
    for v in neighbourhood_list:
        edges[v.number-1] = [nei for nei in v.neighbours]
    
    return nodes, edges





if __name__ == "__main__":
    neighbourhood_list = [
        Vertice(1, [7]),
        Vertice(2, [1, 3, 6, 7]),
        Vertice(3, [2, 6]),
        Vertice(4, [3, 5]),
        Vertice(5, [3]),
        Vertice(6, [5]),
        Vertice(7, [1])
    ]
    nodes = [i.number for i in neighbourhood_list]
    neighbourhood_list = [
        Vertice(1, [2, 3, 5]),
        Vertice(2, [1, 3, 4, 5, 7]),
        Vertice(3, [6]),
        Vertice(4, [2, 7]),
        Vertice(5, [7]),
        Vertice(6, [2]),
        Vertice(7, [6]),
    ]
    nodes, edges = to_nodes_edges(neighbourhood_list)
    # nodes, edges = [i.number for i in neighbourhood_list]
    print(nodes, edges)
    comp = kosaraju(nodes, edges)
    for i in range(max(comp)):
        print(f'Silna spojna skladowa {i+1}: {[nodes[j] for j in range(len(nodes)) if comp[j] == (i + 1) ]}')
